from random import randint
cont = 0
num = randint(1, 10)
n_usu = int(input('TENTE ADIVINHAR O NÚMERO QUE EU ESCOLHI! \nDICA --> ESTÁ ENTRE 0 A 10:'))
#OBS: Dá pra colocar uma variável == False, depois se num == n_usu a variável == True!
while n_usu != num:
    if n_usu < num:
        n_usu = int(input('MAIOR... TENTE NOVAMENTE:'))
    else:
        n_usu = int(input('MENOR... TENTE NOVAMENTE:'))
    cont += 1
print('VOCÊ ACERTOU EM {} TENTATIVA(S) QUE O NÚMERO CORRETO É {}!'.format(cont+1,num))
