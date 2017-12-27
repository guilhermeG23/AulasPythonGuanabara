#Estruturas de controle
#Controle simples

entrada = int(input('Entrada: '))
#Metodo de imprimir variavel no final
if entrada > 5:
    msg = 'Maior que 5'
elif entrada == 5:
    msg = 'Igual a 5'
else:
    msg = 'Inferior a 5'
print(msg)

#Funcao resumida
#Operador terminario

entrada = int(input('Entrada: '))
msg = 'Maior ou igual 5' if entrada >= 5 else 'Menor que 5'
print(msg)

