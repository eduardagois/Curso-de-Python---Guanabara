print('{:=^40}'.format('10 TERMOS DE UMA PA'))
n1 = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = n1 + (10 - 1) * razao
for c in range(n1, decimo + razao, razao):
    print(c, end=' -> ')
print('FIM')
