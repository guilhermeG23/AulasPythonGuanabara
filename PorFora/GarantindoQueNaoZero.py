#Garantindo que não é zero python 2.7
#original = raw_input("Enter a word: ")
#3.5
original = str(input("Entre com o valor: "))
if len(original) <= 0:
	print("False")
else:
	print(original)
