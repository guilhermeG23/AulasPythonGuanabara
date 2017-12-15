#IMprimindo colorido
print('\033[31mOlá, Mundo')

#Cor de fundo
print('\033[1;31;42mOlá mundo')

#Limitando a area do back
#Se voce digitar denovo o code de cor e nao colocar nada ele quebra a sequencia e não deixa continuar limitando sua area
print('\033[1;31;42mOlá mundo\033[m')

#Alguns testes
print('\033[4;31;47mOlá mundo\033[m')
print('\033[7mOlá mundo\033[m')
print('\033[1;32mOlá mundo\033[m')
print('\033[7;30mOlá mundo\033[m')

#As cores começam a partir do code o que significa que pode começar em qualquer lugar do print
#EX:
print('Olá \033[1;31;42mmundo\033[m')

#Usando o format
valor = 'guilherme'
print('print meu nome {}{}{}'.format('\033[1;33m', valor, '\033[m'))
#Sem quebra de cor
print('print meu nome {}{}'.format('\033[1;33m', valor))
#O resultado é igual, porém tudo o que estiver a baixo tem a cor alterada tambem

#usando uma 'lista' = dicionario
#Recebe padrões
cores = {'limpa':'\033[m',
         'cor1':'\033[1;31;43m',
         'cor2':'\033[1;32;42m'}

print('{}print meu nome {}{}{}'.format(cores['limpa'], cores['cor1'], valor, cores['limpa']))