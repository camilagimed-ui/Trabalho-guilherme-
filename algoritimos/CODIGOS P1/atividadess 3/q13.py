#Solicite uma fruta. Mostre "Fruta favorita" se for "maçã" ou "banana"
# . Caso contrário, mostre "Fruta comum".

fruta = input('digite o nome de uma fruta: ')

if fruta == 'maçã' or fruta == 'banana':
    print('fruta favorita')
else:
    print('fruta comum')