import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

ARQUIVO_DADOS = 'dados_projeto.csv'
ARQUIVO_SCALER = 'scaler.joblib'
ARQUIVO_MODELO = 'modelo_kmeans.joblib'

try:
    # Carega os dados
    dados = pd.read_csv(ARQUIVO_DADOS)  
    
    # Usando todas as colunas como caaracterísticas
    caracteristicas = dados

    if caracteristicas.empty:
        print(f"Erro: O arquivo '{ARQUIVO_DADOS}' está vazio.")
        exit()

    print(f"Dados carregados. {len(caracteristicas.columns)} features identificadas:")
    print(list(caracteristicas.columns))
    print(f"{len(caracteristicas)} amostras de atletas para treinar.")


    scaler = StandardScaler()
    caracteristicas_normalizadas = scaler.fit_transform(caracteristicas)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(caracteristicas_normalizadas)

    joblib.dump(kmeans, ARQUIVO_MODELO)
    joblib.dump(scaler, ARQUIVO_SCALER)

    print("\n" + "="*50)
    print("✅ Treinamento Concluído!")
    print(f"Modelo K-Means salvo em: {ARQUIVO_MODELO}")
    print(f"Scaler salvo em: {ARQUIVO_SCALER}")
    print("="*50)

    print("\nAnálise dos Centros dos Clusters (para sua interpretação):")
    # Para interpretar, vamos reverter a normalização dos centros
    centros_norm = kmeans.cluster_centers_
    centros_reais = scaler.inverse_transform(centros_norm)
    
    df_centros = pd.DataFrame(centros_reais, columns=caracteristicas.columns)
    df_centros['cluster_id'] = [0, 1, 2]
    
    # Adicionar contagem de atletas por cluster
    contagem_clusters = pd.Series(kmeans.labels_).value_counts().sort_index()
    df_centros['N_Atletas'] = contagem_clusters
    
    print(df_centros.to_string()) # .to_string() garante boa formatação
    
    print("\n--- Como Interpretar (Exemplo) ---")
    print("Olhe a tabela acima. O cluster com a maior 'estatura' e 'peso' médio")
    print("provavelmente será o de 'Pivôs'. O com menor 'estatura' e")
    print("maior 'abdominal' talvez seja 'Armador'.")
    print("Anote qual ID (0, 1, 2) corresponde a qual posição para usar")
    print("no seu Handler (Chain of Responsibility).")


except FileNotFoundError:
    print(f"Erro: Arquivo '{ARQUIVO_DADOS}' não encontrado.")
    print("Certifique-se de que ele está na mesma pasta que este script.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")