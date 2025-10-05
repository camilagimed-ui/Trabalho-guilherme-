#peca numeros e vai somandoate o usuario digitar -1
# quando o usuario digitar -1 imprima o valor da soma de todos os numeros digitados

soma = 0
numero = int(input('digite um numero: '))   

while numero != -1:
    soma += numero
    numero = int(input('digite um numero: '))   

print('fim do calculo')
print(f'o valor da soma é: {soma}')