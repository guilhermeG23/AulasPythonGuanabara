#conversor de dolar
import os

#conversor
os.system('clear')
escolha = str(input("Converter para Euro ou Dolar(E/D): "))

valor1 = "3.0824"
valor2 = "3.6900"
valor1 = float(valor1)
valor2 = float(valor2)

#Valor D
if(escolha=="D"):
    dolar = input("Digite o valor em reais: ")
    if(dolar==0):
        print("Voce digitou 0, nao a valor!")
    elif(dolar==("")):
        print("Voce nao digitou nenhum valor!")
    else:
        dolar = float(dolar)
        valorFinal = (dolar/valor1)
        print("O valor em Dolar e: ",'{0:,.2f}'.format(valorFinal))

#valor Dolar
elif(escolha=="Dolar"):
    dolar = input("Digite o valor em reais: ")
    if(dolar==0):
        print("Voce digitou 0, nao a valor!")
    elif(dolar==("")):
        print("Voce nao digitou nenhum valor!")
    else:
        dolar = float(dolar)
        valorFinal = (dolar/valor1)
        print("O valor em Dolar e: ",'{0:,.2f}'.format(valorFinal))

#valor d
elif(escolha=="d"):
    dolar = input("Digite o valor em reais: ")
    if(dolar==0):
        print("Voce digitou 0, nao a valor!")
    elif(dolar==("")):
        print("Voce nao digitou nenhum valor!")
    else:
        dolar = float(dolar)
        valorFinal = (dolar/valor1)
        print("O valor em Dolar e: ",'{0:,.2f}'.format(valorFinal))

#valor Dolar
elif(escolha=="dolar"):
    dolar = input("Digite o valor em reais: ")
    if(dolar==0):
        print("Voce digitou 0, nao a valor!")
    elif(dolar==("")):
        print("Voce nao digitou nenhum valor!")
    else:
        dolar = float(dolar)
        valorFinal = (dolar/valor1)
        print("O valor em Dolar e: ",'{0:,.2f}'.format(valorFinal))

#valor E
elif(escolha=="E"):
    euro = input("Digite o valor em reais: ")
    if(euro==0):
        print("Voce digitou 0, nao a valor!")
    elif(euro==("")):
        print("Voce nao digitou nenhum valor")
    else:
        euro = float(euro)
        valorFinal = (euro/valor2)
        print("O valor em Euro e: ",'{0:,.2f}'.format(valorFinal))

#valor Euro
elif(escolha=="Euro"):
    euro = input("Digite o valor em reais: ")
    if(euro==0):
        print("Voce digitou 0, nao a valor!")
    elif(euro==("")):
        print("Voce nao digitou nenhum valor")
    else:
        euro = float(euro)
        valorFinal = (euro/valor2)
        print("O valor em Euro e: ",'{0:,.2f}'.format(valorFinal))

#valor e
elif(escolha=="e"):
    euro = input("Digite o valor em reais: ")
    if(euro==0):
        print("Voce digitou 0, nao a valor!")
    elif(euro==("")):
        print("Voce nao digitou nenhum valor")
    else:
        euro = float(euro)
        valorFinal = (euro/valor2)
        print("O valor em Euro e: ",'{0:,.2f}'.format(valorFinal))

#valor euro
elif(escolha=="euro"):
    euro = input("Digite o valor em reais: ")
    if(euro==0):
        print("Voce digitou 0, nao a valor!")
    elif(euro==("")):
        print("Voce nao digitou nenhum valor")
    else:
        euro = float(euro)
        valorFinal = (euro/valor2)
        print("O valor em Euro e: ",'{0:,.2f}'.format(valorFinal))

#FIM
else:
    print("Saindo da Operacao")
    exit


