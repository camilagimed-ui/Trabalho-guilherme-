#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#  sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('digite o valor do produto: '))
p2 = float(input('digite o valor do produto: '))
p3 = float(input('digite o valor do produto: '))


if (p1 < p2 and p1 < p3):
    print(f'o {p1} e o ideal')
elif (p2 < p1 and p2 < p3):
    print(f'o {p2} e o ideal')
elif (p3 < p1 and p3 < p2):
    print(f'o {p3} e o ideal')
else:
    print('todos os produtos sao muito caros, va em outra loja')
