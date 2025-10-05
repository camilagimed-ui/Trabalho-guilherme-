#Peça ao usuário para informar a forma de pagamento. Mostre "Forma aceita" se for "dinheiro" ou "pix".
#  Caso contrário, mostre "Forma não aceita"

pag = input('insira sua forma de pagamento:')

if pag == 'dinheiro' or pag == 'pix':
    print('forma aceita')
else:
    print('forma nao aceita')