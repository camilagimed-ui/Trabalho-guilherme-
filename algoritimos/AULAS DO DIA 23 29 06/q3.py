#Escreva um algoritmo que imprima todos os números pares entre 100 e 168.
#  (Um número é par quando: numero % 2 == 0)

contador = 100

while contador <= 168:   
    if contador % 2 == 0:
        print(contador)
    contador += 1