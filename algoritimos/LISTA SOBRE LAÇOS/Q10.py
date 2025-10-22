#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
#  intervalo compreendido por eles. 

n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))

print(f"Números entre {n1} e {n2}:")

for i in range(n1 + 1, n2):
    print(i)
