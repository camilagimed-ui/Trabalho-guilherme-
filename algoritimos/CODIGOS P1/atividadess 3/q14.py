#Peça a temperatura atual. Mostre "Atenção!" se a temperatura for menor que 10 ou maior que 35
# . Caso contrário, mostre "Temperatura normal".

temp = int(input('digite a temperatura atual: '))

if temp < 10 or temp > 35:
    print('atenção!!')
else:
    print('temperatura normal')
