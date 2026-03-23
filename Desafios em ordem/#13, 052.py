print('{:=^40}'.format('VERIFICADOR DE NÚMEROS PRIMOS'))
cont = 0
num = int(input('Digite um número inteiro:'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m {}'.format(c), end=' ')
        cont += 1
    else:
        print('\033[m {}'.format(c), end=' ')

print('\n\033[mO número {} foi divisível \033[33m{}\033[m vezes'.format(num, cont))
if cont == 2:
    print('\033[mPor isso, ele é PRIMO!')
else:
    print('\033[mPor isso, não é PRIMO!')
print('{:=^40}'.format('FIM DO PROGRAMA'))
