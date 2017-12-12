#Jeito que eu consegui
nome = str(input("Entre com o nome: "))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
#Mostra só o primeiro nome: print(nome.split(' ')[0])
print(len(nome.split(' ')[0]))

#Método Guanabara
nome = str(input("Entre com o nome: ")).strip()
print("Nome em maiusculo: {}".format(nome.upper()))
print("Nome em minusculo: {}".format(nome.lower()))
print("Quantas letras tem seu nome sem os espaços: {}".format(len(nome) - nome.count(' ')))
print("Quantas letras tem o primeiro nome: {}".format(nome.find(' ')))

#Método a mais
#Faz uma lista e seleciona o primeiro valor da lista separa = nome.split()
print("Seu primeiro nome tem {} caracteres".format(len(separa[0])))
