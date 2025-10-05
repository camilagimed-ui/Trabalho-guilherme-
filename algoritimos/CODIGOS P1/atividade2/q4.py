
idade = int(input('qual sua idade? '))

if (idade < 16):
    print('nao pode votar')
elif (idade >= 18 and idade < 70):
    print('voce e obrigado a votar')
elif (idade == 16 or idade == 17 or idade >= 70):
    print('o voto e facultativo')