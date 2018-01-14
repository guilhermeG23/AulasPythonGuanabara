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

#Grid
#Sistema de grade, trabalha com linhas e colunas, tipo uma tabela
#Ele conta do 0X0, topo da tela e na ponta(Canto superior a esquerda)
#O elemento sempre vai na ponta mais proxima que conseguir
#Row = Linha
#Column = coluna

#O grip pode sobrepor uns ao outros
#Os valores de inicio seram o topo da tela, e todos os depois seram baseados nele
#O menor valor do grid sera seu canto superior esquerdo
#Resto se baseado na distancia entre ele, mesmo se for 0 para 10, o 10 ficara ao lado dele
#O grid alinha todos os elementos para ficar o mais proximo ao canto supeior esquerdo
#O importante é o intervalo definido
lb1.grid(row=0, column=0)
lb2.grid(row=0, column=1)
lb3.grid(row=1, column=0)
lb4.grid(row=1, column=1)

#Main Loop
aba.mainloop()
