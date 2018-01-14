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

#Expand
#Define as areas em igualdade, alem de reajustar automaticamente a tel caso precise
lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

#Main Loop
aba.mainloop()
