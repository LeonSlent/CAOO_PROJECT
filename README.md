# 🏀 Classificador de Atletas (Projeto de Semestre)

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-orange?logo=scikit-learn)
![SQLite](https://img.shields.io/badge/SQLite-blue?logo=sqlite&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green)

Aplicação desktop (Tkinter) que classifica atletas de basquete em 3 posições (Armador, Ala, Pivô) usando um modelo K-Means pré-treinado, como parte da avaliação semestral de Construção de Aplicações Orientadas a Objetos.

---

## Requisitos Técnicos Implementados

* **Machine Learning:** `K-Means` (via `scikit-learn`) para clusterização.
* **Arquitetura:** `Model-View-Controller (MVC)` para separação de responsabilidades.
* **Padrão de Projeto:** `Chain of Responsibility` para o fluxo de classificação (Validar -> Classificar -> Interpretar).
* **Persistência:** `SQLite` para armazenamento dos dados dos atletas cadastrados.
* **Interface:** `Tkinter` para a GUI (interface gráfica).

---

## Como Executar

1.  **Clone o repositório e entre na pasta:**
    ```bash
    git clone https://github.com/LeonSlent/CAOO_PROJECT
    cd CAOO_PROJECT
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Criar
    python -m venv .venv
    
    # Ativar (Windows CMD)
    .\.venv\Scripts\activate.bat
    
    # Ativar (macOS/Linux)
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a Aplicação:**
    ```bash
    python main.py
    ```

NOTA: Projeto está em fase de desenvolvimento, ainda farei a main
