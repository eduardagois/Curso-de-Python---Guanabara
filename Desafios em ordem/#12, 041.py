ano = int(input('Em que ano você nasceu?'))
idade = 2026 - ano
print('Você tem {} anos'.format(idade))

if idade < 9:
    print('A sua categoria é mirim ')
elif 9 < idade < 14:
    print('A sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print('A sua categoria é JÚNIOR')
elif idade == 20:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')
