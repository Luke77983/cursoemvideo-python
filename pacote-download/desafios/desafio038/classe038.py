
class Produto:
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:,.2f}) ".replace(',', '_').replace('.', ',').replace('_', '.')

class Carrinho:
    def __init__(self):
        self.produtos = []
    def __add__(self, produto):
        self.produtos.append(produto)
        return self
    def __str__(self):
        txt = ''
        for i in self.produtos:
            txt += f"\n{i}"
        return f"{txt} \nTotal: {self.total:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')

    @property
    def total(self):
        soma = 0
        for p in self.produtos:
            soma += p.preco
        return soma

