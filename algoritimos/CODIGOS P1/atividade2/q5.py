
n = int(input('qual o total de participantes? '))
valor = 44


if (n >= 5):
    valorD = valor * 0.10
    valor = valor - valorD
    valor = valor * n
    print(f'o valor final fica {valor}')