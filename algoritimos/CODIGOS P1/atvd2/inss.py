
valorH = float(input('digite seu valor/hora: '))
quantidadeH = int(input('digite a quantidade de horas trabalhadas: '))

salarioBruto = valorH * quantidadeH
print(f'Seu salario bruto e: {salarioBruto}')

impostoderenda =  salarioBruto * 0.11
print(f' IR (11%) {impostoderenda}')

inss = salarioBruto * 0.08
print(f'o valor do INSS (8%) e:{inss}')

sindicato = salarioBruto * 0.05
print(f'sindicato (5%): {sindicato}')

salarioliquido = salarioBruto - impostoderenda - inss - sindicato
print(f'salario liquido: {salarioliquido}')



