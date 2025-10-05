#7. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input('digite um numero: '))
n2 = float(input('digite um numero: '))
n3 = float(input('digite um numero: '))

if (n1 > n2 and n1 > n3):
    print(f'o {n1} e o maior')
elif (n2 > n1 and n2 > n3):
    print(f'o {n2} e o maior')
elif (n3 > n1 and n3 > n2):
    print(f'o {n3} e o maior')
 

if (n1 < n2 and n1 < n3):
    print(f'O {n1} é o menor')
elif (n2 < n1 and n2 < n3):
    print(f'O {n2} é o menor')
elif (n3 < n1 and n3 < n2):
    print(f'O {n3} é o menor')