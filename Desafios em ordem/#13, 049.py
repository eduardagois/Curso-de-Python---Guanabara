num = int(input('Digite um número para ver sua tabuada:'))

print('-' * 12)
for c in range(1,11):
    print('{} X {:2} = {}'.format(num, c, num * c))
print('-' * 12)
