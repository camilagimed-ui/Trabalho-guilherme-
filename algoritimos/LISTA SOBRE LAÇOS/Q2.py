#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite 
# a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
#  pedir as informações

nome = input('digite seu nome: ')
senha = input('digite sua senha: ')

while nome == senha:
    print('nome ou senha iguais! tente novamente!!')
    nome = input('digite seu nome: ')
    senha = input('digite sua senha: ')

print('Logado com sucesso!!')
