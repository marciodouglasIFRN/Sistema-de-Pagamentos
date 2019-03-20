from domain.empregado_horista import Empregado

class EmpregadoAssalariado(Empregado):

    def __init__(self,salarioMensal,nome,endereco,taxaDeComicao):
        super().__init__(nome,endereco)
        self.__salarioMensal = salarioMensal
        self.__taxaDeComicao = taxaDeComicao

    def getSalario(self):
        if self.__heComicionado():
            return self.__salarioMensal*self.__taxaDeComicao/100+self.__salarioMensal
        return self.__salarioMensal

    def __str__(self):
        if self.__heComicionado():
            return 'Nome: {} | Endereço: {} | Tipo: Assalariado | Salário por mês: {}'\
                .format(super().__str__(),super().getEndereco(),self.__salarioMensal)
        return 'Nome: {} | Endereço: {} | Tipo: Comicionado | Salário por mês: {} | comição: {}' \
            .format(super().__str__(), super().getEndereco(), self.__salarioMensal, self.__taxaDeComicao)

    def __heComicionado(self):
        if self.__taxaDeComicao != None:
            return True
        return False