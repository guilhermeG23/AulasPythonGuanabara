#Uso de sticky

#Modulo
from tkinter import *

#Aba
aba = Tk()

#Title
aba.title('Sticky')

#Geometry
aba.geometry('400x300+100+100')

#Label
#Width = Largura
#Heigth = Altura
lb1 = Label(aba, text='LABEL1', width=20, height=5, bg="Red")
lbh = Label(aba, text='LABEL LOG HORINZON', bg="green")#REFERENCIA
lbv = Label(aba, text='LABEL LOG VERTICAL', bg="Yellow")

#Imprimir valores
#Sem o Sticky, ele fica centralizado na celula
#Sticky usa referencia aos pontos do anchor
lb1.grid(row=0, column=0, sticky=W)
lbh.grid(row=1, column=0, sticky=W)
lbv.grid(row=0, column=1, sticky=N)
#lbh.grid(row=1, column=0, sticky=E)
#lbv.grid(row=0, column=1, sticky=S)

#Main Loop
aba.mainloop()
