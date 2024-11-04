a = float(input('Qual foi a sua primeira nota ? '))
b = float(input('Quanl foi a sua segunda nota? '))
m = (a+b) / 2
if m >= 7.0:
    print('Você passou pois sua média é {:.1f}'.format(m))
elif 7 > m >= 5:
    print('Você está em recuperação pois sua média foi {:.1f}'.format(m))
elif m < 5:
    print('Você foi reprovado pois sua média foi {:.1f}'.format(m))