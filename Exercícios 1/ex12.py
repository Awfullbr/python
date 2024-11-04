d = int(input('Quantos dias você alugou o carro? '))
km = int(input('Quantos kilometros você percorreu? '))
pago = (d*60) + (km*0.15)
print('Você me deve R${:.2f} pelo aluguel do veiculo.'.format(pago))