from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
ordem = [n1, n2, n3, n4]
escolhido = choice(ordem)
print('O aluno escolhido foi {}'.format(escolhido))