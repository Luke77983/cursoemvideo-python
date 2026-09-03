from rich import print
from rich import inspect
class Funcionario:
    empresa = 'Curso em video'
    def __init__(self, n, setor, cargo):
        self.nome = n
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return f':handshake:Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em video da empresa {Funcionario.empresa}'


c1 = Funcionario('Maria', 'Administração', 'Diretora')
c1.empresa = 'Estudonauta'
print(c1.apresentação())
inspect(c1)

c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentação())
inspect(c2)