from rich import inspect

from desafios.desafio033.classe033 import Aluno


def main():
    a = Aluno('Maria', 1978, 'ads')
    b = Aluno('Pedro', 2015, 'ENG')

    a.add_curso('MODA')
    print(b.cursos_oficiais)
if __name__ == '__main__':
    main()