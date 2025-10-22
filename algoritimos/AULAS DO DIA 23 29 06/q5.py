#Escreva um algoritmo peça um número ao usuário e some somente os números que são menores 
# que 21 e maiores que 70. Continue pedindo até que ele digite -1.

numero = int(input('Digite um número: '))
soma = 0

while numero != -1:   
    if numero < 21 or numero > 70:   
        soma += numero
    numero = int(input('Digite um número: '))

print('Fim do cálculo')
print(f'O valor da soma é: {soma}')
