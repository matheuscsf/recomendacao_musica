import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def carregar_dados(caminho_arquivo):
    """Carrega os dados a partir de um arquivo CSV."""
    df = pd.read_csv(caminho_arquivo)
    return df

def renomear_colunas(df):
    """Renomeia as colunas para português do Brasil."""
    df.rename(columns={
        "User_ID": "id_usuario",
        "User_Text": "texto_usuario",
        "Sentiment_Label": "rotulo_sentimento",
        "Recommended_Song_ID": "id_musica_recomendada",
        "Song_Name": "nome_musica",
        "Artist": "artista",
        "Genre": "genero",
        "Tempo (BPM)": "bpm",
        "Mood": "humor",
        "Energy": "energia",
        "Danceability": "dancabilidade"
    }, inplace=True)
    return df

def tratar_valores_nulos(df):
    """Verifica e trata valores nulos na base de dados."""
    df.fillna(method='ffill', inplace=True)
    return df

def codificar_variaveis(df):
    """Aplica codificação nas variáveis categóricas."""
    label_encoder = LabelEncoder()
    df["rotulo_sentimento"] = label_encoder.fit_transform(df["rotulo_sentimento"])
    df = pd.get_dummies(df, columns=["genero", "humor", "energia", "dancabilidade"], drop_first=True)
    return df

def padronizar_bpm(df):
    """Padroniza a variável BPM usando StandardScaler."""
    scaler = StandardScaler()
    df["bpm"] = scaler.fit_transform(df[["bpm"]])
    return df

def salvar_dados_processados(df, caminho_saida):
    """Salva os dados pré-processados em um arquivo CSV."""
    df.to_csv(caminho_saida, index=False)
    print(f"Dados pré-processados salvos em {caminho_saida}")

def preprocessar_dados(caminho_entrada, caminho_saida):
    """Executa todas as etapas de pré-processamento."""
    df = carregar_dados(caminho_entrada)
    df = renomear_colunas(df)
    df = tratar_valores_nulos(df)
    df = codificar_variaveis(df)
    df = padronizar_bpm(df)
    salvar_dados_processados(df, caminho_saida)
    return df

# Exemplo de uso:
# preprocessar_dados("data/dataset.csv", "data/processed_data.csv")
