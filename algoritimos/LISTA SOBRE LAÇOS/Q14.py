# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
# e a quantidade de números impares. 

pares = 0
impar = 0

for x in range(10):
    numero = int(input('digite um numero inteiro:'))
    if numero % 2 == 0:
        print(f'o numero {numero} e par')
        pares += 1
    else:
        print(f'o numero {numero} e impar')
        impar += 1


print(f'esxite {pares} numeros pares e {impar} numeros impares')