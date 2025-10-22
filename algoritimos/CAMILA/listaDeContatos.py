contatos = []

while True:
    print('Bem vindo a lista de contatos')
    print('1 - cadastro de novo contato')
    print('2 - listar contatos')
    print('3 - alterar contato')
    print('4 - remover contato')
    print('0 - sair')
    opcao = input('digite a opção:')

    if opcao == '0':
        break
    elif opcao == '1':
        nome = input('digite o nome do contato: ')
        numero = int(input('digite o numero do celular: '))
        cidade = input('digite a cidade: ')
        contatos.append([nome,numero,cidade])
    elif opcao == '2':
        for c in contatos:
            print(f'Nome: {c[0]} | Numero: {c[1]} | Cidade: {c[2]}')
    elif opcao == '3':
        for indice in range(len(contatos)):
            print(f'Codigo: {indice}  | Nome:{contatos[indice][0]}')

        indice = int(input('digite o indice que deseja mudar: '))

        while indice < 0 or indice >= len(contatos):
            print('indice invalido!!!')
            indice = int(input('digite um indice valido: '))

        nome = input('digite o nome do contato: ')
        numero = int(input('digite o numero do celular: '))
        cidade = input('digite a cidade: ')
        NovoContato = [nome,numero,cidade]
        contatos[indice] = NovoContato
    elif opcao == '4':
        for indice in range(len(contatos)):
            print(f'Codigo: {indice} | Nome: `{contatos[indice][0]}')
            
        indice = int(input('digite o indice que deseja apagar: '))

        while indice < 0 or indice >= len(contatos):
            print('indice invalido!!!')
            indice = int(input('digite um indice valido para excluir: '))

        contatos.remove(contatos[indice])

    else:
        print('ERRO!!DIGITE UMA OPÇÃO VALIDA!!!')