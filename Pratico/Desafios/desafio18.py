#Este é so o guanabara
#Não consegui

#Importando tudo
#import math

#Impotando so algumas bibliotecas
from math import radians, sin, cos, tan

angulo = float(input("Entre com o angulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("Senho: {:.2f}".format(seno))
print("Cosseno: {:.2f}".format(cosseno))
print("Tangente: {:.2f}".format(tangente))
