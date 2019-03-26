
from model.persistencia.banco import funcionarios

class SistemaFolha:

    def geraId(self):
        if funcionarios.__len__() > 0:
            return int(funcionarios[funcionarios.__len__()-1].getNumero()+1)
        return 1

