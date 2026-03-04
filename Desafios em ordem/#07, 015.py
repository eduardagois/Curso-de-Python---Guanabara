km = float(input('Quantidade de Km percorrido:'))
dia = float(input('Por quantos dias?'))
resultado = (km * 0.15) + (dia * 60)

print('O valor a ser cobrado é {:.2f} R$'.format(resultado))
