![sprint7](https://github.com/user-attachments/assets/c256f579-2633-499d-b540-84ad7b021c89)


&nbsp;
# 🎥 Integração TMDB e AWS S3 com Lambda

Este projeto implementa uma função **AWS Lambda** para consumir a API TMDB, coletar informações sobre filmes populares e armazená-las no **Amazon S3** no formato JSON.

#Para replicação, utilize o código Python fornecido, configurando suas credenciais e dependências.

---

## 📂 Estrutura do Projeto

O projeto foi dividido em **três etapas principais**, conforme descrito abaixo:

### 1. Consumo da API TMDB



Nesta etapa, conectamos à API TMDB usando a biblioteca `tmdbv3api` para obter os dados de filmes populares.

#### Código Python para Consumo:

```python
from tmdbv3api import TMDb, Movie

# Configuração da API TMDB
tmdb = TMDb()
tmdb.api_key = 'SUA_API_KEY'  # Insira sua chave da API TMDB
movie = Movie()

# Coleta de filmes populares
movies = movie.popular()
print(f"Total de filmes populares obtidos: {len(movies)}")
```
[script completo](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%207/desafio/lambdafunction.py)
---

### 2. Processamento e Upload para o S3

Os dados dos filmes foram agrupados em lotes de 100 registros, convertidos para JSON e enviados ao **bucket S3**. O caminho de armazenamento segue o padrão:
`Raw/TMDB/JSON/<ano>/<mês>/<dia>/part-0.json`

#### Código Python para o Upload:

```python
import boto3
import json
from datetime import datetime

# Configuração do cliente S3
s3_client = boto3.client('s3')
bucket_name = 'manzano-datalake'

# Configuração do caminho base
base_path = 'Raw/TMDB/JSON'
today = datetime.utcnow().strftime('%Y/%m/%d')

# Agrupando e salvando filmes em JSON
grouped_data = [movies[i:i+100] for i in range(0, len(movies), 100)]

for index, group in enumerate(grouped_data):
    file_name = f"{base_path}/{today}/part-{index}.json"
    json_data = json.dumps([m.__dict__ for m in group], indent=4)
    
    # Upload para o S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json_data,
        ContentType='application/json'
    )
    print(f"Arquivo {file_name} carregado com sucesso no bucket {bucket_name}.")
```
[script completo](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%207/desafio/lambdafunction.py)
---

### 3. Execução no AWS Lambda

A lógica foi implementada em uma função Lambda, com dependências gerenciadas por **Layers**, para realizar todo o processo automaticamente.

#### Código Completo da Função Lambda:

```python
import boto3
import json
from datetime import datetime
from tmdbv3api import TMDb, Movie

def lambda_handler(event, context):
    # Configuração
    tmdb = TMDb()
    tmdb.api_key = 'SUA_API_KEY'
    movie = Movie()
    s3_client = boto3.client('s3')
    bucket_name = 'manzano-datalake'
    base_path = 'Raw/TMDB/JSON'
    today = datetime.utcnow().strftime('%Y/%m/%d')
    
    # Coleta de filmes populares
    movies = movie.popular()
    grouped_data = [movies[i:i+100] for i in range(0, len(movies), 100)]
    
    for index, group in enumerate(grouped_data):
        file_name = f"{base_path}/{today}/part-{index}.json"
        json_data = json.dumps([m.__dict__ for m in group], indent=4)
        
        # Upload para o S3
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json_data,
            ContentType='application/json'
        )
        print(f"Arquivo {file_name} gravado com sucesso.")
    
    return {
        'statusCode': 200,
        'body': "Função Lambda executada com sucesso!"
    }
```
[script completo](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%207/desafio/lambdafunction.py)
---

## 📸 **Evidências**


### **Scripts Executados:**
![LAMBDA](https://github.com/user-attachments/assets/d06a4a0c-32b7-4d24-a2af-5be200f57cb5)
_Função Lambda realizando upload dos arquivos JSON_

---

## 🎯 **Resultados**

### Caminhos no Bucket S3:

- Os arquivos foram armazenados no bucket `manzano-datalake` nos seguintes diretórios:
  `Raw/TMDB/JSON/<ano>/<mês>/<dia>/part-0.json`

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
