soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + c / c
print('A soma de todos os valores solicitados é {}'.format(soma))
print('E de 1 a 500, existem {:.0f} números ímpares que são múltiplos de 3'.format(cont))

