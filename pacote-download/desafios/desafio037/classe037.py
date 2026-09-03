from rich import print
from rich.panel import Panel


class Mensagem:
    def __init__(self, txt: str = None):
        self.mensagem = txt
        self._tipo = f"AVISO"
        self._icone = ':thought_balloon:'

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novotipo):
        self._tipo = novotipo

    @property
    def icone(self):
        return self._icone

    @tipo.setter
    def tipo(self, novotipo):
        self._tipo = novotipo

    def mostrar(self):
        tipo = f'{self.icone} {self.tipo} {self.icone}'
        painel = Panel(f'{self.mensagem}', title=tipo,width=45, style='white on black')
        print(painel)

class Erro:
   def __init__(self, txt):
       self.mensagem = txt
       self.tipo = 'ERRO'
       self.icone = f":prohibited:"

   def mostrar(self):
       tipo = f'{self.icone} {self.tipo} {self.icone}'
       painel = Panel(f'{self.mensagem}', title=tipo, width=45,style='yellow on red')
       print(painel)
class Aviso:
    def __init__(self, txt):
        self.mensagem = txt
        self.tipo = 'ALERTA'
        self.icone = f":warning:"

    def mostrar(self):
        tipo = f'{self.icone} {self.tipo} {self.icone}'
        painel = Panel(f'{self.mensagem}', title=tipo, width=45, style='black on yellow')
        print(painel)
