import tkinter as tk

janela = tk.Tk()
janela.minsize(800, 400) # O tamanho da Janela

v = tk.IntVar()

tk.Label(janela, text="Você Cursa Ciência Da Computação ?", justify=tk.LEFT, padx=50).pack() # O tamamho e a posição da janela

tk.Radiobutton(janela, text="Sim", padx=50, variable=v, value=1).pack(anchor=tk.W) # O tamamho e a posição do botão
tk.Radiobutton(janela, text="Não", padx=50, variable=v, value=2).pack(anchor=tk.W) # O tamamho e a posição do botão

janela.mainloop()