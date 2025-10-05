#se a media for maior ou igual a 7 imprimir:aprovado
#se a media for menor igual a 6.9 imprimir:reprovado

print('insira as quatro notas dos alunos')
notaUm = int(input('qual foi a primeira nota?'))
notaDois = int(input('qual foi a segunda nota?'))
notaTres = int(input('qual foi a terceira nota?'))
notaQuatro = int(input('qual foi a quarta nota?'))

media = (notaUm + notaDois + notaTres + notaQuatro) / 4

if media >= 7:
   print('aprovado')

if media <= 6.9:
   print('reprovado')