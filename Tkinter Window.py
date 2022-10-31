import tkinter as tk  #Importando a biblioteca

janela = tk.Tk()  # Criando o widget ou (ou componentes) do Tkinter.

janela.title("GUI COM PYTHON")  # Criando o titulo da janela com a biblioteca tkinter

janela.minsize(1200, 800)    # O tamanho é de 1200 px de largura e 600 de altura
janela.resizable(True, True) # A janela possa ser redimensionada

# janela.resizable(True, False) # Usando isso a janela será redimensionada só a parte da lagura
# janela.resizable(False, True) # Usando isso a janela será redimensionada só a parte da altura
# janela.resizable(True, True)  # Usando isso impedi que a janela será redimensionada

tk.Label(janela, text= "Exemplo 1:").grid(column=0, row=0) # A posição da janela com texto
tk.Label(janela, text= "Exemplo 2:").grid(column=0, row=1) # A posição da janela com texto
tk.Label(janela, text= "Exemplo 3:").grid(column=0, row=2) # A posição da janela com texto


janela.mainloop()  # Loop principal da janela