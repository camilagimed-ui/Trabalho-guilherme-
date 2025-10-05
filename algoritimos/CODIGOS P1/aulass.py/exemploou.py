
clientVip = input('voce e cliente vip? (S/N)')
clienteNovo = input('voce e cliente novo? (S/N)')
compra = float(input('valor da compra: '))

if clientVip == 'S' or clienteNovo == 'S':
    compra = compra * 0.9

print(f'o total da compra foi: {compra}')