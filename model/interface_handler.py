from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._proximo = None

    def set_proximo(self, handler):
        self._proximo = handler
        return handler

    @abstractmethod
    def handle(self, contexto):
        # Se já tem erro, para e retorna
        if contexto.get('erro'):
            return contexto

        # Passa para o próximo
        if self._proximo:
            return self._proximo.handle(contexto)
        
        return contexto