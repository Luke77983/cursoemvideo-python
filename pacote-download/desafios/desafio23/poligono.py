from abc import ABC,abstractmethod
class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, tamanho, qtd_lados = 4):
        super().__init__(qtd_lados)
        self.tamanho = tamanho
    def perimetro(self):
        perim = self.qtd_lados * self.tamanho
        return perim
    def area(self):
        area = self.tamanho * self.tamanho
        return area
class Circulo(Poligono):
    def __init__(self, raio, qtd_lados = 2):
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self):
         perim = self.qtd_lados * 3.14 * self.raio
         return perim
    def area(self):
         area = self.raio * (self.raio * 3.14)
         return area
