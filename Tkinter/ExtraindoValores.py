#Modulo
from tkinter import *

#Definindo a ABA
aba = Tk()

#Geometry
aba.geometry('400x200+100+100')
"""
#Como funciona

Entry = É o comando de entrada da caixa de texto, no momento que escrever qualquer coisa ele ja vai possuir um valor
Porem este valor fica somente nele

A funcao get() captura o valor que esta dentro do Entry

#Mas como funciona
Digitamos uma entrada e relacionamos um botao para que quando fosce apertado ele ira capturar o valor do entry e imprimi-lo usando o get na variavel Label
"""
#Def
def printar():
    saida['text'] = entrada.get()

#Entrada
#Caixa de entrada
entrada = Entry(aba)
entrada.place(x=10, y=10)

#Botao
botao = Button(aba, width=20, text='Entrada', command=printar)
botao.place(x=150, y=10)

#Label
saida = Label(aba, text='Padrao')
saida.place(x=10, y=50)

#Chamando a ABA de Loop
aba.mainloop()
