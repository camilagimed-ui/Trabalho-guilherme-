#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem 
# caso o valor seja inválido e continue pedindo até que o usuário 
# informe um valor válido
valor = int(input('digite um valor: '))

while valor > 10:
    print('valor invalido!')
    valor = int(input('digite um valor: '))

print('valor valido!')