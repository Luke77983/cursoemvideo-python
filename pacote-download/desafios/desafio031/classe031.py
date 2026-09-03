class Retangulo:
    def __init__(self, base = 1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor,float) and not isinstance(valor, int):
            raise TypeError('O valor da base deve ser um número')
        if valor < 0:
            raise ValueError('Valor inválido para a base')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError('O valor da altura deve ser um número')
        if valor < 0:
            raise ValueError('Valor inválido para a altura')
        else:
            self._altura = valor


    @property
    def medidas(self):
        return f'Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}'


    @medidas.setter
    def medidas(self, valor):
        self.base = valor[0]
        self.altura = valor[1]

    @property
    def area(self):
        return self._base * self._altura

    @area.setter
    def area(self):
        raise  PermissionError('Àrea não pode ser configurada desse jeito.')