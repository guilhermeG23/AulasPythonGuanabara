# -*- coding: utf-8 -*-

#importa a bibioteca gráfica
from tkinter import *

class janela:
    def _init_(self, janelas):
        self.titulo = str(input('Titulo do arquivo: '))
        self.texto = str(input('Digite sua mensagem: '))
        arquivo = open('{}.txt'.format(titulo), 'w')
        arquivo.write(texto)
        arquivo.close()
 
root = Tk()
#cria a aplicação raiz. É uma janela com barra de título, botão para
#fechar,aumentar, etc.. Deve ser sempre o primeiro objeto a ser criado,
# e deve ser único em uma aplicação

root.title("Crie o arquivo")
root.geometry("300x200")
root.mainloop()
#inicializa o loop

