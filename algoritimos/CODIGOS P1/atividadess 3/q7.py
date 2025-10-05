#Leia dois números. Mostre "Os dois são múltiplos de 5" se ambos forem divisíveis por 5.
#  Caso contrário, mostre "Não são múltiplos de 5".

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

if (n1 % 5 == 0) and (n2 % 5 == 0):
    print("Os dois são múltiplos de 5")
else:
    print("Não são múltiplos de 5")