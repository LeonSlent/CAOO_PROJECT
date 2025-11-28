from model.pipeline import PipelineClassificacao
from model.gerenciador_bd import GerenciadorBD
from view.view import View

class MainController:
    
    def __init__(self):
        self.db = GerenciadorBD()
        self.pipeline = PipelineClassificacao()
        self.view = View(self)
        
    def validar_entrada_view(self, nome, dados_brutos):
        """
        Recebe os dados da View, chama o Model e retorna o resultado.
        Retorna: A posição (str) se sucesso, ou False se erro.
        """
        # Chama o Model (que retorna False ou a String da posição)
        resultado = self.pipeline.executar_fluxo_completo(nome, dados_brutos, self.db)
        
        return resultado
    
    def buscar_todos_atletas(self):
        return self.db.buscar_todos_atletas()
    
    def excluir_atleta(self, id_atleta):
        return self.db.excluir_atleta(id_atleta)

    def fun_troca_tela(self, tela_nova):
        if self.view.frame_atual:
            self.view.frame_atual.destroy()
        tela_nova()

    def pesquisar_atleta(self, nome):
        return self.db.buscar_atletas_por_nome(nome)

    def run (self):
        self.view.main_loop()
