#senha precisa conter *

senha = input('digite uma senha:')

while "*" not in senha:
    print('senha invalida')
    senha = input('digite uma senha:')

print('senha correta')

