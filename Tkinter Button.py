import tkinter as tk

contador = 0

def contador_label(label_rotulo): # Iniciando a definição de uma função.
    def funcao_contar():
        global contador
        contador += 0.001
        label_rotulo.config(text="{:.3f}".format(contador))
        label_rotulo.after(1, funcao_contar) # 1 milisegundo
    
    funcao_contar() # Função contar


janela = tk.Tk()

janela.title("Cronomentro")

janela.minsize(800, 600) # O tamanho é de 1200 px de largura e 600 de altura
janela.resizable(True, True) # A janela possa ser redimensionada

label_rotulo = tk.Label(janela, fg="blue")  # O valor do fg é a cor da contagem 
label_rotulo.pack()

contador_label(label_rotulo)

botao = tk.Button(janela, text="Interromper a Contagem", width=70, command=janela.destroy) # O valor do "width" é para o tamanho da quadro de Interromper a Contagem
botao.pack()

janela.mainloop()