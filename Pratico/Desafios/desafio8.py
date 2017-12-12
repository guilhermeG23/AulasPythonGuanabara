entrada = float(input("Entrada em metros: "))
print("Valor em metros: {}\n Valor em decimetro: {}\nValor em Centimetros: {}\nValor em milimetros: {}".format(entrada, entrada * 10, entrada * 100, entrada * 1000), end = '')
#Melhorias que o guanabara pediu
print("\nValores em Km pra cima\nValor em decametro: {}\nValor em hectometro: {}\nValor em Kilometro: {}".format(entrada / 10, entrada / 100, entrada / 1000))