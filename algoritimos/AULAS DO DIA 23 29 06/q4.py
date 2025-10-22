#Escreva um algoritmo que imprima todos os números ímpares até 100 diferentes de 7, 13, 21 e 51.

numero = 0

while numero <= 100:
    if numero % 2 != 0:
        if numero != 7 and numero != 13 and numero !=21 and numero != 51:
            print(numero)
    numero += 1