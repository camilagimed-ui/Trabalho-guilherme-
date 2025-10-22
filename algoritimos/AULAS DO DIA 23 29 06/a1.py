# Vamos criar um sistema de terminal simulando uma calculadora
# Ela deve perguntar qual operação deseja realizar
# Quando números deve realizar a opção
# Pedir todos os números solicitados
# Realizar operação: somar, subtrair, multiplicar e dividir

# Exemplo de menu:
# Sistema CalcPython
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 0 - Sair
# Digite uma das opções abaixo:

while True:
    opcao = int(input('\nsistema calphynton \n\n1 -somar\n2 -subtrair\n3 -multiplicar\n4 -dividir\n0 -sair:   '  ))

    if(opcao == 0):
        break
    elif(opcao == 1):
        numeros = int(input('digite quntas vezes voce deseja somar: '))
        soma = 0
        for n in range(numeros):
            valor = float(input('digite o valor:'))
            soma += valor
        print(f'o valor da soma e {soma}')
    elif(opcao == 2):
        numeros = int(input('digite quantos numeros voce quer subtrair:'))
        subtrair = 0
        for n in range(numeros):
            valor = float(input('digite o valor: '))
            if(n == 0):
                subtrair = valor
            else:
                subtrair -= valor
    elif(opcao == 3):
        numeros = int(input('digite quantos '))                




    