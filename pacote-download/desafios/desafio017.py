from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    def etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'R${self.preço:,.2f}'
        conteudo += f'{precof.center(30,'.')}'
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)
p1 = Produto('Iphone 17 pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('Notebook Gamer', 8_000 )
p2.etiqueta()