from model.interface_handler import Handler
from model.classificacao import Classificacao

class ClassificadorKMeansHandler(Handler):
    def __init__(self):
        super().__init__()
        self.servico = Classificacao()

    def handle(self, contexto):
        dados = contexto.get('dados_processados')
        
        # Chama a IA
        cluster_id = self.servico.classificar(dados)
        
        if cluster_id is None:
            contexto['erro'] = "Erro interno: Falha ao carregar modelo K-Means."
            return contexto
            
        contexto['cluster_id'] = cluster_id
        return super().handle(contexto)