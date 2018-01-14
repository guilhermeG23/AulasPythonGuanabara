#Bem facil de usar o GRID, Slava mesmo na hora da interface grafica

#Modulo
from tkinter import *

#Aba
aba = Tk()

#Title
aba.title('Fill')

#Geometry
aba.geometry('200x100+100+100')

#Painel

#Label
User = Label(aba, text="Login: ")
Pass = Label(aba, text="Password: ")

#Entrada
name = Entry(aba)
senha = Entry(aba)

#botao
Btn = Button(aba, text="Confirmar")

#Usando o Grid
User.grid(row=0, column=0)
Pass.grid(row=1, column=0)
name.grid(row=0, column=1)
senha.grid(row=1, column=1)
Btn.grid(row=2, column=1)

#Main Loop
aba.mainloop()
