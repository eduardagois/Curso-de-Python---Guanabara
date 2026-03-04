n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

s = n1 + n2
m = n1 * n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma é {}, \n O produto é {}, \n A divisão é {:.3f}, \n A divisão inteira é {} \n e A exponenciação é {}'.format(s, m, d, di, e))