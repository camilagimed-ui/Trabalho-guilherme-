#Peça a idade de uma pessoa. Mostre "Entrada gratuita" se a idade for menor que 12 ou maior
#  que 60. Caso contrário, mostre "Entrada paga".

idade = int(input('insira sua idade: '))

if idade < 12 or idade > 60:
    print('entrada gratuita')
else:
    print('entrada paga')
