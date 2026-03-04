valor = float(input('Digite o valor armazenado na sua carteira:'))
op = str(input('Qual moeda você quer comprar?')).strip().lower()
dolar = valor / 5.13
euro = valor / 6.06
if op == "dolar":
    print('Com {} R$,Você pode comprar {:.2f} US$'.format(valor, dolar))
elif op == "euro":
    print('Com {} R$,Você pode comprar {:.2f} EU$'.format(valor, euro))
else:
    print('Não foi possível converter')