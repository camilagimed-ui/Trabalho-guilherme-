#Solicite a matrícula e a senha de um aluno. O login só será aceito se a matrícula for 
# "20231001" e a senha "algoritmo". Caso contrário, mostre

matricula = int(input('digite sua matricula: '))
senha = (input('digite sua senha: '))

if matricula == 20231001 and senha == 'algoritmo':
    print('login aceito')
else:
    print('dados incorretos')