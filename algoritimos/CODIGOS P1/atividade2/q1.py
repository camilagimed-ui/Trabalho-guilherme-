
tamanho = input('qual tamanho da pipoca voce prefere? digite (P/M/G)')
refri = input('a compra inclui refrigerante? (S/N)')

P = 5
M = 8
G = 10
refrigerante = 5 

if (tamanho == 'P' and refri == 'S'):
    valorP = P + refrigerante
    print(f'o valor sem o desconto e {valorP}')
    desconto = valorP * 0.10
    valorP = valorP - desconto
    print(f'o valor com desconto e {valorP}')
elif (tamanho == 'M' and refri == 'S'):
    valorM = M + refrigerante
    print(f'o valor sem o desconto e {valorM}')
    desconto2 = valorM * 0.10
    valorM = valorM - desconto2
    print(f'o valor com desconto e {valorM}')
elif (tamanho == 'G' and refri == 'S'):
    valorG = G + refrigerante
    print(f'o valor sem o desconto e {valorG}')
    desconto3 = valorG * 0.10
    valorG = valorG - desconto3
    print(f'o valor com desconto e {valorG}')
elif (tamanho == 'P' and refri == 'N'):
    print(f'o valor sem desconto e{P}')
elif (tamanho == 'M' and refri == 'N'):
    print(f'o valor sem desconto e{M}')
elif (tamanho == 'G' and refri == 'N'):
    print(f'o valor sem desconto e{G}')