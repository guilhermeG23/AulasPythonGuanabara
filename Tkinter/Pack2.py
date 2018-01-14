#Modulo
from tkinter import *

#Aba
aba = Tk()

#Title
aba.title("Pack 2")

#Geometry
aba.geometry('400x400+100+100')

#background
aba['bg'] = 'Black'

#Label
l1 = Label(aba, text="LB1")
l2 = Label(aba, text="LB2")
l3 = Label(aba, text="LB3")
l4 = Label(aba, text="LB4")

#Pack
#Usar o Side quer dizer limitar o espaco para o primeiro que a recebe, caso outro tentar, ficara limitado a 1px do limite do primeiro(Na borda) podemos dizer
l1.pack(side=RIGHT)
l2.pack(side=BOTTOM)
l3.pack(side=LEFT)
l4.pack(side=TOP)

#Loop Main
aba.mainloop()
