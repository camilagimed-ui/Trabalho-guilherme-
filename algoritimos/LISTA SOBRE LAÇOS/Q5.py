 #Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
 #  iniciais. Valide a entrada e permita repetir a operação. 

Pa = int(input('digite a populaçaõ de Pa: '))
Pb = int(input(d='digite a população de Pb:'))
TaxaA = float(input('digite a taxa de crescimento de Pa: '))
TaxaB = float(input( 'digite a taxa de crescimento de Pb: '))
anos = 0

while Pa < Pb:
    Pa = Pa + Pa * TaxaA
    pb = Pb + Pb * TaxaB
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a do país B.")