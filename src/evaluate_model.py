import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def carregar_modelo(caminho_modelo):
    """Carrega um modelo treinado salvo em arquivo."""
    return joblib.load(caminho_modelo)

def avaliar_modelo(modelo, X_test, y_test):
    """Avalia o modelo com métricas de desempenho."""
    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)
    relatorio = classification_report(y_test, y_pred)
    matriz_confusao = confusion_matrix(y_test, y_pred)
    return acuracia, relatorio, matriz_confusao

def plotar_matriz_confusao(matriz_confusao, nome_modelo):
    """Plota a matriz de confusão."""
    plt.figure(figsize=(6,5))
    sns.heatmap(matriz_confusao, annot=True, fmt="d", cmap="Blues")
    plt.title(f"Matriz de Confusão - {nome_modelo}")
    plt.xlabel("Predito")
    plt.ylabel("Real")
    plt.show()

def executar_avaliacao(df):
    """Executa a avaliação dos modelos salvos."""
    _, X_test, _, y_test = train_test_split(df.drop(columns=["rotulo_sentimento"]), df["rotulo_sentimento"], test_size=0.2, random_state=42, stratify=df["rotulo_sentimento"])
    
    modelo_lr = carregar_modelo("models/logistic_regression.pkl")
    modelo_rf = carregar_modelo("models/random_forest.pkl")
    
    acuracia_lr, relatorio_lr, matriz_confusao_lr = avaliar_modelo(modelo_lr, X_test, y_test)
    acuracia_rf, relatorio_rf, matriz_confusao_rf = avaliar_modelo(modelo_rf, X_test, y_test)
    
    print("\n=== Regressão Logística ===")
    print(f"Acurácia: {acuracia_lr:.2f}")
    print(relatorio_lr)
    plotar_matriz_confusao(matriz_confusao_lr, "Regressão Logística")
    
    print("\n=== Random Forest ===")
    print(f"Acurácia: {acuracia_rf:.2f}")
    print(relatorio_rf)
    plotar_matriz_confusao(matriz_confusao_rf, "Random Forest")
