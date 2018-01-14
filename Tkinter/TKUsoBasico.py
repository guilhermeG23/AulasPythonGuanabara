#Chamando toda a biblioteca e nomeando de outra forma
import tkinter as tk

#Chamando a funcao principal juntoda biblioteca
aba = tk.Tk()
#Criando um title
aba.title('Aba principal')
#BackGround
aba['bg'] = 'green'
#OU
#aba['background'] = 'green'
#Definir o tamanho da janela
#LxA+E+T
#COmo funciona = 400 de largura, 300 de altura
#100 de distancia da esquerda da tela e 100 de distancia do topo da janela
#Os dois parametros de 100 e 100 podem ser omitidos da impressão, pois não são obrigatorios na chamada
#O mesmo vale se a altura e a largura não forem chamadas, e sim a distancia das bordas da tela
#EX: Completo
aba.geometry('400x300+100+100')
#LxA
#aba.geometry('400x300')
#DE+DT
#aba.geometry('+100+100')
#Chamando a funcao principal
aba.mainloop()
