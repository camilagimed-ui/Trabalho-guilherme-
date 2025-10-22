#. Faça um programa que leia 5 números e informe o maior número. 

maior = 0
for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    print(numero)
    if numero > maior:
        maior = numero
        

print(f'o maior numeor é {maior}')