#Meu método
#So o: from math import sqrt
#Ou: from math import hypot
import math
a = float(input("Entre com o Cateto Adjacente A do triangulo retangulo: "))
b = float(input("Entre com o Cateto Oposto B do triangulo retangulo: "))
hipotenusa = (a**2) + (b**2)
print("A Hipotenusa é {:.2f}".format(math.sqrt(hipotenusa)))

#Método Guanabara(Equação na raça)
adjacente = float(input("Entre com o Adjacente do triangulo retangulo: "))
oposto = float(input("Entre com o oposto do triangulo retangulo: "))
hipotenusa = (adjacente ** 2 + oposto ** 2) ** (1/2)
print("Valor da Hipotenusa: {:.2f}".format(hipotenusa))

#Segundo método guanabara muito util
adj = float(input("Entre com o Adjacente: "))
opos = float(input("Entre com o Oposto: "))
hip = math.hypot(opos, adj)
print("Hipotenusa: {:.2f}".format(hip))
