
#Leia dois números e verifique se ambos são maiores que 100. Caso sejam, mostre "Números grandes". 
# Senão, mostre "Pelo menos um não é grande".

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

if n1 > 100 and n2 > 100:
    print('numeros grandes')
else:
    print('pelo menos um nao e grande')