

numero1 = int(input('insira um numero: '))
numero2 = int(input('insira um numero: '))
numeromaior = 0 
if numero1 > numero2:
    print(f'o numero {numero1} e maior')
    numeromaior = numero1
else:
    print(f'o numero {numero2} e maior')
    numeromaior = numero2

if numeromaior > 0 or numeromaior == 0:
    print('o resultado e positivo ou neutro')
else:
    print('o resultado e negativo')

