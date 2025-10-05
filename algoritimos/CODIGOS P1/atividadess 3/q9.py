#Solicite a cor escolhida pelo usuário. Se for "vermelho" ou "azul",
#  mostre "Cor permitida". Caso contrário, mostre "Cor não permitida".

cor = input('digite uma cor: ')

if cor == 'vermelho' or cor == 'azul':
    print('cor permitida')
else:
    print('cor nao permitida')
