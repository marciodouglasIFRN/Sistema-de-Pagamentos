class MenuHorista:
    def __init__(self,horista):
        self.__horista = horista

    def printMenu(self):
        while True:
            op = input('1- Sair')
            if op == 1:
                break