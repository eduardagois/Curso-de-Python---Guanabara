from time import sleep
from random import randint
num = randint(1,5)
n_usu = int(input('Adivinhe o número que eu escolhi:'))
print('Processando...')
sleep(2)
if n_usu == num:
    print('Parabéns! {} é o número correto!'.format(num))
else:
    print('Errou! O número correto é {}!'.format(num))
