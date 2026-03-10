km = float(input('Qual a velocidade do carro?'))

if km > 80:
    print('Seu carro foi multado! e você pagará uma multa de {:.2f} R$!'.format((km - 80) * 7))
else:
    print('Tudo bem, pode seguir viagem.')
