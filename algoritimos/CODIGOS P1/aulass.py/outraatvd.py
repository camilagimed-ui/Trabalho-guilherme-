
n1 = int(input('esvreva um numero inteiro positivo: '))

if n1 > 0:
    if n1 > 50:
        n1 = n1 * 2
    else: 
        sub = n1 * 12 / 100
        n1 = n1 - sub

print(f'o valor do numero final e: {n1}')