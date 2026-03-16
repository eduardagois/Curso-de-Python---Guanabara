num = int(input('Digite um número inteiro:'))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')

print('\n\033[m O número {} foi divísivel {} vezes!'.format(num, cont))
if cont == 2:
    print('Logo, o número {} é primo!'.format(num))
else:
    print('Logo, o número {} não é primo!'.format(num))
