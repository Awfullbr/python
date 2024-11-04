d = float(input('Qual é a distância de sua viagem? '))
if d <=200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
