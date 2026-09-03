from funcionarios import *

def main():
    f1 = FuncionarioMensalista('José da silva', 8500)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = FuncionarioHorista('Amanda', 25,250)
    f2.calc_sal()
    f2.analisar_sal()
if __name__ == '__main__':
    main()