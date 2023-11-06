import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from pyModbusTCP.server import ModbusServer
from time import sleep


class Interface(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
    
        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Variáveis de controle
        self.var_1 = tk.IntVar(value=3)
        self.setup_widgets()
            
    def aumentar_fonte_radiobutton(self, tamanho_fonte):
        estilo = ttk.Style()
        estilo.configure("TRadiobutton", font=("Arial", tamanho_fonte))

    def setup_widgets(self):

        # Frame para Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text="Qual a boa hoje, meu chefe?", width=50, height=50)
        self.radio_frame.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=20, sticky="nsew")

        # Radiobuttons
        self.radio_1 = ttk.Radiobutton(self.radio_frame, text="Suco de Laranja", variable=self.var_1, value=1)
        self.radio_1.grid(row=0, column=0, padx=10, pady=0, sticky="nsew")

        self.radio_2 = ttk.Radiobutton(self.radio_frame, text="Suco de maçã", variable=self.var_1, value=2)
        self.radio_2.grid(row=0, column=1, padx=270, pady=0, sticky="nsew")

        self.radio_3 = ttk.Radiobutton(self.radio_frame, text="Suco de larançã", variable=self.var_1, value=3)
        self.radio_3.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")

        #Label
        self.label_1 = ttk.Label(
            self.radio_frame,
            text="Sinta a energia da manhã fluindo com cada gole do nosso suco de laranja fresco.\
O sol nasce nas suas papilas gustativas enquanto o suco dourado dança no seu copo.\
Cada gota é um abraço cítrico da natureza, trazendo um sorriso radiante ao seu rosto.\
O suco de laranja é a quintessência da vitalidade e um elixir da frescura.\
Deixe a laranja iluminar o seu dia.",
            justify="center",
            font=("-size", 10),
            wraplength=250
        )
        self.label_1.grid(row=1, column=0, pady=10, padx=5)

       #Label
        self.label_2 = ttk.Label(
            self.radio_frame,
            text="O suco de maçã puro é como uma mordida direto da árvore. \
Cada gole é uma celebração da doçura natural e da simplicidade. \
Ele desliza suavemente pela sua garganta, trazendo consigo o gosto da infância e \
lembranças de pomares ensolarados. Nossa maçã é escolhida a dedo e transformada em um \
néctar fresco e inigualável. Delicie-se com a pura alegria da maçã em cada sorvo!",
            justify="center",
            font=("-size", 10),
            wraplength=250
        )
        self.label_2.grid(row=1, column=1, pady=10)

        #Label
        self.label_3 = ttk.Label(
            self.radio_frame,
            text="Quando o doce beijo da maçã encontra a tangência cítrica da laranja, algo mágico acontece. \
É uma fusão cósmica de sabores que cria uma experiência sensorial inesquecível. \
Cada gole da nossa mistura de suco de laranja e maçã é uma jornada através de campos de frutas ensolarados, \
onde a harmonia reina suprema. Deixe-se levar por essa sinfonia de sabores.",
            justify="center",
            font=("-size", 10),
            wraplength=250
        )
        self.label_3.grid(row=1, column=2, pady=10, padx=5)

        #Label com imagem
        self.image_1 = Image.open("suco_laranja.jpg") 
        self.image_2 = Image.open("suco_laranja.jpg") 
        self.image_3 = Image.open("suco_laranja.jpg") 

        new_width = 150  # Largura desejada
        new_height = 150  # Altura desejada
        self.image_1 = self.image_1.resize((new_width, new_height))
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
        self.label_with_image_1 = tk.Label(self.radio_frame, image=self.photo_1)
        self.label_with_image_1.grid(row=2, column=0, pady=10, padx=15)

        self.image_2 = self.image_2.resize((new_width, new_height))
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        self.label_with_image_2 = tk.Label(self.radio_frame, image=self.photo_2)
        self.label_with_image_2.grid(row=2, column=1, pady=10, padx=0)

        self.image_3 = self.image_3.resize((new_width, new_height))
        self.photo_3 = ImageTk.PhotoImage(self.image_3)
        self.label_with_image_3 = tk.Label(self.radio_frame, image=self.photo_3)
        self.label_with_image_3.grid(row=2, column=2, pady=10, padx=0)


        # Frame para widgets de input
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(row=2, column=1, padx=10, pady=(30, 10), sticky="nsew")
        self.widgets_frame.columnconfigure(index=0, weight=2)

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Continuar", command=self.mostrar_aguarde)
        self.button.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        # Tela de Aguarde
        self.tela_aguarde = TelaAguarde(self.parent, self)
        self.tela_aguarde.grid(row=1, column=0, columnspan=3, padx=(0, 0), pady=0, sticky="nsew")
        self.tela_aguarde.grid_remove()

    def mostrar_aguarde(self):
        global valor_var_1
        valor_var_1 = self.var_1.get()
        print("Valor da variável var_1:", valor_var_1) 

        # Escreve valor do txt
        with open("valor_var_1.txt", "w") as file:
            file.write(str(valor_var_1))

        self.grid_forget()
        self.tela_aguarde.set_var_1_value(valor_var_1)
        self.tela_aguarde.grid()
        self.tela_aguarde.label_aguarde.grid()
        self.tela_aguarde.after(5000, self.voltar_para_tela_selecao)

    def voltar_para_tela_selecao(self):
        self.tela_aguarde.grid_remove()
        self.grid()
        # Escreve valor do txt
        with open("valor_var_1.txt", "w") as file:
            file.write(str(0))


class TelaAguarde(ttk.Frame):
    def __init__(self, parent, interface):
        ttk.Frame.__init__(self, parent)
        self.interface = interface
        self.label_aguarde = ttk.Label(self, text="Por favor, aguarde enquanto o robô faz o seu pedido!", font=("-size", 20))
        self.label_aguarde.grid(row=0, column=0, pady=300, padx=300)
    
    def set_var_1_value(self, value):
        self.var_1_value = value


if __name__ == "__main__":

    janela = tk.Tk()
    janela.geometry('1200x800')
    janela.title("Interface gráfica para pedido")
    
    # Simply set the theme
    #s = ttk.Style()
    #s.theme_use('classic')

    janela.tk.call("source", "azure.tcl")
    janela.tk.call("set_theme", "dark")

    # Adicione um texto simples à janela
    texto_janela = tk.Label(janela, text="Bem vindo ao XXXX! Selecione seu pedido e clique em continuar.", font=("Arial", 20))
    texto_janela.grid(row=1, column=0, padx=10, pady=10)

    # Set a minsize for the window, and place it in the middle
    janela.update()
    janela.minsize(janela.winfo_width(), janela.winfo_height())
    x_cordinate = int((janela.winfo_screenwidth() / 2) - (janela.winfo_width() / 2))
    y_cordinate = int((janela.winfo_screenheight() / 2) - (janela.winfo_height() / 2))
    janela.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    app = Interface(janela)
    app.grid()

    tamanho_fonte = 20
    app.aumentar_fonte_radiobutton(tamanho_fonte)

    janela.mainloop()












