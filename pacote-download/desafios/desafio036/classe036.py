from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor= None):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def fvalor(self):
        return f"R$ {self.valor:,.2f}"

    def pagar(self):
        return f"{self.fvalor} via {self.__class__.__name__}"

class Boleto(Pagamento):
    pass



class Pix(Pagamento):
    pass

class Credito(Pagamento):
    pass

def finalizar_compra(objeto, pag):
    objeto.valor = pag
    print(f"Pagamento  CONFIRMADO de {objeto.pagar()}")