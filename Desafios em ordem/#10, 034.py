salario = float(input('Digite o salário do funcionário em R$:'))

if salario > 1250.00:
    print('O salário sofrerá um aumento de 10%, resultando em {:.2f} R$'.format(salario * 1.10))
else:
    print('O salário sofrerá um aumento de 15%, resultando em {} R$'.format(salario * 1.15))
