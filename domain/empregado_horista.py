from domain.empregado import Empregado

class EmpregadoHorista(Empregado):

    def __init__(self,salarioPorHora):
        self.__salarioPorHora = salarioPorHora
        self.__cartaoDePonto = None
