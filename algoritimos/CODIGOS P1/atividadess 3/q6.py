#Peça a idade e o valor de compra. Só aplique desconto se a idade for maior ou igual a 60
#  e o valor da compra maior que 100. Caso contrário, mostre "Sem desconto".

valor = float(input('digite o valor da compra: '))
idade = int(input('digite sua idade: '))

if idade >= 60 and valor > 100:
    desconto = valor * 0.10
    valorFinal = valor - desconto
    print(f'desconto aceito! o valor final ficou de {valorFinal}')
else:
    print('sem desconto')
