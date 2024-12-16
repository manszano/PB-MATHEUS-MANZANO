![edsafio](https://github.com/user-attachments/assets/ac9b0eef-4f9c-4e7a-a865-7041f48bbc93)

&nbsp;  
# 🎥 Transformação de Dados no AWS Glue

Este projeto tem como objetivo realizar a transformação e organização de dados em um Data Lake, utilizando o AWS Glue. Foram implementados dois jobs principais para leitura, transformação e particionamento de dados.

Para replicação, utilize o código Python fornecido, configurando suas credenciais e dependências no ambiente AWS Glue.

---

## 📂 Estrutura do Projeto

O projeto foi dividido em **duas etapas principais**, conforme descrito abaixo:

### 1. **Transformação de Dados CSV**

Nesta etapa, foi realizada a leitura de um arquivo CSV bruto da camada Raw do Data Lake, e os dados foram transformados e salvos na camada Trusted no formato Parquet. 

#### Código Python:
[proc-csv](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%208/desafio/proc-csv.py)
```python
import sys
from pyspark.sql import SparkSession

# Configuração da SparkSession
spark = SparkSession.builder.getOrCreate()

# Lendo argumentos
raw_path = sys.argv[1]  # Caminho da camada Raw
trusted_path = sys.argv[2]  # Caminho da camada Trusted

# Lendo os dados do CSV
df = spark.read.csv(raw_path, header=True)

# Escrevendo os dados transformados em Parquet na camada Trusted
df.write.mode("overwrite").parquet(trusted_path)
```

---

### 2. **Integração com API TMDB**

Nesta etapa, os dados obtidos da API TMDB foram processados, enriquecidos e particionados por data de execução. Os dados transformados foram salvos na camada Trusted, também no formato Parquet.

#### Código Python:
[proc-tmdb](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%208/desafio/proc-csv.py)
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

# Configuração da SparkSession
spark = SparkSession.builder.getOrCreate()

# Lendo argumentos
raw_path = sys.argv[1]  # Caminho da camada Raw (JSON)
trusted_path = sys.argv[2]  # Caminho da camada Trusted

# Lendo os dados JSON
df = spark.read.json(raw_path)

# Adicionando a coluna de partição pela data de execução
df = df.withColumn("partition_date", current_date())

# Escrevendo os dados particionados em Parquet na camada Trusted
df.write.mode("overwrite").partitionBy("partition_date").parquet(trusted_path)
```

---

## 📸 **Evidências**

### **Scripts Executados:**  
![etljobs](https://github.com/user-attachments/assets/d36d1fc1-52af-4762-8842-af201645f158)
&nbsp; 
_jobs_  

![proc-csv](https://github.com/user-attachments/assets/0d7dafbd-365e-4a2d-94d6-8ea5098923c7)
&nbsp; 
_proc csv job_
![proc-tmdb](https://github.com/user-attachments/assets/83d2d87d-20b4-4301-b341-a6c97f40dca3)
&nbsp; 
_proc tmbd job_
![job-parameters](https://github.com/user-attachments/assets/aa94cbb2-e8c6-4ec2-8c11-420f5bf8c75b)
&nbsp;
_parametros jobs_
&nbsp;
&nbsp; 
*A transformação foi executada com sucesso e os dados foram salvos conforme os padrões definidos.*

---

## 🎯 **Resultados**

### Caminhos ou Resultados Finais:
- **Transformação de CSV:** Dados armazenados no seguinte diretório:  
  `trusted/zone/csv_transform/<ano>/<mês>/<dia>/dados.parquet`
  
- **Integração com API TMDB:** Dados armazenados no seguinte diretório:  
  `trusted/zone/tmdb_api/<ano>/<mês>/<dia>/dados.parquet`
  
![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
