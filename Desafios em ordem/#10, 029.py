km = float(input('Qual a velocidade do carro?'))

if km > 80:
    print('Seu carro foi multado! e você pagará {} de multa!'.format((km - 80) * 7))
else:
    print('Tudo bem, pode seguir viagem.')
