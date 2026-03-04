frase = str(input('Digite uma frase:')).strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('a') + frase.count('A')))
print('A letra A aparece na posição {} da frase'.format(frase.upper().find('A')+1))
print('A letra A apararece, por úlimo, na posição {} da frase'.format(frase.upper().rfind('A')+1))


