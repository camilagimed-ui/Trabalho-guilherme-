#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de 
# qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
#  tabuada. A saída deve 
#ser conforme o exemplo abaixo: 

while True:
    n = int(input('digite um numero entre 1 e 10: '))
    if n > 10 or n == 0:
        print('numero invalido! digite outro numero!')
    else:
        print(f'a tabuada do numero {n} é:')
        
    for x in range(1,11):
        print(f' {n} x {x} é:\n{n * x}')