# 📂 Pasta `src/`

Esta pasta contém os **scripts principais do projeto**, incluindo pré-processamento, modelagem e avaliação dos modelos de machine learning.

---

## 📌 Estrutura da Pasta

```
📂 src/
│── 📜 README.md                  # Documentação desta pasta
│── 📜 preprocess.py               # Funções de pré-processamento dos dados
│── 📜 train_model.py              # Treinamento dos modelos de machine learning
│── 📜 evaluate_model.py           # Avaliação dos modelos treinados
```

---

## 🛠️ Descrição dos Arquivos

### 📑 `preprocess.py`
> **Objetivo:** Realizar o pré-processamento dos dados antes da modelagem.

🔧 **Principais funções:**
- Remover valores ausentes (se necessário) 🚫
- Aplicar codificação de variáveis categóricas 🔢
- Padronizar variáveis numéricas 📏
- Salvar os dados processados para uso posterior 💾

---

### 🎯 `train_model.py`
> **Objetivo:** Treinar os modelos de machine learning para prever o sentimento dos usuários.

🤖 **Principais funcionalidades:**
- Dividir os dados em treino e teste 📊
- Treinar modelos como **Regressão Logística** e **Random Forest** 🏆
- Salvar os modelos treinados para futuras previsões 💾

---

### 📊 `evaluate_model.py`
> **Objetivo:** Avaliar o desempenho dos modelos e gerar métricas de validação.

📈 **Principais funcionalidades:**
- Calcular métricas como **acurácia, precisão, recall e f1-score** 🏆
- Gerar a **matriz de confusão** para visualizar erros e acertos 📊
- Criar relatórios gráficos da performance dos modelos 📉

---

## 🚀 Como Utilizar os Scripts

### 1️⃣ Executar o pré-processamento dos dados
```bash
python src/preprocess.py
```

### 2️⃣ Treinar os modelos
```bash
python src/train_model.py
```

### 3️⃣ Avaliar os modelos
```bash
python src/evaluate_model.py
```

---

## 🤝 Contribuição
Caso faça modificações nos scripts, favor documentar as mudanças e garantir que todas as funções estejam devidamente comentadas.


