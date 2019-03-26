class Sindicato:
    def __init__(self):
        self.__membros = []

    def associarFuncionario(self,membro):
        self.__membros.append(membro)

    def getMembros(self):
        self.__membros