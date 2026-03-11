num = int(input('Digite um número inteiro:'))
print('Escolha uma das bases de conversão:')
print('''[1] BINÁRIO 
[2] OCTAL 
[3] HEXADECIMAL''')
escolha = int(input('Sua escolha:'))

if escolha == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('ERRO. TENTE NOVAMENTE')
