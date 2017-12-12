maior = 0
menor = 999999
digite1 = float(input('Digite um valor: '))

if digite1 > maior:
    maior = digite1
if digite1 < menor:
    menor = digite1

digite2 = float(input('Digite um valor: '))

if digite2 > maior:
    maior = digite2
if digite2 < menor:
    menor = digite2

digite3 = float(input('Digite um valor: '))

if digite3 > maior:
    maior = digite3
if digite3 < menor:
    menor = digite3

print('O maior valor é {}\nMenor valor é {}'.format(maior, menor))
