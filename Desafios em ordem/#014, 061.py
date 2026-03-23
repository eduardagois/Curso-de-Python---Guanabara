print('{:=^40}'.format('GERADOR=DE=PA'))
num = int(input('Digite um número:'))
razao = int(input('Razão:'))
decimo = num + (10 - 1) * razao
n = 0
while n in range(num, decimo + razao, razao):
    print(n, end='->')
print('FIM')