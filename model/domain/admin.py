from model.domain.empregado_horista import EmpregadoHorista
from model.domain.empregado_assalariado import EmpregadoAssalariado
from model.persistencia.banco import funcionarios
from model.domain.sistema_folha import SistemaFolha
from model.domain.sindicato import Sindicato
from datetime import datetime

class Admin:
    def __init__(self):
        self.sistema = SistemaFolha()
        self.sindicato = Sindicato()

    def cadastrarEmpregadoHorista(self,nome,endereco,salarioPorHora):
        funcionarios.append(EmpregadoHorista(self.sistema.geraId(),salarioPorHora,nome,endereco))

    def cadastrarEmpregadoAssalariado(self, nome, endereco, salarioMensal,taxaDeComicao=None):
        funcionarios.append(EmpregadoAssalariado(self.sistema.geraId(),salarioMensal, nome, endereco,taxaDeComicao))

    def listarEmpregados(self):
        return funcionarios

    def removerFuncionario(self,numero):
        for i in funcionarios:
            if i.getNumero() == numero:
                del(funcionarios[funcionarios.index(i)])
                break

    def lancarTaxaDeServico(self,id,valor):
        for i in self.sindicato.getMembros():
            if id == i.getId():
                i.lancarTaxaServico(datetime.now(),valor)
                break

