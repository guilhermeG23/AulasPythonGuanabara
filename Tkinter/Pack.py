#Modulo
from tkinter import *

#Aba
aba = Tk()

#Geometry
aba.geometry("400x400+100+100")

#Cor de fundo
aba['bg'] = 'Black'

#Teste Pack
#Entrada Label
#Se isso existe, não significa que todos serao usados
lb1 = Label(aba, text="LB1", bg='red')
lb2 = Label(aba, text="LB2", bg='white')
lb3 = Label(aba, text="LB3", bg='pink')
lb4 = Label(aba, text="LB4", bg='green')

#Usando o PACK
#Por padrao ele imprimi no centro e no top da TK
#Ha ordem de chamada altera a impressao
#Topo
lb1.pack(side=TOP)
#Esquerda
lb2.pack(side=LEFT)
#Direita
lb3.pack(side=RIGHT)
#Embaixo
lb4.pack(side=BOTTOM)

#MainLoop
aba.mainloop()
