entrada = str(input("Entre com uma frase: ")).upper().strip()
print('Quantas letras A tem na frase: {}'.format(entrada.count('A')))
print('Primeira letra A: {}'.format(entrada.find('A')))
#Procurando a partir da direita
#rfind = le pela direita
print('Ultima letra A: {}'.format(entrada.rfind('A')))
