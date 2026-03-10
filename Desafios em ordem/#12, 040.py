n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

if media >= 7.0:
    print('Sua nota foi {:.2f}! \n APROVADO! :)'.format(media))
elif 5.0 < media < 7.0:
    print('Sua nota foi {:.2f}! \n RECUPERAÇÃO!'.format(media))
else:
    print('Sua nota foi {:.2f}! \n REPROVADO \n Que pena! :('.format(media))

