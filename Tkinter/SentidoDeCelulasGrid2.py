#Mesclagem de Celulas e colunas

#Modulo
from tkinter import *

#Aba
aba = Tk()

#Title
aba.title('Mesclagem')

#Geometry
aba.geometry('400x300+100+100')

#Label
#Width = Largura
#Heigth = Altura
lb1 = Label(aba, text='LABEL1', width=10, height=5, bg="Red")
lb2 = Label(aba, text='LABEL2', width=10, height=5, bg="Green")
lb3 = Label(aba, text='LABEL3', width=10, height=5, bg="Yellow")
lb4 = Label(aba, text='LABEL4', width=10, height=5, bg="Blue")
#Externo Label
lb5 = Label(aba, text='LABEL5', height=5, bg="Purple")
lb6 = Label(aba, text='LABEL6', height=5, bg="Pink")

#Juntado mais de duas celulas a partir de colunas e linhas
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=1)
#Label externo
#Columnspan e rowspan, junta colunas(Mescla colunas)
#Os span definem quantas celulas ele juntaram a partir do ponto onde inicializam
#O sticky esta chamando do Norte a sul e leste a oeste, o que significa que o + é uma junção, de que pontoa que ponto
lb5.grid(row=0, column=2, rowspan=2, sticky=N+S)
lb6.grid(row=2, column=0, columnspan=2, sticky=W+E)

#Main Loop
aba.mainloop()
