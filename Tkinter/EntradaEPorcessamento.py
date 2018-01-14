#Modulo
from tkinter import *

#Aba
aba = Tk()

#Geometry
aba.geometry('400x200+100+100')

#Title
aba.title('Equação')

#Funcao
def somador():
    #Meu modo
    #Convertedo e fazendo a soma
    #Se não converter em vez de fazer a soma, ele ira concatenar as strings como get
    #valor['text'] = int(valor1.get()) + int(valor2.get())

    #Analisa a entrada e ve se o valor pode ser convertido, isnumeric analisa se io valor caractere pode se tornar um valor numerico
    if(str(valor1.get()).isnumeric() and str(valor2.get()).isnumeric()):
        v1 = float(valor1.get())
        v2 = float(valor2.get())
        valor['text'] = v1 + v2
    #Caso não ele printa uma mensagem de aviso
    else:
        valor['text'] = "Achei que tinha aviso!!!"
#Aviso
entrada = Label(aba, text="Entrada so de valores, tudo que não for uma valor numerico dara erro")
entrada.place(x=10, y=5)

#Entradas
valor1 = Entry(aba, width=20)
valor1.place(x=50, y=30)

valor2 = Entry(aba, width=20)
valor2.place(x=50, y=70)

#Somando Place
somador = Button(aba, width=20, text="Somador", command=somador)
somador.place(x=50, y=100)

#Printar soma
#Frase da soma
lb = Label(aba, text="Resultado: ")
lb.place(x=50, y=140)

#Valor inteiro da soma
valor = Label(aba, text="")
valor.place(x=110, y=140)

#Aba Loop
aba.mainloop()
