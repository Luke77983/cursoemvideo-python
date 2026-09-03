import cafeteria

def main():
    b1 = cafeteria.Cafe()
    b2 = cafeteria.Cha()
    b3 = cafeteria.Leite()

    b1.preparar()
    b2.preparar()
    b3.preparar()
if __name__ == '__main__':
    main()