from model.domain.empregado import Empregado
from datetime import datetime

class EmpregadoHorista(Empregado):

    def __init__(self,numero,salarioPorHora,nome,endereco):
        super().__init__(numero, nome, endereco)
        self.__salarioPorHora = salarioPorHora
        self.__cartaoDePonto = []
        self.__entrada = None

    def __str__(self):
        return '{} | Tipo: Horista | Salário por hora: {}'\
            .format(super().__str__(),self.__salarioPorHora)

    def registrarEntrada(self):
        self.__entrada = datetime.now()

    def registraSaida(self):
        saida = datetime.now()


