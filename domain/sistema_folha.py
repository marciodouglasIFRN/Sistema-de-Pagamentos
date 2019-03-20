from domain.empregado_horista import EmpregadoHorista
from domain.empregado_assalariado import EmpregadoAssalariado
from persistencia.banco import funcionarios

class SistemaFolha:

    def cadastrarEmpregadoHorista(self,nome,endereco,salarioPorHora,cartaoDePontos):
        funcionarios.append(EmpregadoHorista(salarioPorHora,nome,endereco))

    def cadastrarEmpregadoAssalariado(self, nome, endereco, salarioMensal,taxaDeComicao=None):
        funcionarios.append(EmpregadoAssalariado(salarioMensal, nome, endereco,taxaDeComicao))

    def listarEmpregados(self):
        return funcionarios