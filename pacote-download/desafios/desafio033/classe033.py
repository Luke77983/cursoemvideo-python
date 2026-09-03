from datetime import date
from abc import ABC,abstractmethod
class Pessoa(ABC)  :
    def __init__(self, nome:str,nasc):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        if  ano < 1900 or ano > date.today().year:
            raise ValueError(f'Ano {ano} é inválido')
        else:
            self._nascimento = ano

    @property
    def idade(self):
        return date.today().year - self._nascimento
    @idade.setter
    def idade(self, valor):
        raise PermissionError('Você não pode alterar a idade. Mude o ano de nascimento')

class Aluno (Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    def __init__(self, nome: str, nasc, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if curso.upper()  in Aluno.cursos_oficiais:
            self._curso = curso.upper()
        else:
            self._curso = None
            raise ValueError(f'O Curso {curso} não está na lista de cursos oficiais.')

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if curso not in Aluno.cursos_oficiais:
            if 3 <= len(curso) <= 5:
                Aluno.cursos_oficiais.append(curso)
            else:
                raise ValueError(f'Nome {curso} está fora do padrão para Cursos')
        else:
            raise ValueError(f'O {curso} ja existe na lista')