from datetime import date
ano = int(input('Em que ano você nasceu?'))
atual = date.today().year
idade = atual - ano
print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('A sua categoria é mirim ')
elif idade <= 14:
    print('A sua categoria é INFANTIL')
elif idade <= 19:
    print('A sua categoria é JÚNIOR')
elif idade <= 25:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')
