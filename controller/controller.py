from view.view import View


class Controller:
    def __init__(self):
        self.view = View(self)

    def fun_troca_tela(self, tela_nova):
        if self.view.frame_atual:
            self.view.frame_atual.destroy()
        tela_nova()

    def run (self):
        self.view.main_loop()