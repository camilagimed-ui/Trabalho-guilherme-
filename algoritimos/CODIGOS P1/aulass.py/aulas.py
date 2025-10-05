
qunatidade = int(input('digite a quantidade do time: '))
ingresso = 44
valortotal = qunatidade * ingresso

if (qunatidade >= 5):
   deconto = valortotal * 0.10
   valortotal = valortotal - deconto

print(f'o valor total e de {valortotal}')