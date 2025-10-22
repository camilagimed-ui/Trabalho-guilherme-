# Faça um programa que leia 5 números e informe a soma e a média dos números. 

soma = 0
for x in range(1,6):
    nota = float(input(f'digite sua {x}º nota: '))
    soma += nota
    
print(f'a media dessas 5 notas é : {soma / 5}')