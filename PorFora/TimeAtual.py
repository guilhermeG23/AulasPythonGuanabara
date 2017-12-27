#Biblioteca
from datetime import datetime
#Variavel
now = datetime.now()
#Atual day Variavel
print(now)

#Imprimindo partes do dia
print(now.year)
print(now.day)
print(now.month)

#mais de uma forma de imprimir o date
print('{}-{}-{}'.format(now.year, now.month, now.day))
print('{}/{}/{}'.format(now.year, now.month, now.day))

#Imprimindo valores quebrados
print(now.hour)
print(now.minute)
print(now.second)

#Imprimindo as Horas 
print('{}:{}:{}'.format(now.hour, now.minute, now.second))

#Imprimindo tudo de uma vez
print('{}/{}/{} e {}:{}:{}'.format(now.day, now.month, now.year,now.hour, now.minute, now.second))
