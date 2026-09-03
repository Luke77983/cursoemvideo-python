from desafios.desafio030.classe030 import Credencial

def main():
    c = Credencial()
    c.senha ='alohomora'
    print(c.senha)
    c.validar('alohomora')
if __name__ == '__main__':
    main()