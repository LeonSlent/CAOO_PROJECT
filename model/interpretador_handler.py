from model.interface_handler import Handler

class InterpretadorHandler(Handler):
    def handle(self, contexto):
        cluster_id = contexto.get('cluster_id')
        
        mapa_posicoes = {
            0: "Armador",
            1: "Ala",
            2: "Pivô"
        }
        
        posicao = mapa_posicoes.get(cluster_id, "Desconhecido")
        contexto['posicao_final'] = posicao
        contexto['sucesso_processamento'] = True
        
        return super().handle(contexto)