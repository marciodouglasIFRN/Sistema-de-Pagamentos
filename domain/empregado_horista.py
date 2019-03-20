from domain.empregado import Empregado

class EmpregadoHorista(Empregado):

    def __init__(self,numero,salarioPorHora,nome,endereco):
        super().__init__(numero, nome, endereco)
        self.__salarioPorHora = salarioPorHora
        self.__cartaoDePonto = None

    def __str__(self):
        return '{} | Tipo: Horista | Salário por hora: {}'\
            .format(super().__str__(),super().getEndereco(),self.__salarioPorHora)
