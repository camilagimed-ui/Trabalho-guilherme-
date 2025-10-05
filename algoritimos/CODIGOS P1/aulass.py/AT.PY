
precoProduto =  float(input('digite o valor'))
percentual = int(input('digite o desconto %:'))

valordodesconto = precoProduto * percentual / 100

print(f'preco do produto e {precoProduto}')
print(f'percentual do desconto e {percentual}')
print(f'valor do desconto e {valordodesconto}')
print(f'preco final do produto e {precoProduto - valordodesconto}')



