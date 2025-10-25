
usuario = [] #[0] é o nome e [1] é a senha 
produtos = [['ração','$150'] ,['shampoo' , '$30'] , ['condicionador' , '$30'],['brinquedo' , '$20'] , ['coleira' , '$20'],['casinha','$80'] , ['caminha' ,'$100'] , ['caixa de trasnporte' , '$210'] , ['escova' , '$25'] , ['kit de perfume' , '$150']]
# [0] é o produto e o [1] é o valor
HorariosD = ['10h' , '12h' , '14h' , '16h' , '18h' ]
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
atendimentoP = [['banho', '$70'] , ['tosa' , '$40'] , ['banho e tosa' ,'$100'] , ['consulta' , '$120']]
avalicao = []
valort = 0
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

            if  tipo == 'cliente':
                print('escolha a opçao que deseja realizar!!!')

                while tipo == 'cliente':
                    print('1 - realizar compra')
                    print('2 - realizar agendamento')
                    print('3 - atendimento ao pet')
                    print('4 - avaliação do produto ou do atendimento')
                    print('0 - sair')
                    opcao = int(input('digite que opcao deseja realizar: '))
                    if opcao == 0:
                        break
                    elif opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
                        print('opcao invalida digite novamente')
                        opcao = int(input('digite que opcao deseja realizar: '))
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
                        while pagamento < 0 or pagamento < valort:
                            print('valor invalido!!digite novamente!!!')
                            pagamento = float(input('insira quanto de dinheiro voce vai dar:'))

                        if pagamento > valort:
                            troco = pagamento - valort
                            print(f'Compra concluida com sucesso!! seu troco é: {troco}')
                        else:
                            print('pagamento realizado com sucesso!!')

                    elif opcao == 2:
                        print('realize o seu agendamento')

                        for h in range(len(HorariosD)):
                            print(f'horarios disponivies {HorariosD[h]}')

                        while True:
                            horario = input('digite qual horario deseja escolher: ')
                            if horario not in HorariosD:
                                print('horario invalido!!! digite novamente')
                                horario = input('digite qual horario deseja escolher: ')

                            if horario == '10h':
                                if contador1 < 3:
                                    contador1 += 1
                                    print('horario marcado com sucesso!!')
                                    break
                                else:
                                    print('esse horaio esta cheio!!')
                            

                            if horario == '12h':
                                if contador2 < 3:
                                    contador2 += 1
                                    print('horario marcado com sucesso!!')
                                    break 
                                else:
                                    print('horario cheio!!')
                            
                            if horario == '14h':
                                if contador3 < 3:
                                    contador3 += 1
                                    print('horario marcado com sucesso!!')
                                    break
                                else:
                                    print('horario cheio!!')
                                
                            if horario == '16h':
                                if contador4 < 3:
                                    contador4 += 1
                                    print('horario marcado com sucesso!!')
                                    break
                                else:
                                    print('horaio cheio!!!')
                                
                            if horario == '18h':
                                if contador5 < 3:
                                    contador5 += 1
                                    print('horaio marcado com sucesso!!')
                                    break
                                else:
                                    print('horario cheio!!')
                    elif opcao == 3:
                        
                        print('Bem vindo ao atendimento ao pet!!! \n escolha o que deseja!')
                        for a in range(len(atendimentoP)):
                            print(f'Atendimento: {atendimentoP[a][0]} | Valor {atendimentoP[a][1]}')

                        quantidadeAtd = int(input('digite quantos atendimentos voce deseja realizar no seu pet: '))

                        for i in range(quantidadeAtd):
                            
                            print('digite o valor do atendimento que deseja realizar: ')
                            compra = float(input('digite o valor do produto que deseja levar:'))
                            valort += compra

                        print(f'o valor total da sua compra foi de {valort}')

                        pagamentoA = float(input('digite a quantia que voce vai dar: '))

                        while pagamentoA < 0 or pagamentoA < valort:
                            print('valor invalido!Digite novamente!!')
                            pagamentoA =  float(input('digite a quantia que voce vai dar: '))

                            if pagamentoA > valort:
                                trocoA = pagamentoA - valort
                                print(f'compra concluida com sucesso!! seu troco foi de {trocoA}')
                            else:
                                print('pagamento realizado com sucesso!!')
                    elif opcao == 4:
                        print('deixe sua avaliação e no que seria possivel a gente melhorar!')
                        Av = input('deixe sua a avaliação aqui: ')
                        avalicao.append(Av)
                        print(avalicao)
                        print('avaliação enviada com sucesso!')


            if tipo == 'administrador':
                print('olá,bem vindo a parte da administração do pet e cia!')
