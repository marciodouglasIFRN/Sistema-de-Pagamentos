from model.domain.empregado_horista import Empregado
from model.domain.resultado_da_venda import ResultadoDaVenda
from datetime import datetime

class EmpregadoAssalariado(Empregado):

    def __init__(self,numero,salarioMensal,nome,endereco,taxaDeComicao):
        super().__init__(numero,nome,endereco)
        self.__salarioMensal = salarioMensal
        self.__taxaDeComicao = taxaDeComicao
        self.__vendas = []

    def getSalario(self):
        if self.__heComicionado():
            return self.__salarioMensal*self.__taxaDeComicao/100+self.__salarioMensal
        return self.__salarioMensal

    def __str__(self):
        if self.heComicionado():
            return '{} | Tipo: Comicionado | Salário por mês: {} | comição: {}' \
            .format(super().__str__(), self.__salarioMensal, self.__taxaDeComicao)
        return '{} | Tipo: Assalariado | Salário por mês: {}' \
            .format(super().__str__(), self.__salarioMensal)

    def realizarVenda(self,data,valor):
        self.__vendas.append(ResultadoDaVenda(datetime.now(),valor))

    def heComicionado(self):
        if self.__taxaDeComicao != None:
            return True
        return False