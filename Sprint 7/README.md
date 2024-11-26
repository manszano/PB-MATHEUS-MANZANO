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
## **Exercício: Contagem de Palavras no Spark**

### **Objetivo**
Contar a quantidade total de palavras no arquivo `README.md` carregado diretamente no Google Colab.

```python
from pyspark.sql import SparkSession

# Iniciar uma sessão Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Caminho do arquivo README.md
file_path = "README.md"

# Carregar o arquivo como RDD
rdd = spark.sparkContext.textFile(file_path)

# Contar o total de palavras
total_words = (
    rdd.flatMap(lambda line: line.split())  # Dividir em palavras
    .map(lambda word: 1)                   # Mapear cada palavra como 1
    .reduce(lambda a, b: a + b)            # Somar todas as ocorrências
)

# Exibir o total de palavras
print(f"Total de palavras: {total_words}")
```

---

<a id="desafio"></a>
## 🎯 **Desafio**

### Configuração e Execução

- **Criação do Bucket S3**: O bucket `manzano-datalake` foi criado para armazenar os arquivos JSON processados.
- **Configuração do Lambda**: A função Lambda foi criada e configurada com uma Layer contendo as bibliotecas `tmdbv3api` e `boto3`.

### **Evidências**
- Exercicio SPARK (realizado no collab)
  ![exerciciospark](https://github.com/user-attachments/assets/ecbd85c9-07a2-4866-93c2-b441f671f9eb)

- Os arquivos JSON foram gravados no bucket S3 no caminho especificado:
  ![S3](https://github.com/user-attachments/assets/8b880e0e-f3ff-4d4c-8266-7b21f74a50bd)
    ```
    Raw/TMDB/JSON/<ano>/<mês>/<dia>/part-<número>.json
    ```
- Script LAMBDA.
![LAMBDA](https://github.com/user-attachments/assets/650ffa9e-2b05-4e6d-91d6-9f5a9b65b62b)

- Política IAM LAMBDA.
![politica-iam](https://github.com/user-attachments/assets/3fd9cf8c-026b-4e58-ae61-4ae62023c435)
---


## 🎯 **Conclusão**

O desafio permitiu o aprendizado e aplicação prática de conceitos fundamentais em integração com APIs.
![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
