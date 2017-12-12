preco = float(input("Valor atual: "))
#Meu jeito de fazer porcento no code(Mania de fazer rapido no C)
desc = preco - ((preco / 100) * 5)
print("Valor com desconto de 5%: {:.2f}".format(desc))