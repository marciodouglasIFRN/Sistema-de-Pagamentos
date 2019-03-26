
class MenuAdmin:

    def __init__(self,admin):
        self.__admin = admin

    def printMenu(self):
        while True:
            op = self.__menuPrincipalAdmin()
            if op == 1:
                self.__cadastrarEmpregado()
            elif op == 2:
                self.__imprimirEmpregados()
            elif op == 3:
                self.__removerEmpregado()
            elif op == 4:
                self.__lancarTaxaDeServico()
            elif op == 5:
                break

    def __menuPrincipalAdmin(self):
        return int(input("Digite o número referente a opção desejada\n"
                         "1- Cadastrar empregado\n"
                         "2- Listar empregados\n"
                         "3- Rmover empregado\n"
                         "4- Sair\n"))


    def __cadastrarEmpregado(self):
        nome = input('Informe o nome do empregdo\n')
        endereco = input('Informe o endereco\n')
        tipo = int(input('Informe o tipo do empregado\n'
                         'Digite 1 para HORISTA\n'
                         'Digite 2 para ASSALARIADO\n'
                         'Digite 3 para COMICIONADO\n'))
        if tipo == 1:
            self.__cadastrarHorista(nome,endereco)
        if tipo == 2:
            self.__cadastrarAssalariado(nome,endereco)
        if tipo == 3:
            self.__cadastrarComicionado(nome,endereco)



    def __cadastrarHorista(self,nome,endereco):
        salario = int(input('Informe o salário por hora\n'))
        self.__admin.cadastrarEmpregadoHorista(nome, endereco, salario)



    def __cadastrarAssalariado(self,nome,endereco):
        salario = int(input('Informe o salário por mês\n'))
        self.__admin.cadastrarEmpregadoAssalariado(nome, endereco, salario)



    def __cadastrarComicionado(self,nome,endereco):
        salario = int(input('Informe o salário por mês\n'))
        taxa = int(input('Informe a porcentagem da comição\n'))
        self.__admin.cadastrarEmpregadoAssalariado(nome, endereco, salario, taxa)

    def __removerEmpregado(self):
        self.__imprimirEmpregados()
        numero = int(input('Escolha o número do empregado a ser removido\n'))
        self.__admin.removerFuncionario(numero)

    def __imprimirEmpregados(self):
        for i in self.__admin.listarEmpregados():
            print(i)

    def __lancarTaxaDeServico(self):
        valor = int(input('Informe o valor da taxa serviço\n'))
        id = int(input('Informe o id do membro\n'))
        self.__admin.lancarTaxaDeServico(id,valor)
