
media = float(input('digite sua media: '))
faltas = int(input('digite o numero de faltas: '))

if(media >= 7 and faltas < 10):
    print('aprovado')
else:
    print('reprovado')