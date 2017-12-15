#Meu jeito

#Valor maior e menor
maior = 0
menor = 999999

#Sequencia sem o for nem if
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

print('O maior valor é {:.2f}\nMenor valor é {:.2f}'.format(maior, menor))

#Jeito guanabara

#Verificando o maior
maior = digite1
if digite2 > digite1 and digite2 > digite3:
    maior = digite2
if digite3 > digite1 and digite3 > digite2:
    maior = digite2
#Verificando o menor
menor = digite1
if digite2 < digite1 and digite2 < digite3:
    menor = digite2
if digite3 < digite1 and digite3 < digite2:
    menor= digite3

#Resultado
print('Resultado, Maior {:.2f}\nMenor {:.2f}'.format(maior, menor))
