km = int(input('A quantos km/h você estava? '))
if km > 80:
    print('Cê é o paul walker fdp? ')
    multa = (km-80) * 7
    print('Paga R${:.2f} noia'.format(multa))
else:
    print('Mete o pé devagar vagabundo')
