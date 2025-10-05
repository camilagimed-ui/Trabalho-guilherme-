#Peça um número de 1 a 7 representando os dias da semana. Mostre "Fim de semana" 
# se o número for 6 ou 7. Caso contrário, mostre "Dia útil".

dia = int(input('digite um numero representando um dia da semana (segunda,terca,etc):'))

if dia == 6 or dia == 7:
    print('fim de semana')
else:
    print('dia util')
