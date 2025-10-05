#Peça dois números inteiros. Mostre "Ambos pares" se os dois forem pares.
#  Caso contrário, mostre "Não são ambos pares".

n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))

if (n1 % 2 == 0 ) and (n2 % 2 == 0 ):
    print('ambos sao pares')
else:
    print('pelo menos um e impar')

