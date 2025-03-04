# 🎵 Análise do Impacto do Ritmo e Gênero Musical no Humor dos Usuários

## 📌 Sobre o Projeto
Este projeto analisa a relação entre **o gênero musical, o BPM e o sentimento** dos usuários após ouvirem determinadas músicas. A partir dos dados obtidos, aplicamos técnicas de **ciência de dados e machine learning** para encontrar padrões e criar modelos preditivos que podem ser usados por empresas de mídia, marketing e streaming musical.

📊 **Metodologia:**
- Análise Exploratória de Dados (EDA)
- Redução de Dimensionalidade com PCA
- Modelagem Preditiva com Regressão Logística e Random Forest
- Avaliação dos Modelos com Matriz de Confusão

📂 **Base de Dados:** [Kaggle - AI-Powered Music Recommendation System](https://www.kaggle.com/datasets/ziya07/ai-powered-music-recommendation-system?select=music_sentiment_dataset.csv)

---

## 📦 Estrutura do Projeto
```
📦 music-sentiment-analysis
│── 📜 README.md                 # Documentação do projeto
│── 📂 data                      # Contém a base de dados
│   ├── music_sentiment_dataset.csv  # Arquivo original do Kaggle
│── 📂 notebooks                 # Contém os notebooks do projeto
│   ├── 01-exploracao-dados.ipynb   # Análise exploratória (EDA)
│   ├── 02-pre-processamento.ipynb  # Pré-processamento dos dados
│   ├── 03-modelagem.ipynb          # Modelagem preditiva
│── 📂 src                        # Código-fonte do projeto
│   ├── preprocess.py             # Funções de pré-processamento
│   ├── train_model.py            # Treinamento do modelo
│   ├── evaluate_model.py         # Avaliação do modelo
│── 📂 reports                    # Relatórios e insights
│   ├── eda_report.pdf            # Relatório da análise exploratória
│   ├── model_results.pdf         # Resultados da modelagem
│── 📂 assets                     # Imagens e gráficos gerados
│   ├── matriz_confusao.png       # Matriz de confusão do modelo
│   ├── pca_visualizacao.png      # Gráfico de PCA
│── 📂 requirements               # Dependências do projeto
│   ├── requirements.txt          # Lista de pacotes necessários
```

---

## 🚀 Como Executar o Projeto
### 1️⃣ Clone o repositório
```bash
git clone https://github.com/matheuscsf/music-sentiment-analysis.git
cd music-sentiment-analysis
```

### 2️⃣ Crie um ambiente virtual e instale as dependências
```bash
python -m venv venv
source venv/bin/activate   # No Windows, use: venv\Scripts\activate
pip install -r requirements/requirements.txt
```

### 3️⃣ Execute os notebooks
Abra os notebooks na pasta `notebooks` para visualizar as análises e modelagens:
```bash
jupyter notebook
```

---

## 📊 Resultados e Insights
✅ **Músicas com BPM mais alto tendem a sentimentos positivos (Happy, Motivated).**

✅ **Gêneros como Clássico estão associados a sentimentos relaxantes.**

✅ **Modelos de machine learning (Regressão Logística e Random Forest) apresentaram 100% de acurácia, indicando uma boa separabilidade entre classes.**

---

## 🤝 Contribuição
Sinta-se livre para contribuir! Caso tenha ideias de melhorias, abra uma *issue* ou envie um *pull request*.

---

## 📜 Licença
Este projeto é distribuído sob a licença MIT. Veja mais detalhes em [LICENSE](LICENSE).

