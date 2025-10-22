
contador = int(input('digite o numero de notas que voce quer'))
auxiliar = contador
soma = 0

while contador > 0:
    nota = float(input('digite uma nota:'))
    print(f'nota {nota}')
    soma = soma + nota
    contador -= 1
    

print(f'o valor da soma e {soma}')
print(f'o valor da media e {soma / auxiliar}')