#Modulo
from tkinter import *

#Interface: O TK é sempre maiusculo
aba = Tk()

#Geometry
aba.geometry("300x200+100+100")

#Definindo funcao
#Funcao sera impressa no console
def bt_click():
    print('Comando funciona')
    #Alterando a propriedade do Label abaixo, para quando apertar o botao ele altera a funcao
    #alterando uma propriedade
    lb['text'] = "É Claro"
    
#Botao
#Comando, onde aparece, tamanho do botao, texto do botao, comando a executar, não usar () pois isso define uma funcao
bt = Button(aba, width=20, text="OK", command=bt_click)
#Imprimi o botao, coloca a osição que ele é chamado
bt.place(x=50, y=50)

#Chamada
lb = Label(aba, text="Comando funciona")
lb.place(x=50, y=100)

#Chamada da interface
aba.mainloop()
