from model.validador_handler import ValidadorHandler
from model.classificador_handler import ClassificadorKMeansHandler
from model.interpretador_handler import InterpretadorHandler

class PipelineClassificacao:
    def __init__(self):
        # Monta a corrente aqui
        self.validador = ValidadorHandler()
        self.classificador = ClassificadorKMeansHandler()
        self.interpretador = InterpretadorHandler()

        # Liga os elos
        self.validador.set_proximo(self.classificador).set_proximo(self.interpretador)

    def executar_fluxo_completo(self, nome, dados_strings, banco_dados):
        # Cria o envelope de dados
        contexto = {
            'nome_bruto': nome,
            'dados_brutos_strings': dados_strings,
            'erro': None,
            'sucesso_processamento': False,
            'posicao_final': None,
            'dados_processados': []
        }

        # Roda a corrente
        resultado = self.validador.handle(contexto)

        # Verifica Erro
        if resultado['erro']:
            # Você pode descomentar o print abaixo para ver o erro no terminal
            # print(f"Erro: {resultado['erro']}")
            return False

        # Tenta Salvar no Banco
        if resultado['sucesso_processamento']:
            salvou = banco_dados.salvar_atleta(
                resultado['nome_bruto'],
                resultado['dados_processados'],
                resultado['posicao_final']
            )
            
            if salvou:
                return resultado['posicao_final'] # SUCESSO!
            
        return False