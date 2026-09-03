from desafios.desafio032.classes032 import *

def main():
    print('Criando a conta...')
    cc = ContaBancaria(123,'Gustavo', 10000,)

    print('Vou tentar sacar...')
    cc.sacar(500)

    print('Tentando muddar o nome...')
    cc.nome = 'Maricota'

    print(cc)



if __name__ == '__main__':
    main()