#Importa tudo sem consideração, assim voce não precisa fazer referencia a biblioteca quando usar
from tkinter import *

#Definindo a classe
#Classes em Python utilizam nomenclatura em maiusculo
aba = Tk()

#Entrada de label
#Antes de tudo, depois de definir um Label, voce tem que escolher o responsavel pela janela, o pai, no caso usamos a ABA()
#Agora definimos que o Valor recebeo Label
#E configuramos o gerenciador de layout que ira utilizar, no caso o place, no place ajustamos as coordenadas x e y, que sa as distancias para a borda da janela TK
valor = Label(aba, text='Hello Word')
valor.place(x=10, y=10)
#Geometria da aba
aba.geometry('300x300+100+100')

#Inicia a janela
aba.mainloop()
