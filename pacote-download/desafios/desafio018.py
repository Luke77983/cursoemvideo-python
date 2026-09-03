from rich import print
from rich.panel import Panel
class Churrasco:
    # Atributos de classe
    consumo_padrao:float = 0.400 #Cada pessoa come em media 400g de carne
    preco_Kg:float = 82.40 #Cada Kg de carne custa 82.40
    def __init__(self, titulo='', quant=0):
        self.titulo = titulo
        self.quant = quant
    def __str__(self):
        return f'Esse é {self.titulo} com {self.quant} pessoas participando.'

    def calcular_qtd_carne(self)-> float:
        return self.quant * Churrasco.consumo_padrao
    def calcular_custo_total(self)-> float:
        return self.calcular_qtd_carne() * Churrasco.preco_Kg
    def calcular_custo_individual(self)-> float:
        return self.calcular_custo_total() / self.quant
    def Analisar(self):
        conteudo = f'Analizando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]'
        conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_Kg:,.2f}'
        conteudo += f'\nRecomendo comprar {self.calcular_qtd_carne():.3f}Kg de carne'
        conteudo += f'\ncusto total será de RS{self.calcular_custo_total():.2f}'
        conteudo += f'\nCada pessoa pagará RS{self.calcular_custo_individual():.2f} para participar'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
c1 = Churrasco('Churras dos Amigos', 15)
c1.Analisar()