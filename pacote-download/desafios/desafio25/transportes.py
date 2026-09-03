from abc import ABC, abstractmethod
from rich.table import Table


class Transporte(ABC):
    def __init__(self, distancia):
        self.distacia = distancia
        self.frete = 0


    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
    fator = 0.50

    def calc_frete(self):
        self.frete = self.distacia * Moto.fator
        return f'R${self.frete:.2f}'


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    fator = 1.20

    def calc_frete(self):
        self.frete = self.distacia * Caminhao.fator
        if self.distacia < 50:
            return f'Raio mínimo de 50km'
        else:
            return f'R${self.frete:.2f}'


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    fator = 9.50

    def calc_frete(self):
        self.frete = self.distacia * Drone.fator
        if self.distacia > 10:
            return f'Raio máximo de 10km'
        else:
            return f'R${self.frete:.2f}'
