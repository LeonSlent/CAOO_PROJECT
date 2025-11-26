import joblib
import numpy as np
import os
import sys

class Classificacao:
    
    def __init__(self):
        """
        Carrega o modelo K-Means e o Scaler na inicialização.
        """
        caminho_deste_arquivo = os.path.dirname(__file__)
        pasta_raiz = os.path.dirname(caminho_deste_arquivo)
        
        caminho_modelo = os.path.join(pasta_raiz, 'modelo_kmeans.joblib')
        caminho_scaler = os.path.join(pasta_raiz, 'scaler.joblib')

        try:
            self.modelo_kmeans = joblib.load(caminho_modelo)
            self.scaler = joblib.load(caminho_scaler)
            # print("✅ Modelos de IA carregados com sucesso.")
            
        except FileNotFoundError:
            print(f"❌ ERRO CRÍTICO: Não achei os arquivos .joblib na pasta: {pasta_raiz}")
            print("Certifique-se de ter rodado o 'treinamento.py' na raiz.")
            self.modelo_kmeans = None
            self.scaler = None

    def classificar(self, dados_atleta: list):
        """
        Recebe uma lista com 8 números e retorna o Cluster ID (0, 1 ou 2).
        """
        if self.modelo_kmeans is None or self.scaler is None:
            return None

        try:
            # O Scikit-learn espera um array 2D (uma lista de listas), mesmo para 1 pessoa
            dados_np = np.array(dados_atleta).reshape(1, -1)

            #Normaliza os dados 
            dados_normalizados = self.scaler.transform(dados_np)
            
            # K-Means diz qual é o grupo
            cluster_id = self.modelo_kmeans.predict(dados_normalizados)
            
            # Retorna o número inteiro
            return int(cluster_id[0])
            
        except Exception as e:
            print(f"Erro ao classificar: {e}")
            return None