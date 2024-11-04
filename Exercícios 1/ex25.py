from random import randint
cp = randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar valendo 20tão')
print('-=-'*20)
jogador = int(input('Em qual nùmero eu pensei? '))
if jogador == cp:
    print('Xitado até eu!')
else:
    print('Passa a grana noia')