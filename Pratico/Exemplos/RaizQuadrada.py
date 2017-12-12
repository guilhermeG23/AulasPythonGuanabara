#Import tudo
import math

#Importando so o sqrt
#from math import sqrt

#por biblioteca
entrada = float(input("Digite o valor: "))
print("O valor: {}\nRaiz Quadrada do valor é: {:.2f}".format(entrada, math.sqrt(entrada)))
#Aredondando pra cima
raiz = math.sqrt(entrada)
print("O valor: {}\nRaiz Quadrada do valor é: {:.2f}".format(entrada, math.ceil(raiz)))
#Aredonda pra baixo
print("Raiz Quadrada do valor é: {:.2f}".format(math.floor(raiz)))

#OU = por equação
print("Por equação: {:.2f}".format(entrada ** (1/2)))

#Ou = por comando
print("Por equação: {:.2f}".format(pow(entrada, (1/2))))
