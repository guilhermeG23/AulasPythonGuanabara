#modulo
from tkinter import *

#ABA
aba = Tk()

#Title
aba.title('Anchor')

#Background
aba['bg'] = 'Black'

#Geometry
aba.geometry('400x400+100+100')

#Propiedade Side e Anchor
lb1 = Label(aba, text="LB1", bg='white')
lb2 = Label(aba, text="LB2", bg='red')
lb3 = Label(aba, text="LB3", bg='yellow')
lb4 = Label(aba, text="LB4", bg='blue')

#print
#Para usarmos o Anchor ele tem que usar os pontos da bussula
#Norte = N
#Nordeteste = NW
#Noroeste = NE
#Leste = E
#Sudeste = SE
#Sul = S
#Sudoeste = SW
#Oeste = W

#Usando o Side e o anchor ao mesmo tempo
lb1.pack(side=TOP, anchor=NW)
lb2.pack(side=TOP, anchor=NE)
lb3.pack(side=BOTTOM, anchor=SE)
lb4.pack(side=BOTTOM, anchor=SW)

#Main Loop
aba.mainloop()
