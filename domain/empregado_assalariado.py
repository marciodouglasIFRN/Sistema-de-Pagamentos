from domain.empregado_horista import Empregado

class EmpregadoAssalariado(Empregado):

    def __init__(self):
        self.__salarioMensal = 0
        self.__taxaDeComicao = 0

    def getSalario(self):
        return self.__salarioMensal


