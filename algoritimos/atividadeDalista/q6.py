
#6. Faça um Programa que leia três números e mostre o maior deles.



n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if (n1 > n2 and n1 > n3):
    print(f'numero {n1} e o maior')
elif (n2 > n1 and n2 > n3):
    print(f'numero {n2} e o maior')
elif (n3 > n1 and n3 > n2):
    print(f'numero {n3} e o maior')