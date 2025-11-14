import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("MTG Manager")
        self.root.geometry("1200x720")
        self.root.config(bg="#FFFFFF")
        self.frame_atual = None
        self.tela_inicial()

    def main_loop(self):
        self.root.mainloop()

    # Função para trocar de tela
    def trocar_tela(self, tela_nova):
        self.controller.fun_troca_tela(tela_nova)

    def tela_inicial(self):
        self.root.resizable(False, False) #proibe aumentar a tela
        self.root.title("Classificador de Atletas") #Titulo da tela
        self.root.geometry("1200x720") #Tamanho da tela
        self.root.config(bg="#D2BBB0") #Cor de fundo inteiro da tela

        # Criando o fundo da tela
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="#B4460F", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo 
        self.frame_titulo = tk.Frame(self.root, bg="#D2BBB0", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # criando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Classificador de Atletas - Basquete", font=("Arial", 32, "bold"),bg="#B4460F", fg="black")
        self.titulo.pack(pady=5)

        # Criando frame de fundo do menu
        self.frame_botoes = tk.Frame(self.root, width=800, height=500, bg="#D2BBB0", relief="solid")
        self.frame_botoes.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o botão de novos atletas
        self.btn_cadastro = tk.Button(self.root, text="Cadastro de Atletas", font=("Arial", 18, "bold"), bg="#B4460F", width=26, height=1, command=lambda: self.trocar_tela(self.cadastro))
        self.btn_cadastro.place(relx=0.5, rely=0.5, anchor="n")

        # Criando o botão de lista de atletas
        self.btn_cadastro = tk.Button(self.root, text="Lista de Atletas", font=("Arial", 18, "bold"), bg="#B4460F", width=26, height=1)
        self.btn_cadastro.place(relx=0.5, rely=0.6, anchor="n")

        # Criando o botão de sair
        self.btn_cadastro = tk.Button(self.root, text="Sair", font=("Arial", 18, "bold"), bg="#B4460F", width=26, height=1)
        self.btn_cadastro.place(relx=0.5, rely=0.7, anchor="n")

        # criando imagem
        imagem = Image.open("img/bola.png") #diretório da imagem
        imagem = imagem.resize((200, 200), Image.Resampling.LANCZOS) #redimencionando a imagem
        self.imagem_tk = ImageTk.PhotoImage(imagem) #convertendo a imagem para o formato do tkinter
        label_imagem = tk.Label(self.root, bg="#D2BBB0", image=self.imagem_tk) # Adicionando a imagem ao label
        label_imagem.place(relx=0.5, rely=0.2, anchor="n") # Adicionando a imagem ao frame
        self.label_imagem = label_imagem

    def cadastro(self):
        self.root.resizable(False, False) #proibe aumentar a tela
        self.root.title("Classificador de Atletas") #Titulo da tela
        self.root.geometry("1200x720") #Tamanho da tela
        self.root.config(bg="#D2BBB0") #Cor de fundo inteiro da tela

        # Criando o fundo da tela
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="#B4460F", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo 
        self.frame_titulo = tk.Frame(self.root, bg="#D2BBB0", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # criando o Título dentro do Frame
        self.titulo = tk.Label(self.frame_titulo, text="Adicionando novo atleta", font=("Arial", 32, "bold"),bg="#B4460F", fg="black")
        self.titulo.pack(pady=5)

        # Criando frame de fundo do menu
        self.frame_botoes = tk.Frame(self.root, width=800, height=500, bg="#D2BBB0", relief="solid")
        self.frame_botoes.place(relx=0.5, rely=0.5, anchor="center")

        #Crianco um frame para centralizar todas as entradas juntas
        agrupador_frame = tk.Frame(self.root, bg="#D2BBB0")
        agrupador_frame.place(relx=0.5, rely=0.25, anchor="n")

        # Colocando a entrada de nome
        label_nome = tk.Label(agrupador_frame, text='Nome:', font=("Arial", 16, "bold"), bg="#B4460F")
        label_nome.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.entryNome = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryNome.grid(row=0, column=1, padx=5, pady=5)

        #Colocando a entrada de alltura
        label_altura = tk.Label(agrupador_frame, text='Altura:', font=("Arial", 16, "bold"), bg="#B4460F")
        label_altura.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entryAltura = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryAltura.grid(row=1, column=1, padx=5, pady=5)

        # Colocando a entrada de Peso
        label_peso = tk.Label(agrupador_frame, text='Peso:', font=("Arial", 16, "bold"), bg="#B4460F")
        label_peso.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.entryPeso = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryPeso.grid(row=2, column=1, padx=5, pady=5)

        # Colocando a entrada de flexibilidade
        label_flexibilidade = tk.Label(agrupador_frame, text='Flexibilidade:', font=("Arial", 16, "bold"), bg="#B4460F")
        label_flexibilidade.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.entryFlexibilidade = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryFlexibilidade.grid(row=3, column=1, padx=5, pady=5)

        # Colocando a entrada de força
        label_forca = tk.Label(agrupador_frame, text="Força", font=("arial", 16, "bold"), bg="#B4460F")
        label_forca.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.entryForca = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryForca.grid(row=4, column=1, padx=5, pady=5)

        # Colocando a entrada de abdominal
        label_abdominal = tk.Label(agrupador_frame, text="Abdominal", font=("arial", 16, "bold"), bg="#B4460F")
        label_abdominal.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.entryAbdominal = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryAbdominal.grid(row=5, column=1, padx=5, pady=5)

        # Colocando a entrada de salto horizontal
        label_salto_horizontal = tk.Label(agrupador_frame, text="Salto horizontal", font=("arial", 16, "bold"), bg="#B4460F")
        label_salto_horizontal.grid(row=6, column=0, sticky="e", padx=5, pady=5)
        self.entrySalto_horizontal = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entrySalto_horizontal.grid(row=6, column=1, padx=5, pady=5)

        # Colocando a entrada de salto vertical
        label_salto_vertical = tk.Label(agrupador_frame, text="Salto vertical", font=("arial", 16, "bold"), bg="#B4460F")
        label_salto_vertical.grid(row=7, column=0, sticky="e", padx=5, pady=5)
        self.entrySalto_vertical = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entrySalto_vertical.grid(row=7, column=1, padx=5, pady=5)

        # Colocando a entrada da altura TC
        label_alturaTC = tk.Label(agrupador_frame, text="Altura TC", font=("arial", 16, "bold"), bg="#B4460F")
        label_alturaTC.grid(row=8, column=0, sticky="e", padx=5, pady=5)
        self.entryAlturaTC = tk.Entry(agrupador_frame, width=30, font=("Arial", 17, "bold"), bg="#B4460F", fg="black")
        self.entryAlturaTC.grid(row=8, column=1, padx=5, pady=5)

        # Botão de voltar pro menu inicial e de cadastrar atleta
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 16, "bold"), bg="#B4460F", command=lambda: self.trocar_tela(self.tela_inicial))
        self.btn_voltar.place(relx=0.23, rely=0.77, anchor="n")
        self.btn_cadastrar_atleta = tk.Button(self.root, text="Cadastrar", font=("Arial", 16, "bold"), bg="#B4460F")
        self.btn_cadastrar_atleta.place(relx=0.75, rely=0.77, anchor="n")