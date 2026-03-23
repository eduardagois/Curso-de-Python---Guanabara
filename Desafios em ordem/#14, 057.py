sexo = str(input('Digite o sexo de uma pessoa: [M/F]')).upper().strip()[0]
while sexo not in ['M', 'F']:
    str(input('Sexo INVÁLIDO. Tente novamente:')).upper().strip()[0]
if sexo == 'M':
    print('O sexo da pessoa é MASCULINO')
else:
    print('O sexo da pessoa é FEMININO')
