from math import factorial
cont = 0
num = int(input('Digite um número para calcular seu fatorial:'))
print('Calculando {}!:'.format(num))
while num != 1:
    num -=1
    print('{} X {} X'.format(num, num-1))
print('fim')