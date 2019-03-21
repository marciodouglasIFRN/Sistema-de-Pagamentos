class Empregado:
    def __init__(self,numero,nome,endereco):
        self.__numero = numero
        self.__nome = nome
        self.__endereco = endereco

    def __str__(self):
        return 'Número: {} | Nome: {} | Endereço: {}'.format(self.__numero,self.__nome,self.__endereco)

    def getNumero(self):
        return self.__numero

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self,endereco):
        self.__endereco = endereco