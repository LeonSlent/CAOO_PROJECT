from abc import ABC, abstractmethod
from .classificacao import Classificacao

# (Classes Base)

class Handler(ABC):
    
    # Interface base para todos os elos da corrente.
    
    def __init__(self):
        self._proximo = None

    def set_proximo(self, handler):
        # Define quem é o próximo passo da corrente.
        self._proximo = handler
        return handler  # Retorna o handler para permitir encadeamento visual

    @abstractmethod
    def handle(self, contexto):
        
        # Método que processa a lógica.
        # Se tiver um próximo e não houver erro fatal, passa a bola para frente.
        
        # Se já existe um erro marcado no contexto, a gente para a corrente
        if contexto.get('erro'):
            return contexto

        # Se existe um próximo passo, chama ele
        if self._proximo:
            return self._proximo.handle(contexto)
        
        return contexto


# 2. OS ELO CONCRETOS

class ValidadorHandler(Handler):
    
    # ELO 1: Responsável por verificar se os dados vindos da View são válidos. Converte strings para float e checa campos vazios.
    
    def handle(self, contexto):
        # 1. Valida Nome
        nome = contexto.get('nome_bruto')
        if not nome:
            contexto['erro'] = "O nome do atleta é obrigatório."
            return contexto # Para a corrente aqui (retorna com erro)

        # 2. Valida Números
        dados_strings = contexto.get('dados_brutos_strings', [])
        dados_convertidos = []
        
        # Verifica se tem os 8 campos
        if len(dados_strings) != 8:
            contexto['erro'] = "Faltam dados físicos."
            return contexto

        try:
            for valor_str in dados_strings:
                # Tenta converter string "1,80" ou "1.80" para float
                valor_float = float(valor_str.replace(',', '.'))
                
                if valor_float <= 0:
                    contexto['erro'] = "Valores devem ser maiores que zero."
                    return contexto
                
                dados_convertidos.append(valor_float)

        except ValueError:
            contexto['erro'] = "Campos numéricos devem conter apenas números."
            return contexto

        # Se passou, salva os dados limpos no contexto e chama o próximo (super)
        contexto['dados_processados'] = dados_convertidos
        return super().handle(contexto)


class ClassificadorKMeansHandler(Handler):
    
    # ELO 2: Pega os dados numéricos e joga no K-Means
    
    def __init__(self):
        super().__init__()
        self.servico = Classificacao() # Carrega o .joblib

    def handle(self, contexto):
        dados = contexto.get('dados_processados')
        
        # Chama o serviço de IA
        cluster_id = self.servico.classificar(dados)
        
        if cluster_id is None:
            contexto['erro'] = "Erro interno: Falha ao carregar modelo K-Means."
            return contexto
            
        contexto['cluster_id'] = cluster_id
        return super().handle(contexto)


class InterpretadorHandler(Handler):
    
    # ELO 3: Traduz o número do cluster (0, 1, 2) para texto (Armador, Ala, Pivô).
    
    def handle(self, contexto):
        cluster_id = contexto.get('cluster_id')
        
        # Lógica de negócio definida no treinamento
        mapa_posicoes = {
            0: "Armador",
            1: "Ala",
            2: "Pivô"
        }
        
        posicao = mapa_posicoes.get(cluster_id, "Desconhecido")
        contexto['posicao_final'] = posicao
        contexto['sucesso_processamento'] = True
        
        # Fim da linha, não precisa chamar super().handle se for o último,
        # mas é boa prática chamar caso adicione mais passos no futuro.
        return super().handle(contexto)


# 3. (O que seu Controller vai chamar)

class PipelineClassificacao:
    def __init__(self):
        # Montagem da Cadeia de Responsabilidade
        self.validador = ValidadorHandler()
        self.classificador = ClassificadorKMeansHandler()
        self.interpretador = InterpretadorHandler()

        # Configura a ordem: Valida -> Classifica -> Interpreta
        self.validador.set_proximo(self.classificador).set_proximo(self.interpretador)

    def executar_fluxo_completo(self, nome, dados_strings, banco_dados):
        
        # Esta função roda a chain e retorna EXATAMENTE o que seu Controller quer:
        # - False (se der erro)
        # - Ou a String da Posição (se der certo)
        
        
        # 1. Cria o "Envelope" (Contexto) que vai viajar pela corrente
        contexto = {
            'nome_bruto': nome,
            'dados_brutos_strings': dados_strings,
            'erro': None,
            'sucesso_processamento': False,
            'posicao_final': None,
            'dados_processados': []
        }

        # 2. Dispara a Chain (Começa pelo validador)
        resultado = self.validador.handle(contexto)

        # 3. Verifica se a Chain devolveu erro
        if resultado['erro']:
            print(f"Erro na Chain: {resultado['erro']}") # Log opcional
            return False  # <--- Retorna False para o Controller avisar a View

        # 4. Se a Chain teve sucesso, faz a persistência (Banco de Dados)
        # A persistência pode ficar aqui no Manager/Facade para garantir atomicidade
        if resultado['sucesso_processamento']:
            salvou = banco_dados.salvar_atleta(
                resultado['nome_bruto'],
                resultado['dados_processados'],
                resultado['posicao_final']
            )
            
            if salvou:
                return resultado['posicao_final'] # Retorna a string "Armador", "Ala"
            else:
                return False # Erro no banco

        return False