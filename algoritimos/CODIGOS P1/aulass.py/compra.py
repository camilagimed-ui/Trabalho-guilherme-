
compra = float(input('digite o total da compra:'))
cupomDesconto = 15

if compra >= 100:
    desconto = compra * cupomDesconto / 100 
    compra = compra - desconto 

print(f'o preco total da compra foi: {compra}')