#nova função
#o len conta quatos caracteres determinada palavra tem!!!

senha = input('digite sua senhra(minimo 8 caracteres)')
tamanho = len(senha)


while tamanho < 8 or '*' not in senha:
    print('senha com caracteres insuficientes ou n possui *...')
    senha = input('digite sua senhra(minimo 8 caracteres)')
    tamanho = len(senha)
    if tamanho >= 8 and '*' in senha:
        print('senha aceita')