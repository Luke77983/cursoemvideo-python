from desafios.desafio035.classe035 import *
def main():
    a1 = DOC('prova',550_000)
    a2 = PDF('contrato', 850000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)

if __name__ == '__main__':
    main()