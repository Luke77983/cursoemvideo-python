from abc import ABC,abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
    sal_min = 1612
    inss = 7.5
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f'O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario/self.sal_min:.1f} sálarios mínimos[/].'
        painel = Panel(conteudo, title='Análise de Salário',width=50)
        print(painel)


class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora=7.37, qtd_horas=220):
        self.valor_hora = valor_hora
        self.horas_trab = qtd_horas
        super().__init__(nome)
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        desc = (Funcionario.inss / 100) * self.sal_bruto
        self.salario = self.sal_bruto - desc
        return self.salario




class FuncionarioMensalista(Funcionario):
    def __init__(self, nome,salario_bruto= Funcionario.sal_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_sal(self):
       desc = (Funcionario.inss / 100 ) * self.salario_bruto
       self.salario = self.salario_bruto - desc
       return self.salario
