print('{:=^40}'.format('DETECTOR DE PALÍNDROMO'))
frase = str(input('Digite uma frase:')).upper().strip()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
#inverso = juntas[::-1]
#Assim, tiraria o for e poderia deixar só as condições ;)
for letra in range(len(juntas) -1, -1, -1):
    inverso += juntas[letra]
print('O inverso de {} é {}'.format(juntas, inverso))
if juntas == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
