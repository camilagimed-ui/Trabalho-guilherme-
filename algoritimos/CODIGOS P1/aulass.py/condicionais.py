
anoNasc = int(input('digite seu ano de nascimento: '))
acompanhada = input('voce esta acompanhada? (S/N): ')

idade = 2025 - anoNasc

if(idade >= 18 or acompanhada == 'S'):
    print('voce pode entrar na festa')
else:
    print('voce nao pode entrar na festa!!!')