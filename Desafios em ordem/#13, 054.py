from datetime import date
atual = date.today().year
contma = 0
contme = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a pessoa {}º nasceu?'.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        contma += 1
    else:
        contme += 1
print('Ao todo, tivemos {} pessoas maiores de idade.'.format(contma))
print('E também, tivemos {} pessoas menores de idade.'.format(contme))
