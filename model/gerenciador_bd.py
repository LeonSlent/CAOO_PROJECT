import sqlite3
import os

NOME_BD = "atletas.db"

class GerenciadorBD:
    
    def __init__(self, nome_bd=NOME_BD):

        pasta_raiz = os.path.dirname(os.path.dirname(__file__))
        self.caminho_bd = os.path.join(pasta_raiz, nome_bd)
        
        self.criar_tabela_atletas()

    def _conectar(self):

        try:
            return sqlite3.connect(self.caminho_bd)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def criar_tabela_atletas(self):
        sql_comando = """
        CREATE TABLE IF NOT EXISTS atletas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,  -- <--- ADICIONADO: Nome do atleta
            timestamp TEXT NOT NULL,
            
            -- As 8 features
            peso REAL NOT NULL,
            estatura REAL NOT NULL,
            altura_setado REAL NOT NULL,
            flexibilidade REAL NOT NULL,
            abdominal REAL NOT NULL,
            forca_arremesso REAL NOT NULL,
            salto_horizontal REAL NOT NULL,
            salto_vertical REAL NOT NULL,
            
            -- O resultado da classificação
            posicao_classificada TEXT NOT NULL 
        );
        """
        
        conn = self._conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(sql_comando)
                conn.commit()
                print(f"Tabela 'atletas' verificada no banco.")
            except sqlite3.Error as e:
                print(f"Erro ao criar tabela: {e}")
            finally:
                conn.close()

    def salvar_atleta(self, nome: str, dados_atleta: list, posicao: str):
        if len(dados_atleta) != 8:
            print("Erro: dados_atleta deve ter 8 valores.")
            return False

        sql_insert = """
        INSERT INTO atletas (
            nome, timestamp, 
            peso, estatura, altura_setado, flexibilidade, 
            abdominal, forca_arremesso, salto_horizontal, salto_vertical, 
            posicao_classificada
        ) VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        dados_para_salvar = (nome, *dados_atleta, posicao)
        
        conn = self._conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(sql_insert, dados_para_salvar)
                conn.commit()
                print(f"Atleta '{nome}' salvo com sucesso como '{posicao}'.")
                return True
            except sqlite3.Error as e:
                print(f"Erro ao salvar atleta: {e}")
                return False
            finally:
                conn.close()
        return False
    
    def buscar_todos_atletas(self):
        # Conecta ao banco
        conn = sqlite3.connect(self.caminho_bd)
        cursor = conn.cursor()
        
        try:
            sql = """
            SELECT 
                id, 
                nome, 
                posicao_classificada,
                peso, 
                estatura, 
                altura_setado,
                flexibilidade, 
                abdominal, 
                forca_arremesso,
                salto_horizontal,
                salto_vertical
            FROM atletas
            """
            cursor.execute(sql)
            dados = cursor.fetchall() 
            return dados
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return []
        finally:
            conn.close()
    
    def excluir_atleta(self, id_atleta):
        sql = "DELETE FROM atletas WHERE id = ?"
        
        conn = self._conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(sql, (id_atleta,))
                conn.commit()
                print(f"Atleta com ID {id_atleta} excluído.")
                return True
            except sqlite3.Error as e:
                print(f"Erro ao excluir: {e}")
                return False
            finally:
                conn.close()
        return False
    
    def buscar_atletas_por_nome(self, nome_parcial):
        conn = sqlite3.connect(self.caminho_bd)
        cursor = conn.cursor()
        
        try:
            sql = """
            SELECT 
                id, 
                nome, 
                posicao_classificada, 
                peso, 
                estatura, 
                altura_setado, 
                flexibilidade, 
                abdominal, 
                forca_arremesso, 
                salto_horizontal, 
                salto_vertical
            FROM atletas
            WHERE nome LIKE ?
            """
            cursor.execute(sql, (f'%{nome_parcial}%',)) 
            dados = cursor.fetchall()
            return dados
        except Exception as e:
            print(f"Erro na pesquisa: {e}")
            return []
        finally:
            conn.close()
    
'''
# Bloco de Teste
if __name__ == "__main__":
    # Teste rápido
    db = GerenciadorBD()
    # Dados fictícios
    db.salvar_atleta("Michael Jordan (Teste)", [90, 198, 150, 50, 40, 5.5, 200, 100], "Ala")
    '''