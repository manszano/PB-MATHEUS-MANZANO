<div>
  <img src="https://github.com/user-attachments/assets/7bad38b5-9a4f-4a79-a606-95c9701d737a" width="100%" alt="Banner">
</div>


&nbsp;
# 📱 Análise de Aplicativos do Google Play Store

Bem-vindo ao projeto de análise de dados dos aplicativos disponíveis no Google Play Store! 🎉 Neste projeto, exploramos o dataset `googleplaystore.csv` e realizamos diversas operações de análise para obter insights interessantes sobre os aplicativos, tais como número de instalações, avaliações, categorias mais populares e muito mais! 🚀

## 📂 Estrutura do Projeto

O código está organizado em várias etapas, conforme descrito abaixo:

### 1. Importação das bibliotecas

Começamos com a importação das bibliotecas essenciais para manipulação de dados e visualização de gráficos:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### 2. Leitura do dataset

O arquivo `googleplaystore.csv` é lido e carregado em um DataFrame pandas para ser manipulado:

```python
df = pd.read_csv('googleplaystore.csv')
```

### 3. Limpeza de dados

Para garantir a consistência dos dados, realizamos a remoção de linhas duplicadas:

```python
df_limpo = df.drop_duplicates()
```

### 4. Gráficos 📊

Diversos gráficos são gerados para visualizar os dados de forma clara e informativa:

#### Top 5 Apps por Número de Instalações (em bilhões):

Um gráfico de barras exibe os 5 aplicativos mais instalados.

```python
top_5_apps = df_limpo.nlargest(5, 'Installs')[['App', 'Installs']]
plt.bar(top_5_apps['App'], top_5_apps['Installs'])
```

#### Distribuição de Categorias dos Apps:

Um gráfico de pizza mostra a proporção das categorias dos aplicativos.

```python
plt.pie(categorias_frequencia, labels=categorias_frequencia.index)
```

### 5. Análise Estatística 🔍

Realizamos várias análises descritivas, como:

#### App mais caro:

Descobrimos qual o aplicativo mais caro disponível na loja.

```python
app_mais_caro = df.loc[df['Price'].idxmax()][['App', 'Price']]
```

#### Número de apps classificados como "Mature 17+":

Verificamos quantos aplicativos possuem classificação indicativa "Mature 17+".

```python
quantidade_mature = df[df['Content Rating'] == 'Mature 17+'].shape[0]
```

#### Top 10 apps por número de reviews:

Um gráfico de barras mostra os 10 aplicativos com mais avaliações.

```python
plt.bar(top_10_reviews['App'], top_10_reviews['Reviews'])
```

### 6. Outras Análises Gráficas 📈

Além dos gráficos já mencionados, criamos outras visualizações para analisar diferentes aspectos dos dados:

#### Dispersão entre Tamanho do Aplicativo e Número de Instalações:

Um gráfico de dispersão mostra a relação entre o tamanho do aplicativo e o número de instalações.

```python
plt.scatter(df['Size_MB'], df['Installs'])
```

#### Média de Avaliação por Gênero:

Visualizamos a média das avaliações por gênero de aplicativo através de um gráfico de linhas.

```python
plt.plot(media_avaliacao_por_genero['Genres'], media_avaliacao_por_genero['Rating'])
```


## 📈 Conclusão

Este projeto oferece uma análise detalhada dos aplicativos do Google Play Store, com diversas visualizações que facilitam a compreensão dos padrões e tendências dos aplicativos mais populares. Não deixe de explorar os gráficos interativos e tirar suas próprias conclusões! 😊


![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
