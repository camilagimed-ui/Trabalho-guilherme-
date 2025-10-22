'--------------------------------------------------PROJETO DO PETSHOP------------------------------------------------'

usuario = [] #[0] é o nome e [1] é a senha [2] é o tipo 

while True:
    print('Bem vindo ao Pet e Cia!!!')
    print('Escolha uma das opções abaixo: ')
    print('1 - Cadastro')
    print('2 - login')
    print('0 - Sair')

    opcao = int(input('digite uma opcao: '))

    if opcao == 0:
        break
    elif opcao != 1 and opcao != 2 and opcao != 0:
        print('digite uma opcao valida!!')

    elif opcao == 1:
        print('efetue seu cadastro!')
        nome = input('nome: ')
        senha = input('senha: ')
        senha2 = input('confirme sua senha: ')
        tipo = input('digite se voce é administrador ou cliente: ')
        idade = int(input('idade: '))
        nomePet = input('digite o nome do seu pet: ')

        while True:
            if tipo != 'administrador' and tipo != 'cliente':
                print('tipo invalido,digite o tipo novamente!!')
                tipo = input('digite se voce é administrador ou cliente: ')

            elif senha != senha2:
                print('tem certeza que digitou as duas senhas iguais? Tente novamente')
                senha = input('senha: ')
                senha2 = input('confirme sua senha: ')

            elif idade < 0 or idade > 110:
                print('idade invalida!!Digite novamente!!')
                idade = int(input('idade: '))

            else:
                for n in usuario:
                    if nome == n[0]:
                        print('Esse nome ja exite!!!Tente outro nome!!!')
                        nome = input('nome: ')
                    
                else:
                    usuario.append([nome , senha , tipo , idade , nomePet])  
                    print(f'Parabens {nome}, voce foi cadastrado com sucesso!!')
                    break
    elif opcao == 2:
        print('faça o seu login!!')
        nome = input('digite seu nome: ')
        senha = input('digite sua senha: ')
        logado = 0
        for i in usuario:
            if i[0] == nome and i[1] == senha:
                logado = 1

        if logado == 0:
            print('usuario nao encontrado!!!login invalido!!!')
        else:
            print('login efetuado com sucesso!!')
