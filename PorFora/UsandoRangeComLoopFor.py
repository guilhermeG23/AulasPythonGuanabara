#Usando o Range
for i in range(10):
    print(i, end=',')

#EX: Range(1, 10, 2) = do 1 a 10 pulando 2 casas
#Igual: 1, 3, 5, 7, 9

#Outros modelos de range
#Imprime o valor e pula dois a frente
#EX:1 ,3, 5, 7, 9
print('\n')
for i in range(1, 11, 2):
    print(i, end=',')

#Fazer o inverso
print('\n')
for i in range(10, 0, -1):
    print(i, end=',')

#Funcao ENUMERATE
print('\n')
for i, c in enumerate('Hello Word!'):
    print(i, c)
