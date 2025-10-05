salario = float(input('digite seu salario: '))

salarioLiquido = salario
percentual = 0
valorDoAumento = 0


if(salario >0 and salario <= 280):
    percentual = 20
elif(salario > 280 and salario <= 700):
    percentual = 15
elif(salario > 700 and salario <= 1500):
    percentual = 10
elif(salario > 1500):
    percentual = 5
else:
    print('valor invalido')

valorDoAumento = salario * percentual / 100
salarioLiquido = salario + valorDoAumento

print(f'o salario e: {salario}') 
print(f'o percentual do aumento e: {percentual}')
print(f'e o novo salario apos o bruto e: {salarioLiquido}')
