from domain.empregado_horista import EmpregadoHorista
from domain.empregado_assalariado import EmpregadoAssalariado
from persistencia.banco import funcionarios

class SistemaFolha:


    def __geraId(self):
        if funcionarios.__len__() > 0:
            return funcionarios[funcionarios.__len__()-1].getNumero()+1
        return 1
