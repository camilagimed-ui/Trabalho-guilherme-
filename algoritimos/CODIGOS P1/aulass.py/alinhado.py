
compra = float(input('Digite o valor da compra: '))
estado = input('Digite a sigla do seu estado: ')

if estado == 'PB':
    if compra > 500:
        cpf = input('Digite seu CPF: ')
    else:
        print('Não precisa de CPF.')

if estado == 'RN':
    if compra > 700:
        cpf = input('Digite seu CPF: ')
    else:
        print('Não precisa de CPF.')
