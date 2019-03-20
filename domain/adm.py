from domain.empregado_horista import EmpregadoHorista
from domain.empregado_assalariado import EmpregadoAssalariado
from persistencia.banco import funcionarios

class Adm:
    def cadastrarEmpregadoHorista(self,nome,endereco,salarioPorHora):
        funcionarios.append(EmpregadoHorista(self.__geraId(),salarioPorHora,nome,endereco))

    def cadastrarEmpregadoAssalariado(self, nome, endereco, salarioMensal,taxaDeComicao=None):
        funcionarios.append(EmpregadoAssalariado(self.__geraId(),salarioMensal, nome, endereco,taxaDeComicao))

    def listarEmpregados(self):
        return funcionarios

    def removerFuncionario(self,numero):
        for i in funcionarios:
            if i.getNumero() == numero:
                del(funcionarios[funcionarios.index(i)])
                break