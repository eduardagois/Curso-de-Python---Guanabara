preco = float(input('Digite o valor do produto:'))
forma = str(input('Escolha a forma de pagamento: \n À Vista; À vista no cartão; Até 2x sem Juros ou 3x ou mais com juros.')).upper().strip()

if forma in 'À VISTA':
    print('Pagando à vista você ganha 10% de desconto, passando a pagar {:.2f} R$'.format(preco * 0.9))
elif forma in 'À VISTA NO CARTÃO':
    print('Pagando à vista no cartão você recebe 5% de desconto, passando a pagar {:.2f} R$ no produto.'.format(preco * 0.95))
elif forma in '2X NO CARTAO':
    print('Pagando em até 2x no cartão, você paga o preço normal, sem juros.')
elif forma in '3X OU MAIS NO CARTÃO':
    print('Pagando em 3x ou mais no cartão, você terá que pagar 20% de juros, passando a pagar {:.2f} no produto.'.format(preco * 1.2))
else:
    print('ERRO! TENTE NOVAMENTE')
