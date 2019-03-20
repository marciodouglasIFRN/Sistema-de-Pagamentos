from domain.sistema_folha import SistemaFolha
sf = SistemaFolha()
while True:
    op = int(input("Escolha uma opção\n"
                   "1- Cadastrar empregado\n"
                   "2- Listar empregados\n"))
    if op == 1:
        nome = input('Informe o nome do empregdo\n')
        endereco = input('Informe o endereco\n')
        tipo = int(input('Informe o tipo do empregado\n'
                     'Digite 1 para HORISTA\n'
                     'Digite 2 para ASSALARIADO\n'
                     'Digite 3 para COMICIONADO\n'))
        if tipo == 1:
            salario = int(input('Informe o salário por hora\n'))
            sf.cadastrarEmpregadoHorista(nome,endereco,salario,'pt')
        if tipo == 2:
            salario = int(input('Informe o salário por mês\n'))
            sf.cadastrarEmpregadoAssalariado(nome,endereco,salario)
        if tipo == 3:
            salario = int(input('Informe o salário por mês\n'))
            taxa = int(input('Informe a porcentagem da comição'))
            sf.cadastrarEmpregadoAssalariado(nome,endereco,salario,taxa)
    elif op == 2:
        for i in sf.listarEmpregados():
            print(i)
    elif op == 3:
        print('3')
