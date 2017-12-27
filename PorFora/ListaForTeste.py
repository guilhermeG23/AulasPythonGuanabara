#Lista Python
x = ['x1', 'x2', 'x3', 'x4']
x1 = ['x5', 'x6', 'x7', 'x8']

#Imprimindo o numero de valores que x carrega
print(len(x))

#Ou
#Imprimir valor por valor da lista
print('\n')
for a in x:
    print(a)

#Print primeiro valor
print(x[0])

#Print entre valores
print(x[1:4])

#Lista ao contrario
print([10, 20, 30, 40][::-1])

#comparacoes com listas, True e False
print('x1' in x)
print('as' in x)

#Juntando listas
print(x + x1)

#Printando listas
print(x * 2)

#Usando o reverse
print(x.reverse())

#Variaveis que aprendem
#Fazendo referencia, x2 não recebe x, ele faz referencia a x
x2 = x
x.append('TESTE')
print(x)

#Agora para copiar e não fazer referencia
x3 = x[:]#Copia
x.append('teste')
print(x)
print(x3)

#Valores de lista
lista = ['x1', 'x2', 'x3']
l = [lista, 'x4', 'x5']
print(l)

#Copiar valores
lista1 = lista[:]
lista.append('pastel de frango')
print(lista)
print(lista1)

#Limpando valores da lista
lista1.clear()
print(lista1)




