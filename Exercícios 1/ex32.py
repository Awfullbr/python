s = int(input('Qual é o seu salário? '))
if s > 1250:
    a = s * 0.10
    print('Seu salário é superior a R$1250, logo seu aumento será de R${:.2f}'.format(a))
else:
    b = s * 0.15
    print('Seu salário é inferiro a R$1250, logo seu aumento será de R${:.2f}'.format(b))
