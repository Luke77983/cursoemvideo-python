from rich import inspect, print

from desafios.desafio028.termostato import *

def main():
    t = Termostato()
    try:
        t.temperatura = 25.3
        print(t.ftemperatura)
    except Exception as e:
        print(f'Houve um problema: {e}')
        print(f'A temperatura atual é de {t.ftemperatura}')



if __name__ == '__main__':
    main()