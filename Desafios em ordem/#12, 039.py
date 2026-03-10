from time import sleep
ano = int(input('Em que ano você nasceu?'))
idade = 2026 - ano
print('Você tem {} anos.'.format(idade))
print('Verificando...')
sleep(2)
if idade == 18:
    print('Você deve se alistar agora!')
elif idade > 18 and idade - 18 > 1:
    print('O seu alistamento está atrasado em {} anos!'.format(idade - 18))
elif idade > 18 and idade - 18 == 1:
    print('O seu alistamento está atrasado em {} ano!'.format(idade - 18))
elif idade < 18 and 18 - idade == 1:
    print('Ainda não está na hora de se alistar, falta {} ano!'.format(18 - idade))
else:
    print('Ainda não está na hora de se alistar, faltam {} anos!'.format(18 - idade))
