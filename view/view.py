import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sys

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
        self.btn_lista = tk.Button(self.root, text="Lista de Atletas", font=("Arial", 18, "bold"), bg="#B4460F", width=26, height=1, command=lambda: self.trocar_tela(self.lista_atletas))
        self.btn_lista.place(relx=0.5, rely=0.6, anchor="n")

        # Criando o botão de sair
        self.btn_sair = tk.Button(self.root, text="Sair", font=("Arial", 18, "bold"), bg="#B4460F", width=26, height=1, command=lambda: self.close())
        self.btn_sair.place(relx=0.5, rely=0.7, anchor="n")

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
        self.btn_cadastrar_atleta = tk.Button(self.root, text="Cadastrar", font=("Arial", 16, "bold"), bg="#B4460F", command=lambda: self.adicionar_atleta())
        self.btn_cadastrar_atleta.place(relx=0.75, rely=0.77, anchor="n")

    def lista_atletas(self):
        self.root.resizable(False, False)
        self.root.title("Classificador de Atletas")
        self.root.geometry("1200x720")
        self.root.config(bg="#D2BBB0")

        # Criando o fundo da tela
        self.frame_fundo = tk.Frame(self.root, width=1160, height=680, bg="#B4460F", relief="solid")
        self.frame_fundo.place(relx=0.5, rely=0.5, anchor="center")

        # Criando o frame do titulo 
        self.frame_titulo = tk.Frame(self.root, bg="#D2BBB0", relief="solid")
        self.frame_titulo.place(relx=0.5, rely=0.05, anchor="n")

        # Titulo
        self.titulo = tk.Label(self.frame_titulo, text="Lista de Atletas", font=("Arial", 32, "bold"), bg="#B4460F", fg="black")
        self.titulo.pack(pady=5)

        # --- ÁREA DE PESQUISA ---
        self.entry_pesquisa = tk.Entry(self.frame_fundo, font=("Arial", 11), width=50)
        self.entry_pesquisa.place(relx=0.35, rely=0.18, anchor="n")

        self.btn_pesquisar = tk.Button(self.frame_fundo, text="Pesquisar", font=("Arial", 8, "bold"), bg="white", fg="#030303", width=12, height=1, 
                                       command=self.pesquisar_atleta) # <--- AQUI: Chamando a função de pesquisa corretamente
        self.btn_pesquisar.place(relx=0.57, rely=0.177, anchor="n")

        # --- TABELA (TREEVIEW) ---
        self.tree = ttk.Treeview(self.frame_fundo, columns=("ID","Nome", "Posição", "Peso", "Estatura", "Altura", "Flexibilidade", "Abdominal", "Força", "Salto H", "Salto V",), show="headings", height=13)
        self.tree.place(relx=0.5, rely=0.3, anchor="n")

        # Cabeçalhos
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome", command=lambda: self.treeview_ordenacao(self.tree, "Nome", False))
        self.tree.heading("Posição", text="Posição", command=lambda: self.treeview_ordenacao(self.tree, "Posição", False))
        self.tree.heading("Peso", text="Peso", command=lambda: self.treeview_ordenacao(self.tree, "Peso", False))
        self.tree.heading("Estatura", text="Estatura", command=lambda: self.treeview_ordenacao(self.tree, "Estatura", False))
        self.tree.heading("Altura", text="Altura TC", command=lambda: self.treeview_ordenacao(self.tree, "Altura", False))
        self.tree.heading("Flexibilidade", text="Flexibilidade", command=lambda: self.treeview_ordenacao(self.tree, "Flexibilidade", False))
        self.tree.heading("Abdominal", text="Abdominal", command=lambda: self.treeview_ordenacao(self.tree, "Abdominal", False))
        self.tree.heading("Força", text="Força", command=lambda: self.treeview_ordenacao(self.tree, "Força", False))
        self.tree.heading("Salto H", text="Salto H", command=lambda: self.treeview_ordenacao(self.tree, "Salto H", False))
        self.tree.heading("Salto V", text="Salto V", command=lambda: self.treeview_ordenacao(self.tree, "Salto V", False))

        # Colunas
        self.tree.column("ID", width=0, anchor="w", stretch=False)
        self.tree.column("Nome", width=200, anchor="c")
        self.tree.column("Posição", width=100, anchor="c")
        self.tree.column("Peso", width=80, anchor="c")
        self.tree.column("Estatura", width=80, anchor="c")
        self.tree.column("Altura", width=80, anchor="c")
        self.tree.column("Flexibilidade", width=80, anchor="c")
        self.tree.column("Abdominal", width=80, anchor="c")
        self.tree.column("Força", width=80, anchor="c")
        self.tree.column("Salto H", width=80, anchor="c")
        self.tree.column("Salto V", width=80, anchor="c")

    
        self.atualizar_treeview() # Carrega os dados na tabela
        
        # Botões do rodapé
        self.btn_voltar = tk.Button(self.root, text="Voltar", font=("Arial", 16, "bold"), bg="#FDFDFD", command=lambda: self.trocar_tela(self.tela_inicial))
        self.btn_voltar.place(relx=0.23, rely=0.77, anchor="n")

        self.btn_excluir = tk.Button(self.root, text="Excluir", font=("Arial", 16, "bold"), bg="#FDFDFD", command=self.excluir_atleta)
        self.btn_excluir.place(relx=0.75, rely=0.77, anchor="n")

    def excluir_atleta(self):
        # Pega o item selecionado
        item_selecionado = self.tree.selection()
        if not item_selecionado:
            return 
        id_do_atleta = item_selecionado[0]
        
        # 2. Pergunta confirmação
        if messagebox.askyesno("Confirmar", "Deseja realmente excluir?"):
            
            # 3. Chama o controller e guarda o resultado
            excluiu_com_sucesso = self.controller.excluir_atleta(id_do_atleta)
            
            # 4. Verifica o resultado e avisa o usuário
            if excluiu_com_sucesso:
                # A própria View chama seu método de recarregar a lista
                self.atualizar_treeview() 
                messagebox.showinfo("Sucesso", "Atleta excluído.")
            else:
                messagebox.showerror("Erro", "Não foi possível excluir o atleta.")

    def atualizar_treeview(self, lista_dados=None):
        # Limpa a tabela e insere novos dados
        if lista_dados is None:
            # Se não passar nada, busca tudo
            lista_dados = self.controller.buscar_todos_atletas()

        # Limpa a tabela atual
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Insere os dados
        for atleta in lista_dados:
            self.tree.insert("", "end", iid=atleta[0], values=atleta)

    def pesquisar_atleta(self):
        texto_digitado = self.entry_pesquisa.get()
        
        # Chama o controller
        resultados = self.controller.pesquisar_atleta(texto_digitado)
        
        # Atualiza a tela com o resultado
        self.atualizar_treeview(resultados)

    def adicionar_atleta(self, ):

        # Pega os valores da carta
        nome = self.entryNome.get()
        altura = self.entryAltura.get()
        peso = self.entryPeso.get()
        flexibilidade = self.entryFlexibilidade.get()
        forca = self.entryForca.get()
        abdominal = self.entryAbdominal.get()
        salto_horizontal = self.entrySalto_horizontal.get()
        salto_vertical = self.entrySalto_vertical.get()
        altura_tc = self.entryAlturaTC.get()
        # Chama o controller para validar a entrada
        resultado = self.controller.validar_entrada_view(nome, [peso, altura, altura_tc, flexibilidade, abdominal, forca, salto_horizontal, salto_vertical])
        if resultado:
            messagebox.showinfo("Sucesso", f"Atleta classificado como: {resultado}")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Erro na classificação do atleta.")

    def treeview_ordenacao(self, tv, col, reverse):
        # tv: o widget Treeview que será ordenado.
        # col: o nome da coluna que deve ser usada para ordenar.
        # Pega todos os itens da treeview. tv.get_children('') pega todos os IDs dos itens da árvore.
        # tv.set(k, col) obtém o valor da coluna col do item k.
        # Então l é uma lista do tipo: [(valor_coluna, id_item), ...]
        l = [(tv.set(k, col), k) for k in tv.get_children('')]

        # Tenta ordenar numericamente se possível
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse) 
        except ValueError:
            l.sort(key=lambda t: t[0].lower(), reverse=reverse)  # se ordenação falhou com numeros inteiros (no caso de nome) ordena o texto em ordem alfabetica

        # Reorganiza os itens agora ja ordenados
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

            # Atualiza o comando do cabeçalho para alternar a ordem na próxima vez
        tv.heading(col, command=lambda: self.treeview_ordenacao(tv, col, not reverse))

    def limpar_campos(self):
        self.entradas = [
        self.entryAltura, 
        self.entryPeso, 
        self.entryFlexibilidade, 
        self.entryForca, 
        self.entryAbdominal, 
        self.entrySalto_horizontal, 
        self.entrySalto_vertical, 
        self.entryAlturaTC
        ]
    
        # Limpa o campo de nome
        self.entryNome.delete(0, tk.END)
        
        # Limpa os campos numéricos (sua lista self.entradas)
        for ent in self.entradas:
            ent.delete(0, tk.END)

    def close(self):
        sys.exit()