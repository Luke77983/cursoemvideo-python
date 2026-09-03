from rich import inspect, print

from desafios.desafio029.classes029 import Diario

def main():
   d = Diario()
   d.escrever('Essa é a primeira mensagen')
   d.escrever('Estou aprendendo python')
   d.senha = 'alohomora'
   d.ler('alohomora')
   inspect(d, private=True)

    # inspect(d, private=True, methods=True)


if __name__ == '__main__':
    main()