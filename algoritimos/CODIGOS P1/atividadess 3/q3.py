#Leia a temperatura e a umidade. Mostre "Clima agradável" se a temperatura estiver abaixo de 30 e
#  a umidade abaixo de 70. Caso contrário, mostre "Clima desconfortável".

temp = float(input('digite a temeperatura do local: '))
umidade = float(input('digite a umidade do local: '))

if temp < 30 and umidade < 70:
    print('clima agradavel')
else:
    print('clima desconfortavel')
