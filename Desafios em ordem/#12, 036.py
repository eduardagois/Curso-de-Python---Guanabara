casa = float(input('Digite o valor de compra da casa em R$:'))
salario = float(input('Agora digite o seu salário em R$:'))
anos = int(input('Em quantos anos você quer terminar de pagar a casa?'))
prestacao = casa / (anos * 12)

if prestacao > salario * 0.3:
    print('Não é possível conseguir um empréstimo! \n O valor da prestação da casa de {} R$, num período de {} anos, excedeu 30% do seu salário! \n Já que custou {:.2f} R$!'.format(casa, anos, prestacao))
else:
    print('O empréstimo será concedido! \n O valor da prestação da casa de {} R$, num período de {} anos, excedeu 30% do seu salário! \n Já que {:.2f} R$!'.format(casa, anos, prestacao))

