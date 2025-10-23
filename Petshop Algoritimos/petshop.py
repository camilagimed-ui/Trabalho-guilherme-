
'--------------------------------------------------PROJETO DO PETSHOP------------------------------------------------'

usuario = [] #[0] é o nome e [1] é a senha 
produtos = [['ração','$150.00'] ,['shampoo' , '$30.00'] , ['condicionador' , '$30.00'],['brinquedo' , '$20.00'] , ['coleira' , '$20.00'],['casinha','$80.00'] , ['caminha' ,'$100.00'] , ['caixa de trasnporte' , '$210.00'] , ['escova' , '$25.00'] , ['kit de perfume' , '$150.00']]
# [0] é o produto e o [1] é o valor
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
                possuiNome = 0
                for n in usuario:
                    if nome == n[0]:
                        print('Esse nome ja exite!!!Tente outro nome!!!')
                        possuiNome = 1
                        nome = input('nome: ')
                    
                if possuiNome == 0:
                    usuario.append([nome , senha , tipo , idade , nomePet])  
                    print(f'Parabens {nome}, voce foi cadastrado com sucesso!!')
                    break
    if opcao == 2:
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
            print(f'login efetuado com sucesso!!Bem vindo {nome}!!')

    elif tipo == 'cliente':
        print('escolha a opçao que deseja realizar!!!')

        while tipo == 'cliente':
            print('1 - realizar compra')
            print('2 - realizar agendamento')
            print('0 - sair')
            opcao = int(input('digite que opcao deseja realizar: '))
            if opcao == 0:
                break
            elif opcao == 1:
                valort = 0
                print('Realize sua compra agora mesmo: ')
                for p in range(len(produtos)):
                    print(f'Produto: {produtos[p][0]} | Valor: {produtos[p][1]}')

                quantidade = int(input('digite a quantidade de produtos que deseja comprar: '))

                for q in range(quantidade):
                    compra = float(input('digite o valor do produto que deseja levar:'))
                    valort = valort + compra
                
                print(f'o valor total da compra foi : {valort}')
                pagamento = float(input('insira quanto de dinheiro voce vai dar:'))
                if pagamento < 0:
                    print('valor invalido!!digite novamente!!!')
                    pagamento = float(input('insira quanto de dinheiro voce vai dar:'))

                elif pagamento < valort:
                    print('valor invalido!!! digite novamente!!')
                    pagamento = float(input('insira quanto de dinheiro voce vai dar:'))

                elif pagamento > valort:
                    print('valor invalido!!! digite novamente!!')
                    pagamento = float(input('insira quanto de dinheiro voce vai dar:'))
                else:
                    print('pagamento realizado com sucesso!!')
