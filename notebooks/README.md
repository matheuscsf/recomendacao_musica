# 📂 Pasta `notebooks/`

Esta pasta contém os **notebooks Jupyter** utilizados no projeto. Os notebooks estão organizados em uma sequência lógica, desde a exploração dos dados até a modelagem preditiva.

---

## 📌 Estrutura da Pasta

```
📂 notebooks/
│── 📜 README.md                      # Documentação desta pasta
│── 📜 01-exploracao-dados.ipynb       # Análise exploratória (EDA)
│── 📜 02-pre-processamento.ipynb      # Pré-processamento dos dados
│── 📜 03-modelagem.ipynb              # Modelagem preditiva
```

---

## 📝 Descrição dos Notebooks

### 🔍 `01-exploracao-dados.ipynb`
> **Objetivo:** Realizar a **análise exploratória dos dados (EDA)** para entender padrões e distribuições.

📊 **Principais etapas:**
- Visualização da distribuição dos sentimentos dos usuários 🎭
- Análise da relação entre BPM, gênero musical e sentimentos 🎶
- Correlações entre as variáveis 🔗

---

### 🛠️ `02-pre-processamento.ipynb`
> **Objetivo:** Preparar os dados para a modelagem, garantindo que estejam limpos e prontos para serem utilizados.

🔧 **Principais etapas:**
- Tratamento de valores ausentes (se necessário) 🚫
- Codificação de variáveis categóricas (One-Hot Encoding e Label Encoding) 🔢
- Padronização da variável BPM 📈
- Redução de dimensionalidade com PCA 🔄

---

### 🤖 `03-modelagem.ipynb`
> **Objetivo:** Treinar e avaliar modelos de machine learning para prever o sentimento do usuário baseado nas características musicais.

🤖 **Principais etapas:**
- Divisão dos dados em treino e teste 🎯
- Treinamento dos modelos de **Regressão Logística** e **Random Forest** 🏆
- Avaliação dos modelos com métricas como **acurácia, precisão e recall** 📊
- Matriz de Confusão para análise dos erros ❌✅

---

## 🚀 Como Executar os Notebooks

Para executar os notebooks, siga os passos abaixo:

1️⃣ Ative o ambiente virtual (se estiver usando):
```bash
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2️⃣ Inicie o Jupyter Notebook:
```bash
jupyter notebook
```

3️⃣ Acesse a pasta `notebooks/` e abra os arquivos desejados.

---

## 🤝 Contribuição
Caso faça modificações nos notebooks, favor documentar as mudanças com comentários e salvar novas versões com nomes descritivos.


