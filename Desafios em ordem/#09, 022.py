nome = str(input('Digite o seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome)-nome.count(' '))

dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0],len(dividido [0])))

