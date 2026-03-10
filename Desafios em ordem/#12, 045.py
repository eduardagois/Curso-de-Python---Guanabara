import time
import random
print('--' * 6 + 'JOKENPÔ' + '--' * 6)
print('SERÁ QUE VOCÊ PODE ME VENCER?')
print('ESCOLHA A SUA JOGADA:')
jog = str(input('Pedra, papel ou tesoura:')).strip().capitalize()

escolha = ['Pedra', 'Papel', 'Tesoura']
jogc = random.choice(escolha)
time.sleep(1)
print('Sua jogada: {} \n Minha Jogada: {} \n'.format(jog, jogc))
print('PROCESSANDO...')
time.sleep(3)

#VITÓRIAS
if jog == 'Papel' and jogc == 'Pedra':
    print('PARABÉNS, VOCÊ VENCEU!')
elif jog == 'Pedra' and jogc == 'Tesoura':
    print('PARABÉNS, VOCÊ VENCEU!')
elif jog == 'Tesoura' and jogc == 'Papel':
    print('PARABÉNS, VOCÊ VENCEU!')
#DERROTAS
elif jog == 'Papel' and jogc == 'Tesoura':
    print('QUE PENINHA, VOCÊ PERDEU! XD \n SEJA MELHOR DA PRÓXIMA VEZ')
elif jog == 'Pedra' and jogc == 'Papel':
    print('QUE PENINHA, VOCÊ PERDEU! XD \n SEJA MELHOR DA PRÓXIMA VEZ')
elif jog == 'Tesoura' and jogc == 'Pedra':
    print('QUE PENINHA, VOCÊ PERDEU! XD \n SEJA MELHOR DA PRÓXIMA VEZ')
#EMPATES
elif jog == 'Papel' and jogc == 'Papel':
    print('PARECE QUE EMPATAMOS...')
elif jog == 'Pedra' and jogc == 'Pedra':
    print('PARECE QUE EMPATAMOS...')
elif jog == 'Tesoura' and jogc == 'Tesoura':
    print('PARECE QUE EMPATAMOS...')
else:
    print('ERRO, TENTE NOVAMENTE.')