#Meu método
#Removendo os espaços da entrada
cidade = str(input("Entre com a cidade: ")).strip()
cidadeSanto = cidade.split(' ')[0]
if cidadeSanto.upper() == "SANTO":
    print("Sua cidade {}".format(cidade))
    print("Cidade começa com santo")
else:
    print("Sua cidade {}".format(cidade))
    print("Cidade não começa com santo")

#Método guanabara
print(cidade[:5].capitalize() == 'Santo')
