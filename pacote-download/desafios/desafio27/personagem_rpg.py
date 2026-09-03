from abc import ABC,abstractmethod
from rich import print
import random
from rich.panel import Panel


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.forca = 0
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        self.forca = forca
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'[green]{self.nome}[/] ({self.vida}) atacou [red]{alvo.nome}[/] com um [blue]{golpe}[/] de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer')


    def receber_dano(self, dano):
        fator = random.randint(0,dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]')




    @abstractmethod
    def curar(self):
        pass

    def player_status(self, pers):
        conteudo = f'[green]Vida[/]: {pers.vida}'
        conteudo += f'\n[blue]Força[/]: {self.forca}'
        conteudo += f'\n[red]Golpes[/]: '
        for g in self.golpes:
            conteudo += (f' {g} ')
        painel = Panel(conteudo, title=f'{pers.nome}', width=50)
        print(painel)



class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Chute giratório', 'Golpe de Machado']


    def curar(self):
        fator = random.randint(0,100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] enrolou uma atadura mos ferimentos e [green]recuperou {fator} pontos[/] de vida.')



class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Raio de Luz', 'Magia Estática']

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {fator} pontos[/] de vida.')


