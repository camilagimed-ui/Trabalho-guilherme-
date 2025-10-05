#Peça dois números inteiros. Mostre "Pelo menos um é negativo" se um ou os dois 
# forem menores que zero. Caso contrário, mostre "Nenhum negativo".

n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite um numero inteiro: '))

if n1 < 0 or n2 < 0:
    print('pelo menos um e negativo')
else:
    print('nenhum negativo')
