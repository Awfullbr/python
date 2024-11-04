from datetime import date
nas = int(input('Em que ano você nasceu? '))
ano = date.today().year
i = ano - nas 
if i <= 9:
    print('Você nasceu em {}, logo sua idade é {}, então está na categoria: Mirim.'.format(nas, i))
elif i <= 14:
    print('Você nasceu em {}, logo sua idade é {}, então sua categoria será: Infantil.'.format(nas, i))
elif i <= 19:
    print('Você nasceu em {}, logo sua idade é {}, então sua categoria será: Jûnior.'.format(nas, i))
elif i <= 25:
    print('Você nasceu em {}, logo sua idade é {}, então sua categoria será: Sênior.'.format(nas, i))
elif i <= 26:
    print('Você nasceu em {}, logo sua idade é {}, então sua categoria será: Master.'.format(nas, i))