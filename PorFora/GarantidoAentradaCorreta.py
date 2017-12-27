original = str(input("Entre com o valor: ")).lower()
print(len(original))
if original.isalpha():
  if len(original) <= 0:
    print("False")
  else:
    print(original)
else:
  print("Deu errado")
