#crie um algoritimo que some 3 numeros e 
# verifique se o resultado e positivo
#se sim, imprimir: ' o resultado e positivo'
# se nao, imprimir: 'o resultado e negativo ou neutro'

n1 = int(input('insira um numero:'))
n2 = int(input('insira um numero:'))
n3 = int(input('insira um numero:'))

soma = n1 + n2 + n3

if soma > 0:
    print('o resultado e positivo')
else:
    print('o resultado e negativo ou neutro')