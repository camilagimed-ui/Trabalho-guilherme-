
quantidade = float(input('quantos litros deseja colocar? '))
preco = 6.50
valorT = quantidade * preco

if (quantidade >= 20):
    print(f'o valor sem desconto e de {valorT}')
    desconto = valorT - 5
    print(f'o valor com desconto e de {desconto}')
else:
    print(f'o valor sem desconto e de {valorT}')