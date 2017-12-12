#clonado, meio a meio, guanabara
import random
#Não é obrigatorio usar o str para strings no python
nome1 = str(input('Digite o nome1: '))
nome2 = str(input('Digite o nome2: '))
nome3 = str(input('Digite o nome3: '))
nome4 = str(input('Digite o nome4: '))
lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice(lista)
print('O elemento sorteado foi:', sorteio)
