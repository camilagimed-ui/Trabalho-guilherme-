#3. Faça um programa que leia e valide as seguintes informações: 
#a. Nome: maior que 3 caracteres; 
#b. Idade: entre 0 e 150; 
#c. Salário: maior que zero; 
#d. Sexo: 'f' ou 'm'; 
#e. Estado Civil: 's', 'c', 'v', 'd'; 

while True:
    nome = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    salario = float(input('digite seu salario: '))
    sexo = input('digite seu sexo (F/M): ')
    ec = input('digite seu estado civil (s/c/v/d): ')

    if len(nome) < 3:
        print('nome com menos de 3 caracteres, digite outro nome!!')
    elif idade < 0 or idade > 150:
        print('idade inválida! Digite entre 0 e 150.')
    elif salario <= 0:
        print('salario menor ou igual a 0, digite outro salario!!')
    elif sexo != 'F' and sexo != 'M':
        print('sexo inválido! Digite F ou M.')
    elif ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
        print('estado civil inválido! Digite s, c, v ou d.')
    else:
        break  


print(f'seu nome é: {nome}')
print(f'sua idade é: {idade}')
print(f'seu salário é: {salario}')
print(f'seu sexo é: {sexo}')
print(f'seu estado civil é: {ec}')
