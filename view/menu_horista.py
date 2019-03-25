

class MenuHorista:
    def __init__(self,horista):
        self.__horista = horista

    def printMenu(self):
        str = 'entrada'
        while True:

            op = int(input('1- Bater ponto de '+str+'\n'
                                                    '2- Sair\n'))
            if op == 1:
                if str == 'entrada':
                    self.__horista.registrarEntrada()
                    str = 'saida'
                else:
                    self.__horista.registrarSaida()
                    str = 'entrada'
            elif op == 2:
                break