#Leia o nome de um time. Mostre "Esse time é famoso" se o nome for "Flamengo" ou "Corinthians"
# . Caso contrário, mostre "Time comum".

time = input('digite o nome de um time:')

if time == 'flamengo' or time == 'corinthians':
    print('esse time e famoso')
else:
    print('esse time e comum')
