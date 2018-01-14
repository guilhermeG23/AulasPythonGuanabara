#Modulo
#Chamando somente a funcao partial
from functools import partial
from tkinter import *

#Chamando a janela
aba = Tk()

#Geometry
aba.geometry("300x200+100+100")

#Criando uma definicao generica de chamada
#Como funciona: O bt vai ser chamado do botao com a chamada e o text vai receber o text ue o botao esta vinculado
#Definicao
def botao(bt):
    lb['text'] = bt['text']

#Caso voce tente usar o command para definir o result do Def vai dar erro pois voce esta tentado evocar a funcao e nao linkar

#Botao
#Reescrevendo uma chamada com partial
#BT1
bt1 = Button(aba, width=20, text='BT1')
#Reescrevendo o valor, defenicao e depois o valor dela(No caso o Botao e seu valor em TEXT)
#Correto
bt1['command'] = partial(botao, bt1)
#Errado
#bt1['command'] = botao(bt1): Isso é evocar a funcao o que dara um erro caso tente
bt1.place(x=50, y=50)

#BT2
bt2 = Button(aba, width=20, text='BT2')
#Reescrevendo o valor, defenicao e depois o valor dela(No caso o Botao e seu valor em TEXT)
bt2['command'] = partial(botao, bt2)
bt2.place(x=50, y=80)

#Label
lb = Label(aba, text='Sem chamada')
lb.place(x=50, y=110)
    
#Chamando a janela
aba.mainloop()
