from rich import print
from desafios.desafio038.classe038 import *
def main():
   p1 = Produto("Mouse", 325)
   p2 = Produto("Teclado",433)
   p3 = Produto("Memória 256",1_000)
   p4 = Produto("Placa de video",25_999)

   c1 = Carrinho()
   c2 = Carrinho()

   c1 = c1 + p1 + p2 + p3
   print(c1)
if __name__ == '__main__':
    main()