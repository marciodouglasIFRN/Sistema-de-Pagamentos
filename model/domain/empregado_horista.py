from model.domain.cartao_de_ponto import CartaoDePonto
from model.domain.empregado import Empregado
from datetime import datetime

class EmpregadoHorista(Empregado):

    def __init__(self,numero,salarioPorHora,nome,endereco):
        super().__init__(numero, nome, endereco)
        self.__salarioPorHora = salarioPorHora
        self.__cartoesDePonto = []
        self.__entrada = None

    def __str__(self):
        return '{} | Tipo: Horista | Salário por hora: {}'\
            .format(super().__str__(),self.__salarioPorHora)

    def registrarEntrada(self):
        self.__entrada = datetime.now().hour


    def registrarSaida(self):
        saida = datetime.now()
        horasTrabalhadas =  saida.hour - self.__entrada
        self.__cartoesDePonto.append(CartaoDePonto(saida.day, horasTrabalhadas))

    def getSalario(self):
        horasTrabalhada = 0
        for cartao in self.__cartoesDePonto:
            horasTrabalhada += cartao.getHora()
        return horasTrabalhada * self.__salarioPorHora


