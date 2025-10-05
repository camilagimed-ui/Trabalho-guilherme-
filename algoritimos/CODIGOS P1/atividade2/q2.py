 
metrosG = float(input('quantos metros gean saltou? '))
metrosGu = float(input('quantos metros gustavo saltou? '))

if (metrosG > metrosGu):
    print(f'gean ganhou com um salto de {metrosG} metros')
elif(metrosGu > metrosG):
    print(f'gustavo ganhou com um salto de {metrosGu} metros')
else:
    print('ambos empataram')