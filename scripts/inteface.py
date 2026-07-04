from tkinter import *

# Cria a janela principal
janela = Tk()
janela.title("Minha Interface")
janela.geometry("500x300")

# Adiciona um rótulo
texto = Label(janela, text="Olá, bem-vindo à minha interface!")
print
texto.pack(pady=10)

# Inicia o loop da interface
janela.mainloop()   


