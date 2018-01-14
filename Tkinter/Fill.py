#Modulo
from tkinter import *

#Aba
aba = Tk()

#Title
aba.title('Fill')

#Geometry
aba.geometry('400x400+100+100')

#Background
aba['bg'] = "Black"

#Label
lb1 = Label(aba, text="LB1", bg="white")
lb2 = Label(aba, text="LB2", bg="red")
lb3 = Label(aba, text="LB3", bg="yellow")
lb4 = Label(aba, text="LB4", bg="blue")

#Fill
#Usa o plano cartesiano: X = Horizontal, Y = Vertical
#Caso não possuem texto, ele ficam no tamanho minimo possivel
lb4.pack(side=TOP, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)
lb1.pack(side=BOTTOM, fill=X)


#Main Loop
aba.mainloop()
