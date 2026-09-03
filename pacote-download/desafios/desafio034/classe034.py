from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self, nome:str|None = None, salario:float= 1_621):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor:float = None):
        if valor is None:
            raise  ValueError("Impossivel reajustar o salário desse jeito!")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError(f"Você não pode reduzir o salário de um funcionário.")


    @abstractmethod
    def calcular_bonus(self, valor:int):
        pass

    def __str__(self):
        return f"{self.nome} ganha {self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}"
class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        bonus = self.salario / 100 * 15
        return bonus


class Designer(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)


    def calcular_bonus(self):
        bonus = self.salario / 100 * 8
        return bonus


class Desenvolvedor(Funcionario):

    def __init__(self, nome, salario):
        super().__init__(nome, salario)


    def calcular_bonus(self):
        bonus = self.salario / 100 * 10
        return bonus



