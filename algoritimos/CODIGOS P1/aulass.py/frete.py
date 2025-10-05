
compra = float(input('digite o total da compra:'))
valordofrete = 60

if compra > 100:
    compra = compra - valordofrete
else:
    compra = compra + valordofrete

print(f'o valor total da compra + frete e :{compra}')