#trabalhando com métodos
entrada = input("Entrada: ")
print("Saida: {}".format(entrada))
#Tipo da entrada
print("Tipo: {}".format(type(entrada)))
#Entrada é Alpha-numero?
print("AlphaNumerico: {}".format(entrada.isalnum()))
#Entrada é alfabetica
print("Alpha: {}".format(entrada.isalpha()))
#Estrada é numerica
print("Numerico: {}".format(entrada.isnumeric()))
#Entrada é espaço vazio
print("Espaço: {}".format(entrada.isspace()))
#Entrada é minuscula
print("Minusculo: {}".format(entrada.islower()))
#Maiuscula
print("Maiusculo: {}".format(entrada.isupper()))
#Capitalizada(maiusculo e minusculo)
print("Capitalizada: {}".format(entrada.istitle()))