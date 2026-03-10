r1 = float(input('Digite a medida da primeira reta:'))
r2 = float(input('Digite a medida da segunda reta:'))
r3 = float(input('Digite a media da terceira reta:'))

if r1 < r3 + r2 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é equilátero')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('O triângulo é isóceles.')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é possível formar um triângulo')
