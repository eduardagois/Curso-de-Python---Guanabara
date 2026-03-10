r1 = float(input('Digite um valor, em cm, para medida de uma reta:'))
r2 = float(input('Digite para a segunda reta:'))
r3 = float(input('Agora, para a última reta:'))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
