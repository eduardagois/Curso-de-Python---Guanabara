peso = float(input('Digite o peso em Kg:'))
altura = float(input('Digite a altura em metros:'))
imc = peso / altura ** 2

print('O seu IMC é: {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Você está obeso!')
elif imc >= 40:
    print('Você tem obesidade mórbida')