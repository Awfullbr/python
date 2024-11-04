vc = float(input('Qual é o valor do barraco que você vai morar? R$ '))
s = float(input('Quanto você ganha seu fudido? R$ '))
a = int(input('Em quantos anos você pretende pagar está merda? '))
prestação = vc / (a * 12)
mínimo = s * 30 / 100
print('Para pagar uma casa de R$ {:.2f}'.format(vc, a), end=' ')
print('A prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser aceito')
else:
    print('Empréstimo negado!')
#NÃO ENTENDI PORRA NENHUMA
