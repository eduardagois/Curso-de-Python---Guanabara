import math
ang = float(input('Digite um ângulo qualquer:'))
rad = math.radians(ang)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

print('O seno de {} é {:.2f} \n O cosseno é {:.2f} \n E a tangente é {:.2f}'.format(ang, s, c, t))

