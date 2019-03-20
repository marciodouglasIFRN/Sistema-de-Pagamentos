class Empregado:
    def __init__(self,nome,endereco):
        self.__nome = nome
        self.__endereco = endereco

    def __str__(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco