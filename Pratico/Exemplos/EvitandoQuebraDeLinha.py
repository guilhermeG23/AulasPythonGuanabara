n1 = float(input("Entrada 1: "))
n2 = float(input("Entrada 2: "))
#Controle de casas reais a serem impressas
print("Valor: {:.2f}".format(n1/n2))
#Juntando dois prints quebrados
print("Valor: {:.2f}".format(n1/n2), end='')
print("Testado na sida de valor")
#Colocando um valor na quebrar de prints
print("Valor: {:.2f}".format(n1/n2), end=' >>> ')
print("Testado na sida de valor")