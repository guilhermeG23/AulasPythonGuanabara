altura = float(input("Altura da parede: "))
largura = float(input("Largura da parede: "))
area = altura * largura
print("A Altura da parede é: {:.2f} e a largura é: {:.2f}\nA area em quadrados da parede é {:.2f}\nprecisa de {:.2f} litros de tinta para pinta-la.".format(altura, largura, area, area / 2))