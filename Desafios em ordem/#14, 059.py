from time import sleep
print('{:=^30}'.format('CALCULADORA'))
n1 = int(input('DIGITE UM VALOR:'))
n2 = int(input('DIGITE OUTRO VALOR:'))
escolha = ''

while escolha != 5:
    print('=-=' * 10)
    escolha = int(input('''ESCOLHA:
    [1] SOMA
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA \n >>>>> '''))
    if escolha == 1:
        print('A SOMA DOS VALORES {} E {} É: \n {}'.format(n1, n2, n1+n2))
    elif escolha == 2:
        print('A MULTIPLICAÇÃO DE {} E {} RESULTA EM {} : \n'.format(n1, n2, n1*n2))
    elif escolha == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}!'.format(n1, n2))
        elif n1 == n2:
            print('O número {} é igual ao número {}!'.format(n1, n2))
        else:
            print('O número {} é maior que o número {}!'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('DIGITE UM NÚMERO:'))
        n2 = int(input('DIGITE OUTRO NÚMERO:'))
    elif escolha == 5:
        print('FINALIZANDO...')
        sleep(1)
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE:')
    print('=-=' * 10)
print('PROGRAMA ENCERRADO.')
