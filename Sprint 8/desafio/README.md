![header-image](#)

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
![evidencia](#)  
_A transformação foi executada com sucesso e os dados foram salvos conforme os padrões definidos._  

---

## 🎯 **Resultados**

### Caminhos ou Resultados Finais:
- **Transformação de CSV:** Dados armazenados no seguinte diretório:  
  `trusted/zone/csv_transform/<ano>/<mês>/<dia>/dados.parquet`
  
- **Integração com API TMDB:** Dados armazenados no seguinte diretório:  
  `trusted/zone/tmdb_api/<ano>/<mês>/<dia>/dados.parquet`

![footer-image](#)
