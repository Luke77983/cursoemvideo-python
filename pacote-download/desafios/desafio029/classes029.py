from rich import print
class Diario:
    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self,msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())


    def ler(self,senha=None):
        if senha != self.__senha:
            raise PermissionError('Senha inválida! Você não pode ler meu diário!')
        else:
            print('[green]Diário LIBERADO[/]')
            for s in self.__segredos:
                print(f'- {s}')

    @property
    def senha(self):
       return PermissionError('Ninguém tem permissão de ver a senha')

    @senha.setter
    def senha(self,senhanova):
        self.__senha = senhanova