![sprint7main](https://github.com/user-attachments/assets/68cbba14-fc36-43fe-af30-e0328461388a)
<p align="center">
 <a href="#Sobre">Sobre</a> •
 <a href="#exercicio">Exercício</a> •
 <a href="#desafio">Desafio</a>
</p>

---

<a id="Sobre"></a>
## 📝 **Sobre**

### **Objetivo do Projeto**
Criar uma função **AWS Lambda** que consuma a API TMDB para coletar informações de filmes populares e salve os dados em um bucket S3 da AWS no formato JSON, utilizando bibliotecas como `tmdbv3api` e `boto3`.

---

### **Tarefas Realizadas**

- **Consumo da API TMDB**
  - Conexão com a API TMDB utilizando a biblioteca `tmdbv3api`.
  - Recuperação de filmes populares via método `movie.popular()`.

- **Manipulação de Dados**
  - Dados agrupados em lotes de 100 registros para facilitar o processamento.
  - Conversão dos objetos da API em JSON.

- **Integração com S3**
  - Upload dos arquivos JSON para um bucket S3 no formato especificado:
    ```
    Raw/TMDB/JSON/<ano>/<mês>/<dia>/part-<número>.json
    ```

- **Configuração de Permissões**
  - Definição de permissões adequadas para que a função Lambda consiga realizar operações no bucket S3.

---

<a id="exercicio"></a>
## **Exercício: Código Implementado no Colab**

O código abaixo foi utilizado para implementar a solução no ambiente de desenvolvimento.

```python
import json
import boto3
import os
from datetime import datetime
from tmdbv3api import TMDb, Movie

# Configuração da API TMDB
tmdb = TMDb()
tmdb.api_key = os.environ['chave']  # Substituir por sua chave TMDB
movie = Movie()

# Configuração do cliente S3
s3_client = boto3.client('s3')
bucket_name = 'manzano-datalake'

def lambda_handler(event, context):
    base_path = 'Raw/TMDB/JSON'
    today = datetime.utcnow().strftime('%Y/%m/%d')
    movies = movie.popular()
    
    # Agrupando dados em lotes de 100
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
        print(f"Arquivo {file_name} gravado com sucesso no bucket {bucket_name}.")
    
    return {
        'statusCode': 200,
        'body': "Função executada com sucesso!"
    }
```

### **Considerações Importantes**

#### _Aprendizados_

- Conexão com a API TMDB utilizando a biblioteca `tmdbv3api`.
- Manipulação e serialização de objetos Python em JSON.
- Operações com o S3 via `boto3`, incluindo upload e configuração de permissões.

#### _Tecnologias Utilizadas_

- Python 3.9
- tmdbv3api
- boto3 (integração com AWS S3)

---

<a id="desafio"></a>
## 🎯 **Desafio**

### Configuração e Execução

- **Criação do Bucket S3**: O bucket `manzano-datalake` foi criado para armazenar os arquivos JSON processados.
- **Configuração do Lambda**: A função Lambda foi criada e configurada com uma Layer contendo as bibliotecas `tmdbv3api` e `boto3`.

### **Evidências**

- Os arquivos JSON foram gravados no bucket S3 no caminho especificado:
    ```
    Raw/TMDB/JSON/<ano>/<mês>/<dia>/part-<número>.json
    ```
- Logs confirmam o sucesso da operação.

---

## 🎯 **Conclusão**

O desafio permitiu o aprendizado e aplicação prática de conceitos fundamentais em integração com APIs, manipulação de dados e serviços em nuvem como o AWS Lambda e S3. Foi um exercício enriquecedor para consolidar habilidades em desenvolvimento e DevOps.
