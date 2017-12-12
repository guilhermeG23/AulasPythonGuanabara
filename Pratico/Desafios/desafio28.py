import random
valor = random.randint(0, 5)

entrada = int(input('Digite um valor entre 0 a 5: '))

if valor == entrada:
    print("Seu valor foi: {}\nA maquina pensou o mesmo, venceu!".format(entrada))
else:
    print("Voce errou, seu valor {} e o valor da maquina {}".format(entrada, valor))
