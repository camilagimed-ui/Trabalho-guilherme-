#senha no minimo 8 no maximo 16 e tem que ter *




senha = input('digite sua senhra(minimo 8 caracteres no maximo 16)')
tamanho = len(senha)


while tamanho < 8 or tamanho > 16 or "*" not in senha:
    print('senha com caracteres insuficientes ou n possui *...')
    senha = input('digite sua senhra(minimo 8 caracteres no maximo 16)')
    tamanho = len(senha)
    if tamanho >= 8 or tamanho <= 16  and '*' in senha:
        print('senha aceita')

