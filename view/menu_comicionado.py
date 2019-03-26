
class MenuAssalariado:
    def __init__(self,comicionado):
        self.__comicionado = comicionado

    def printMenu(self):
        while True:
            op = int(input('1-Realizar venda\n'
                           '2-Lançar resultado de venda\n'
                           '3-Sair\n'))
            if op == 1:
                pass
            elif op == 2:
                data = input('Informe a data da venda\n')
                valor = input('Informe o valor da venda\n')
                self.__comicionado.lancarResultadoVenda(data,valor)
            elif op == 3:
                break