
peso = float(input('digite o valor do peso dos peixes:'))

execesso = peso - 50
multa = execesso * 4

print(f'o peso e: {peso}') 

if execesso > 50:
    print(f'o execesso e : {execesso}')
    print(f'o valor da multa e: {multa}') 


