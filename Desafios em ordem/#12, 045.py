import time
import random
print('--' * 6 + 'JOKENPÔ' + '--' * 6)
print('SERÁ QUE VOCÊ PODE ME VENCER?')
print('ESCOLHA A SUA JOGADA:')
jog = str(input('PEDRA, PAPEL OU TESOURA:')).strip().upper()

escolha = ['PEDRA', 'PAPEL', 'TESOURA']
jogc = random.choice(escolha)
print('SUA JOGADA: {} \n MINHA JOGADA: {} \n'.format(jog, jogc))
print('PROCESSANDO...')
time.sleep(3)

#VITÓRIAS
if jog == 'PAPEL' and jogc == 'PEDRA':
    print('PARABÉNS, VOCÊ VENCEU!')
elif jog == 'PEDRA' and jogc == 'TESOURA':
    print('PARABÉNS, VOCÊ VENCEU!')
elif jog == 'TESOURA' and jogc == 'PAPEL':
    print('PARABÉNS, VOCÊ VENCEU!')
#DERROTAS
elif jog == 'PAPEL' and jogc == 'TESOURA':
    print('QUE PENINHA, VOCÊ PERDEU! XD \n SEJA MELHOR DA PRÓXIMA VEZ')
elif jog == 'PEDRA' and jogc == 'PAPEL':
    print('QUE PENINHA, VOCÊ PERDEU! XD \n SEJA MELHOR DA PRÓXIMA VEZ')
elif jog == 'TESOURA' and jogc == 'PEDRA':
    print('QUE PENINHA, VOCÊ PERDEU! XD \n SEJA MELHOR DA PRÓXIMA VEZ')
#EMPATES
elif jog == 'PAPEL' and jogc == 'PAPEL':
    print('PARECE QUE EMPATAMOS...')
elif jog == 'PEDRA' and jogc == 'PEDRA':
    print('PARECE QUE EMPATAMOS...')
elif jog == 'TESOURA' and jogc == 'TESOURA':
    print('PARECE QUE EMPATAMOS...')
else:
    print('ERRO, TENTE NOVAMENTE.')