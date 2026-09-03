from rich import  print
from transportes import *


def main():
    dist = 80

    '''entrega = Drone(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}')'''
    viagem = [Moto(dist), Caminhao(dist),Drone(dist)]
    tab = Table(title='Tabela de Fretes')
    tab.add_column('Distância', justify='left')
    tab.add_column('Tipo', justify='center')
    tab.add_column('Frete', justify='right')

    for item in viagem:
        tab.add_row(f'{dist}km',f'{type(item).__name__}',f'{item.calc_frete()}')
    print(tab)
if __name__ == '__main__':
    main()