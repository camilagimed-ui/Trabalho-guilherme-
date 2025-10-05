#Escreva um algoritmo que imprima todos os números pares entre 100 e 168.
#  (Um número é par quando: numero % 2 == 0)

n = 100

while n <= 168:
    if n % 2 == 0:
        print(f'o numero {n} e par')
    n += 1