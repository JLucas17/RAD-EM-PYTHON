import tkinter as tk

def mostrar_nomes(): # função mostar nomes
    print(f"Nome: {e1.get()}\nSobrenome: {e2.get()}")

janela = tk.Tk()
janela.minsize(800, 400) # O tamanho é de 800 px de largura e 400 de altura
janela.title(" Insira os seus dados")

tk.Label(janela, text="Nome").grid(row=0)       # Criando texto Nome na janela
tk.Label(janela, text="Sobrenome").grid(row=1)  # Criando texto Sibrenome na janela

e1 = tk.Entry(janela)
e2 = tk.Entry(janela)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(janela, text="Exibir Dados", command=mostrar_nomes).grid(row=5, column=0, sticky=tk.W, pady=4)

# O comando janela.destroy tambem pode ser usado como janela.quit

tk.Button(janela, text="Sair", command=janela.quit).grid(row=5, column=1, sticky=tk.E, pady=4)

janela.mainloop()

# Exempo Do Cadastro
# Nome: João Lucas
# Sobrenome: Brito 