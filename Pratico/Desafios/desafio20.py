#Meio guanabara
from random import shuffle
nome1 = str(input('Digite o nome1: '))
nome2 = str(input('Digite o nome2: '))
nome3 = str(input('Digite o nome3: '))
nome4 = str(input('Digite o nome4: '))
lista = [nome1, nome2, nome3, nome4]

#Randomizar o eleito
shuffle(lista)
print('Ordem do sorteio foi...')
print(lista)

