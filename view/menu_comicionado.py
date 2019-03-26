
class MenuAssalariado:
    def __init__(self,comicionado):
        self.__comicionado = comicionado

    def printMenu(self):
        while True:
            op = int(input('1-Realizar venda\n'
                           '2-Sair\n'))
            if op == 1:
                pass
            elif op == 2:
                break