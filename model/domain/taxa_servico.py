class TaxaServico:
    def __init__(self,data,valor):
        self.__data = data
        self.__valor = valor

    def getValor(self):
        return self.__valor

    def getData(self):
        return self.__data