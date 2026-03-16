num = int(input('Digite um número para ver sua tabuada:'))
print('{:=^40}'.format('TABUADA DO {}'.format(num)))
for c in range(1, 11):
    print('{:2} X {:2} == {:2}'.format(num, c, c * num))
print('{:=^40}'.format('FIM!'))
