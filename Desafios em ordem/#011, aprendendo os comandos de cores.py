#\033[style;text;backm

#STYLE: #0 none; 1 bold; 4 underline; 7 negative
#TEXT: 30-37; BACKGROUND: 40-47

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m' }

print('\033[7;30;45mOlá, Mundo!\033[m')

a = 5
b = 9
print('Os valores são \033[1;31m{}\033[m e \033[1;35m{}\033[m'.format(a,b))

nome = 'Duda'
print('Prazer em te conhecer, {} {}! {}'.format('\033[1;35m', nome, '\033[1;35m'))

nome = 'Góis'
print('Olá!, {} {}! {}'.format(cores['amarelo'], nome, cores['amarelo']))
