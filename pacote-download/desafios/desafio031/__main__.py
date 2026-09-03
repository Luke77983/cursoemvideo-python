from rich import inspect

from desafios.desafio031.classe031 import *

def main():
    r = Retangulo()
    try:
        r.base = 12
        r.altura = -4
    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}: {e}')

    print(r.medidas)
    # inspect(r,private=True, methods=True)


if __name__ == '__main__':
    main()