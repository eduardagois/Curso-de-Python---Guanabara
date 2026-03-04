dist = float(input('Qual a distância da viagem em Km?'))

if dist <= 200:
    print('O preço da passagem é {} R$'.format(dist * 0.5))
else:
    print('O preço da passagem é {} R$'.format(dist * 0.45))