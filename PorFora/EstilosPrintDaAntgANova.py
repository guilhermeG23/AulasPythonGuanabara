#Estilo de formatação no print

#Variaveis
x = 'teste'
x1 = 'teste12'
x2 = 'teste123123'

#Ruim
print('Hello ' + x + '!')

#Modo antigo
print('Hello %s!' % x)

#Metodo novo
print('Hello {}!'.format(x))

#Metodos de chamada
print('{0}, {1}, {0}, {2}'.format(x, x1, x2))

#Transformando o valor em binario
print('{:b}'.format(5))
print('{:b}'.format(23))
print('{:b}'.format(255))

