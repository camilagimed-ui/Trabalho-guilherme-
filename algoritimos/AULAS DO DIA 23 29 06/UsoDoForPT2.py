
#x = tuple(range(100))
#print(x)

#for x in range(10):
    #print('loop 10x')


#numero = int(input('digite um numero:'))

#for x in range(numero):
    #print(x + 1)

#quantas notas ele quer digitar
#somar e fazer a media 

notas = int(input('digite n notas: '))
soma = 0

for n in range(notas):
    nota = float(input('digite a nota:'))
    soma += nota

print(f'o valor da soma e de {soma} e a media e {soma / notas}')