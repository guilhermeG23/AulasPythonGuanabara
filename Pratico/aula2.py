#Entrada de valores inteiros e floats
valor1 = int(input("Valor1: "))
valor2 = int(input("Valor2: "))
valor3 = valor1 + valor2
print('Valor de saida formatador inteiro {}'.format(valor3))
#Saida customizada do guanabara desafio
#python 2 saida
print('A soma entre',valor1,'mais',valor2,'é igual há: {}'.format(valor3))
#Saida melhorada
#python 3 saida
print('A soma entre {} mais {} é igual há: {}'.format(valor1, valor2, valor3))
#Para identificar pode fazer isso(Não modifica a saida e nem atrapalha o resultado final)
#print('A soma entre {0} mais {1} é igual há: {2}'.format(valor1, valor2, valor3))
#Valores float
valor4 = float(input("Valor4: "))
valor5 = float(input("Valor5: "))
valor6 = valor5 + valor4
print('Valor de saida formatador float {}'.format(valor6))
#Como saber a saida do valor
print(type(valor6))
#Saida de strinf
entrada = str(input("Entrada: "))
print("Saida: {}".format(entrada))
#Saida boolean
#Saida boolem, se tem valor a saida e verdadeira, se não tem a saida é falsa
entrada1 = bool(input("Entrada Booleam: "))
print("Saida Booleam: {}".format(entrada1))