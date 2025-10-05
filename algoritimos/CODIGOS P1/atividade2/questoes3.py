
salario = float(input('insira o valor do seu salario'))
porcentagem= float(input('insira o valor da porcentagem do seu imposto de renda'))
print(f'seu salario e {salario} e sua porcentagem de imposto de renda e {porcentagem}%')
imposto = salario * (porcentagem / 100)
salarioLiquido = salario - imposto 
print(f'o salario liquido e {salarioLiquido}')
