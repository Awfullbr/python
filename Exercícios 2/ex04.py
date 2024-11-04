from datetime import date
da = int(input('Informe a data de nascimento: '))
anoatual = date.today().year
idade = anoatual - da
print('Quem nasceu em {} tem {} em {}.'.format(da, idade, anoatual))
if idade == 18:
    print('Você está na idade de alistamento obrigatorio.')
elif idade > 18:
    print('Você passou da idade de alistamento obrigatorio.')
else:
    print('Você é muito jovem para se alistar.')