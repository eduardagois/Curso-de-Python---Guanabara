print('{:=^40}'.format('MERCADO'))

preco = float(input('Digite o valor do produto:'))
print('''''Escolha a forma de pagamento: 
[1] À Vista (Dinheiro/Cheque)
[2] À vista no cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão''''')
forma = int(input('Qual é a opção?'))

if forma == 1:
    print('Você recebe um desconto de 10%, passando a pagar R$ {}'.format(preco * 0.9))
elif forma == 2:
    print('Você recebe um desconto de 5%, passando a pagar R$ {}'.format(preco * 0.95))
elif forma == 3:
    parcela == 2:
        print('Você pagará  R$ {} em {}x no cartão'.format(preco / parcela, parcela))
    else:
        print('ERRO \n TENTE NOVAMENTE')
elif forma == 4:
    parcela = int(input('Em quantas parcelas?'))
    print('Você pagará R$ {} em {}x no cartão'.format((preco * 1.2) / parcela, parcela))
    print('Preço total: R$ {}'.format(preco * 1.2))
else:
    print('ERRO. \n TENTE NOVAMENTE')
print('{:=^40}'.format('OBRIGADO PELA COMPRA!'))
