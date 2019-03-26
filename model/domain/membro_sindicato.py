
from model.domain.taxa_servico import TaxaServico
class MembroSindicato:
    def __init__(self,idMembro,taxaSindical):
        self.__idMembro = idMembro
        self.__taxaSindical = taxaSindical
        self.__taxaServico = []

    def getId(self):
        return self.__idMembro

    def getTaxaSindical(self):
        return self.__taxaSindical

    def lancarTaxaServico(self,data,valor):
        self.__taxaServico.append(TaxaServico(data,valor))
