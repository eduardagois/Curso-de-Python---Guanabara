soma = 0
for c in range(0,6):
    num = int(input('Digite um número inteiro para somar:'))
    if num % 2 == 0:
        soma = soma + num
print(soma)