#Criando listas
#Modelos que funcionam para criar listas
l = list()
print(type(l))
l = []
print(type(l))

#Acrescentando valores em uma lista
l.append('x1')
print(l)
l.append('x2')
print(l)

#Adicionando na ordem que quiser
#Um exemplo é que cada valor está na ordem de entrada a partir de 0
#cada valor é listado a partir de zero e impresso

l.insert(1, 'x1.1')
print(l)

#Deletando um valor da lista a partir de sua chegada
#Deletando o valor que acabou de ser adicionado
del l[1]
print(l)

#Mostra o ultimo valor da lista e o removendo da lista
print(l.pop())
#Ou pode simplismente eliminar o valor
print(l.pop(0))

#Mais ações de listas
ls = ['1', '2', 't', '0', '12', '0']

#Adiciona um valor a lista
print(ls.extend('e'))

#Remove um valor da lista
print(ls.remove('t'))

