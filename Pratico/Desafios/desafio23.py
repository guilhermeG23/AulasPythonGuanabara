#Método guanabara
valor = int(input("Entre com o valor inteiro: "))
valor1 = valor // 1 % 10
valor2 = valor // 10 % 10
valor3 = valor // 100 % 10
valor4 = valor // 1000 % 10
print('Valor da unidade: {}'.format(valor1))
print('Valor da Dezena: {}'.format(valor2))
print('Valor da Centena: {}'.format(valor3))
print('Valor da milhar: {}'.format(valor4))
