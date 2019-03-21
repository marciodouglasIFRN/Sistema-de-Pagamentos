from model.persistencia.banco import funcionarios
from model.domain.admin import Admin
class Altenticacao:

    def altenticar(self,numero):
        if numero != 'adm' and len(funcionarios)>0:
            for f in funcionarios:
                if f.getNumero() == int(numero):
                    return f
                else:
                    return None
        elif numero == 'adm':
            return Admin()
        else:
            return None

