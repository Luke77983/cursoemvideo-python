from rich import print
from rich.panel import Panel
from rich import inspect
class Gamer:
    def __init__(self, nome, nick ):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    def add_favoritos(self, f=''):
        self.jogos.append(f)
        self.jogos = sorted(self.jogos, key=str.lower)
    def ficha(self):
        stat = f'Nome real: [black on blue]{self.nome}[/]'
        stat += '\nJogos favoritos:'
        for j in self.jogos:
            stat += f'\n[blue]:video_game: {j}[/]'
        painel = Panel(stat,title=f'Jogador <{self.nick}>', width=34)
        print(painel)
j1 = Gamer('Fabricio da Silva', 'detonator2025')
j1.add_favoritos('Mario bros')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of war')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.add_favoritos('Mario Bros')
j2.add_favoritos('Call of Duty')
j2.ficha()