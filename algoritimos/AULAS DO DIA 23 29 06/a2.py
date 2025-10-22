
email = input('digite seu email: ')

while "@" not in email:
    print('email invalido,digite novamente')
    email = input('digite seu email: ')

print('entrou no email!')