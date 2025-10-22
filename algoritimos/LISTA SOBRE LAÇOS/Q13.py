#13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
#  número elevado ao segundo número.
#  Não utilize a função de potência da linguagem

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

n1 = base
for i in range(expoente - 1):
    n1 *= base

print(f'O número {base} elevado a {expoente} é: {n1}')
