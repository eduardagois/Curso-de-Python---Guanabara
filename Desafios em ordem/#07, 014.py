t1 = float(input('Digite a temperatura em °C:'))
convert = str(input('Para qual temperatura você quer converter?')).strip().lower()
kel = (t1 + 273)
fah = (t1 * 1.8 + 32)

if convert == 'kelvin':
    print('A temperatura em Kelvin é {} ºF'.format(kel))
elif convert == 'fahrenheit':
    print('A temperatura em Fahrenheit é {} K'.format(fah))
else:
    print('Não foi possível converter')