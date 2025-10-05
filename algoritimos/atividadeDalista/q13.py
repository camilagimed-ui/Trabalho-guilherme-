#13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
#  (1-Domingo, 2- Segunda, etc.), se digitar
#outro valor deve aparecer valor inválido.

n = int(input('isira um numero referente ao dia da semana (1-Domingo, 2- Segunda, etc.): '))

if (n == 1):
    print('domingo')
elif (n == 2):
    print('segunda')
elif (n == 3):
    print('terca')
elif (n == 4):
    print('quarta')
elif (n == 5):
    print('quinta')
elif (n == 6):
    print('sexta')
elif (n == 7):
    print('sabado')
else:
    print('valor invalido')
