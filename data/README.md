# 📂 Pasta `data/`

Esta pasta contém os **dados utilizados no projeto**. Aqui você encontrará a base de dados original e quaisquer versões processadas ou modificadas para análise.

---

## 📌 Estrutura da Pasta

```
📂 data/
│── 📜 README.md                  # Documentação desta pasta
│── 📜 dataset.csv                # Base de dados original do Kaggle
│── 📜 processed_data.csv         # Dados pré-processados (se necessário)
```

---

## 📥 Base de Dados Original
📍 **Nome:** `dataset.csv`
📍 **Fonte:** [Kaggle - AI-Powered Music Recommendation System](https://www.kaggle.com/datasets/ziya07/ai-powered-music-recommendation-system?select=music_sentiment_dataset.csv)
📍 **Descrição:** Contém informações sobre músicas recomendadas e os sentimentos dos usuários após ouvi-las.

**Principais Colunas:**
- `id_usuario`: Identificação do usuário
- `texto_usuario`: Comentário do usuário sobre a música
- `rotulo_sentimento`: Sentimento expresso (Happy, Sad, Relaxed, Motivated)
- `id_musica_recomendada`: ID único da música
- `nome_musica`: Nome da música
- `artista`: Nome do artista
- `genero`: Gênero musical
- `bpm`: Batidas por minuto da música
- `humor`: Classificação emocional da música
- `energia`: Nível de energia da música
- `dancabilidade`: Indica se a música é dançante

---

## 🔄 Dados Processados
Caso os dados passem por pré-processamento (remoção de ruídos, tratamento de valores nulos, codificação de variáveis), os arquivos resultantes serão salvos aqui com nomes apropriados, como `processed_data.csv`.

---

## 🚀 Como Utilizar os Dados
Para carregar os dados em um notebook Python, utilize o seguinte código:
```python
import pandas as pd

df = pd.read_csv("data/dataset.csv")
df.head()
```

Caso esteja trabalhando com os dados processados:
```python
df = pd.read_csv("data/processed_data.csv")
df.head()
```

---

## 🤝 Contribuição
Caso realize modificações na base de dados, favor documentar as alterações e salvar o novo arquivo com um nome descritivo.


