from domain.empregado import Empregado

class EmpregadoHorista(Empregado):

    def __init__(self,salarioPorHora,nome,endereco):
        super().__init__(nome,endereco)
        self.__salarioPorHora = salarioPorHora
        self.__cartaoDePonto = None

    def __str__(self):
        return 'Nome: {} | Endereço: {} | Tipo: Horista | Salário por hora: {}'\
            .format(super().__str__(),super().getEndereco(),self.__salarioPorHora)
