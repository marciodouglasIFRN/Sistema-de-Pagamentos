
from view.altenticacao import Altenticacao
from view.menu_adm import MenuAdmin
from view.menu_horista import MenuHorista
from model.domain.admin import Admin
from model.domain.empregado_horista import EmpregadoHorista


while True:
    empregado = Altenticacao().altenticar(input('Para altenticar-se informe seu número de identificacao:\n'))
    if isinstance(empregado, Admin):
        MenuAdmin(empregado).printMenu()
    elif isinstance(empregado,EmpregadoHorista):
        MenuHorista(empregado).printMenu()
    else:
        print('Tente outra vez')