from rich import inspect,print
from desafios.desafio034.classe034 import *
def main():

    funcionarios = [Desenvolvedor("Pedro", 18_000),
                    Designer("José", 25_000),
                    Gerente("Mariana", 45_000)
                    ]
    for f in funcionarios:
        print(f)

if __name__ == '__main__':
    main()