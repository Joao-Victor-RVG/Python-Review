#cotação do dia 31/03/2022

din = float(input('Quanto dinheiro você tem na carteira? R$:'))
dolar =  (din / 4.73)
libra =  (din / 6.22)
euro  =  (din / 5.24)
print(f'Você tem uma quantida equivalente à {dolar::.2f} dolares')
print(f'Você tem uma quantida equivalente à {libra:.2f} libras')
print(f'Você tem uma quantida equivalente à {euro:.2f}  euros')
