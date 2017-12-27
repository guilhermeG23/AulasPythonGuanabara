# -*- coding: utf-8 -*-

#importa a bibioteca gráfica
from tkinter import *
 
root = Tk()
#cria a aplicação raiz. É uma janela com barra de título, botão para
#fechar,aumentar, etc.. Deve ser sempre o primeiro objeto a ser criado,
# e deve ser único em uma aplicação
 
Mensagem = Label(root, text="Hello Word!\n\nGuilherme T.I")
#cria um label com o texto especificado
Mensagem.pack()
#insere na tela

root.title("Hello Word Com Interface")
root.geometry("400x300")
root.mainloop()
#inicializa o loop
