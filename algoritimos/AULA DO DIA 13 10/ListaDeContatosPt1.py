
contatos = []

while True:
    print('Bem vindo a lista de contatos')
    print('1 - cadastro de novo contato')
    print('2 - listar contatos')
    print('3 - alterar contato')
    print('4 - remover contato')
    print('0 - sair')
    opcao = input('digite a opção:')
    if(opcao == '0'):
        break
    elif(opcao == '1'):
        nome = input('digite o nome do contato:')
        celular = input('digite seu celular:')
        cidade = input('digite sua cidade:')
        contatos.append([nome , celular , cidade])
    elif(opcao == '2'):
        for c in contatos:
            print(f'nome: {c[0]} | celular: {c[1]} | cidade: {c[2]}')
    elif(opcao == "3"):
        for indice in range(len(contatos)):
            print(f'Código {indice} - Nome {contatos[indice][0]}')

        indice = int(input('Digite o indice que deseja alterar: '))
        while indice < 0 or indice >= len(contatos):
            print('Inválido')
            indice = int(input('Digite o indice que deseja alterar: '))

        nome = input("Digite o novo nome do contato: ")
        celular = input('Digite o novo seu celular: ')
        cidade = input('Digite a nova cidade: ')
        novaSublista = [nome, celular, cidade]
        contatos[indice] = novaSublista
    elif(opcao == "4"):
        for indice in range(len(contatos)):
            print(f'Código {indice} - Nome {contatos[indice][0]}')

        indice = int(input('Digite o indice que deseja remover: '))
        while indice < 0 or indice >= len(contatos):
            print('Inválido')
            indice = int(input('Digite o indice que deseja remover: '))

        contatos.remove(contatos[indice])
    else:
        print('Erro, escolha uma opção correta')