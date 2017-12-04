dias = int(input("Quantos dias você alugou o carro: "))
km = float(input("Kilometragem do Carro andada: "))
final = ((km * 0.15) + (dias * 60))
print("Dias que foi utilizado {}\nCusto dos dias alugados {}\nKm rodados {}\nValor de Km rodados {}\nO valor final é {:.2f}".format(dias, dias * 60, km, km * 0.15, final))