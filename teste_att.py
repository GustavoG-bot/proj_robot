import tkinter as tk
import threading
from tkinter import ttk

def inicio():
    tela_finalizado.grid_forget() 
    tela_boas_vindas.grid()


def mostrar_tela_selecao():
    tela_boas_vindas.grid_forget()  # Oculta a tela de boas-vindas
    frame.grid()


def confirmar():

    drink = drink_selecionado.get()
    

    if drink == "Drink 1":
        drink = 1 
    if drink == "Drink 2":
        drink = 2 
    if drink == "Drink 3":
        drink = 3 
    
    alcool = alcool_selecionado.get()
    
    if alcool == "Fraco":
        alcool = 1 
    if alcool == "Médio":
        alcool = 2 
    if alcool == "Forte":
        alcool = 3 

    sabor = sabor_selecionado.get()
    
    if sabor == "Com Açúcar":
        sabor = 1 
    if sabor == "Sem Açúcar":
        sabor = 2 

    resposta = f"Drink: {drink}\nQuantidade de Álcool: {alcool}\nSabor: {sabor}"
    print(resposta)

    with open("dados.txt", "w") as arquivo:
        arquivo.write(f"{drink}\n")
        arquivo.write(f"{alcool}\n")
        arquivo.write(f"{sabor}\n")


    aguarde()

    threading.Thread(target=inicio).start()
    

def aguarde():

    frame.grid_forget()  # Oculta a tela de boas-vindas
    tela_aguarde.grid()
    while True:
        sinal = input("Digite '1' quando o drink estiver pronto: ")
        if sinal == '1':
            finalizado()
            break

def finalizado():


    tela_aguarde.grid_forget()  # Oculta a tela de boas-vindas
    tela_finalizado.grid() 
    var1.set(None)
    var2.set(None)
    var3.set(None)

    while True:
        sinal = input("Digite '1' quando retirar o copo: ")
        if sinal == '1':
            inicio()
            break  

    with open("dados.txt", "w") as arquivo:
        zerou = 0
        arquivo.write(f"{zerou}\n")
        arquivo.write(f"{zerou}\n")
        arquivo.write(f"{zerou}\n")



def selecionar_drink(opcao):
    drink_selecionado.set(opcao["text"])

def selecionar_alcool(opcao):
    alcool_selecionado.set(opcao["text"])

def selecionar_sabor(opcao):
    sabor_selecionado.set(opcao["text"])
    



root = tk.Tk()
root.title("Controle de Robô Barman")
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

estilo = ttk.Style()
estilo.configure("TRadiobutton", font=20)

v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()

## Tela de boas-vindas
tela_boas_vindas = tk.Frame(root, padx=100, pady=200)
tela_boas_vindas.grid(row=0, column=0, padx=50, pady=40)

boas_vindas_label = ttk.Label(tela_boas_vindas, text="Bem-vindo ao Robô Barman", font=("Arial", 24))
boas_vindas_label.pack(pady=20)

faca_pedido_button = ttk.Button(tela_boas_vindas, text="Faça seu pedido", command=mostrar_tela_selecao)
faca_pedido_button.pack()


## tela de selecao
frame = tk.Frame(root, padx=100, pady=100)
frame.grid(row=0, column=0, padx=50, pady=40)

frame.grid_forget()


# Crie colunas e linhas vazias para o alinhamento dos elementos
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)


drink_label = ttk.Label(frame, text="Escolha o drink:", font=("Arial", 24))
drink_label.grid(row=0, column=0, columnspan=3)

drink_selecionado = tk.StringVar()
botoes_drink = []

drink1_button = ttk.Radiobutton(frame, text="Drink 1", command=lambda: selecionar_drink(drink1_button), variable=var1, value=1)
drink2_button = ttk.Radiobutton(frame, text="Drink 2", command=lambda: selecionar_drink(drink2_button), variable=var1, value=2)
drink3_button = ttk.Radiobutton(frame, text="Drink 3", command=lambda: selecionar_drink(drink3_button), variable=var1, value=3)

botoes_drink.extend([drink1_button, drink2_button, drink3_button])

drink1_button.grid(row=1, column=0, padx=10, pady=30)
drink2_button.grid(row=1, column=1, padx=10, pady=30)
drink3_button.grid(row=1, column=2, padx=10, pady=30)

alcool_label = ttk.Label(frame, text="Escolha a quantidade de álcool:", font=("Arial", 24))
alcool_label.grid(row=2, column=0, columnspan=3)

alcool_selecionado = tk.StringVar()
botoes_alcool = []


fraco_button = ttk.Radiobutton(frame, text="Fraco", command=lambda: selecionar_alcool(fraco_button), variable=var2, value=1)
medio_button = ttk.Radiobutton(frame, text="Médio", command=lambda: selecionar_alcool(medio_button), variable=var2, value=2)
forte_button = ttk.Radiobutton(frame, text="Forte", command=lambda: selecionar_alcool(forte_button), variable=var2, value=3)

botoes_alcool.extend([fraco_button, medio_button, forte_button])

fraco_button.grid(row=3, column=0, padx=10, pady=30)
medio_button.grid(row=3, column=1, padx=10, pady=30)
forte_button.grid(row=3, column=2, padx=10, pady=30)

sabor_label = ttk.Label(frame, text="Escolha o sabor:", font=("Arial", 24))
sabor_label.grid(row=4, column=0, columnspan=3)

sabor_selecionado = tk.StringVar()
botoes_sabor = []

acucar_button = ttk.Radiobutton(frame, text="Com Açúcar", command=lambda: selecionar_sabor(acucar_button), variable=var3, value=1)
sem_acucar_button = ttk.Radiobutton(frame, text="Sem Açúcar", command=lambda: selecionar_sabor(sem_acucar_button), variable=var3, value=2)

botoes_sabor.extend([acucar_button, sem_acucar_button])

acucar_button.grid(row=5, column=0, padx=5, pady=10)
sem_acucar_button.grid(row=5, column=2, padx=5, pady=10)

confirmar_button = ttk.Button(frame, text="Confirmar", command=confirmar)
confirmar_button.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Tela aguardando
tela_aguarde = tk.Frame(root, padx=100, pady=200)
tela_aguarde.grid(row=0, column=0, padx=50, pady=40)

tela_aguarde.grid_forget()

aguarde_label = ttk.Label(tela_aguarde, text="Aguarde o drink está sendo preparado", font=24)
aguarde_label.pack(pady=20)


# Tela final 
tela_finalizado = tk.Frame(root, padx=100, pady=200)
tela_finalizado.grid(row=0, column=0, padx=50, pady=40)

tela_finalizado.grid_forget()

finalizado_label = ttk.Label(tela_finalizado, text="Pode retirar seu drink")
finalizado_label.pack(pady=20)

root.mainloop()
















