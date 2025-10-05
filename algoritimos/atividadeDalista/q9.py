#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('digite um numero: '))
n2 = float(input('digite um numero: '))
n3 = float(input('digite um numero: '))

if n1 >= n2 and n2 >= n3:
    print(n1, n2, n3)
elif n1 >= n3 and n3 >= n2:
    print(n1, n3, n2)
elif n2 >= n1 and n1 >= n3:
    print(n2, n1, n3)
elif n2 >= n3 and n3 >= n1:
    print(n2, n3, n1)
elif n3 >= n1 and n1 >= n2:
    print(n3, n1, n2)
else:
    print(n3, n2, n1)