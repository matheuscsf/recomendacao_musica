import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

def dividir_dados(df):
    """Separa as variáveis dependentes e independentes e divide os dados em treino e teste."""
    X = df.drop(columns=["rotulo_sentimento"])
    y = df["rotulo_sentimento"]
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def treinar_regressao_logistica(X_train, y_train):
    """Treina um modelo de Regressão Logística."""
    modelo = LogisticRegression(max_iter=500, solver="lbfgs", multi_class="multinomial")
    modelo.fit(X_train, y_train)
    joblib.dump(modelo, "models/logistic_regression.pkl")
    print("Modelo de Regressão Logística salvo em models/logistic_regression.pkl")
    return modelo

def treinar_random_forest(X_train, y_train):
    """Treina um modelo de Random Forest."""
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    joblib.dump(modelo, "models/random_forest.pkl")
    print("Modelo Random Forest salvo em models/random_forest.pkl")
    return modelo

def treinar_modelos(caminho_dados):
    """Executa o treinamento dos modelos e salva os arquivos."""
    df = pd.read_csv(caminho_dados)
    X_train, X_test, y_train, y_test = dividir_dados(df)
    modelo_lr = treinar_regressao_logistica(X_train, y_train)
    modelo_rf = treinar_random_forest(X_train, y_train)
    print("Treinamento concluído!")
    return modelo_lr, modelo_rf

# Exemplo de uso:
# treinar_modelos("data/processed_data.csv")
