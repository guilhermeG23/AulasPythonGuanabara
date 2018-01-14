#Botao de vai e volta

#Modulo
from tkinter import *

#Interface: O TK é sempre maiusculo
aba = Tk()

#Geometry
aba.geometry("300x200+100+100")

#Blocos de instrucao
#Def = Valores a imprimir
#BT1
def click_bt1():
    print('Primeiro BOTAO')
    lb['text'] = 'BT1'
#BT2
def click_bt2():
    print('Segundo BOTAO')
    lb['text'] = 'BT2'

#Botoes
#O command vincula a funcao no Command
bt1 = Button(aba, width=20, text="B1", command=click_bt1)
bt2 = Button(aba, width=20, text="B2", command=click_bt2)

#Imprimindo Botoes com suas coordenadas
bt1.place(x=50, y=50)
bt2.place(x=50, y=80)

#Comando label
lb = Label(aba, text="")
lb.place(x=50, y=120)

#Chamada do loop
aba.mainloop()
