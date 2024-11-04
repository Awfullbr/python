co = int(input('Qual é o comprimento do cateto oposto? '))
ca = int(input('Qual é o comprimento do caceto adjacente? '))
h = (co**2+ca**2) **(1/2)
print('A hipotenusa é {:.3f}'.format(h))