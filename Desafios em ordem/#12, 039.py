from time import sleep
ano = int(input('Em que ano você nasceu?'))
idade = 2026 - ano
print('Você tem {} anos.'.format(idade))
print('Verificando...')
sleep(2)
if idade == 18:
    print('Você deve se alistar agora!')
elif idade > 18 and idade - 18 > 1:
    saldo = idade - 18
    print('O seu alistamento está atrasado em {} anos!'.format(saldo))
    print('Seu alistamento foi em {}'.format(2026 - saldo))
elif idade > 18 and idade - 18 == 1:
    saldo = idade - 18
    print('O seu alistamento está atrasado em {} ano!'.format(saldo))
elif idade < 18 and 18 - idade == 1:
    saldo = 18 - idade
    print('Ainda não está na hora de se alistar, falta {} ano!'.format(saldo))
    print('Será em {}'.format(2026 + saldo))
else:
    saldo = 18 - idade
    print('Ainda não está na hora de se alistar, faltam {} anos!'.format(saldo))
    print('Será em {}'.format(2026 + saldo))
