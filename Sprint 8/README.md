![header-image](#)

<p align="center">
 <a href="#Sobre">Sobre</a> •
 <a href="#exercicio">Exercício</a> •
 <a href="#desafio">Desafio</a>
</p>

---

<a id="Sobre"></a>
## 📝 **Sobre**

### **Objetivo do Projeto**
Este projeto tem como objetivo aplicar técnicas de manipulação de dados e processamento distribuído utilizando Apache Spark. Os exercícios consistem em operações básicas com listas e manipulação de DataFrames, enquanto o desafio é implementado no AWS Glue para transformação e organização de dados em um Data Lake.

---

### **Tarefas Realizadas**
- **Exercício - Warm Up com Python**
  - Manipulação de listas.
  - Geração de arquivos CSV.
- **Exercício - Manipulação com Spark**
  - Operações com DataFrames no PySpark.
  - Integração de bibliotecas auxiliares.
- **Desafio - Processamento com Glue**
  - Transformação de dados da Raw Zone para a Trusted Zone.
  - Organização de dados no formato Parquet, particionados e integrados ao Glue Data Catalog.

---

<a id="exercicio"></a>
## **Exercício**

### **Objetivo**
Realizar manipulação de listas e DataFrames, criando soluções básicas em Python e Apache Spark.

---

### **Exercício 1: Manipulação de Listas**
```python
import random

# Declaração da lista com 250 números inteiros aleatórios
lista_numeros = random.sample(range(1, 1000), 250)

# Revertendo a lista
lista_numeros.reverse()

# Imprimindo o resultado
print(lista_numeros)
```

---

### **Exercício 2: Manipulação de Listas com Arquivos**
```python
# Lista com 20 nomes de animais
animais = ["Cachorro", "Gato", "Papagaio", "Pato", "Tartaruga", "Arara", "Leão", 
           "Tigre", "Elefante", "Cavalo", "Porco", "Macaco", "Lobo", "Veado", 
           "Ganso", "Cobra", "Raposa", "Onça", "Bicho-preguiça", "Capivara"]

# Ordenando e imprimindo os animais
animais.sort()
[print(animal) for animal in animais]

# Salvando em arquivo CSV
with open("animais.csv", "w") as file:
    for animal in animais:
        file.write(f"{animal}\n")
```

---

### **Exercício 3: Geração de Dataset de Nomes**
```python
import random
import names

# Definições iniciais
random.seed(40)
qtd_nomes_unicos = 3008
qtd_nomes_aleatorios = 10000000

# Gerando nomes únicos
nomes_unicos = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

# Gerando 10 milhões de nomes aleatórios
dados = [random.choice(nomes_unicos) for _ in range(qtd_nomes_aleatorios)]

# Salvando em arquivo
with open("nomes_aleatorios.txt", "w") as file:
    file.write("\n".join(dados))
```

---

### **Exercício 4: Manipulação com PySpark**
#### **Etapa 1: Configuração Inicial**
```python
from pyspark.sql import SparkSession

# Configurando a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)

# Visualizando os dados
df_nomes.show(5)
```

#### **Etapa 2: Renomear e Verificar Schema**
```python
# Renomeando a coluna
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Verificando o esquema
df_nomes.printSchema()
df_nomes.show(10)
```

#### **Etapas 3-5: Adicionando Colunas**
```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import random

# Funções UDF
escolaridade_udf = udf(lambda: random.choice(["Fundamental", "Medio", "Superior"]), StringType())
pais_udf = udf(lambda: random.choice(["Brasil", "Argentina", "Chile", "Colômbia", "Uruguai"]), StringType())
ano_nascimento_udf = udf(lambda: str(random.randint(1945, 2010)), StringType())

# Adicionando colunas
df_nomes = df_nomes.withColumn("Escolaridade", escolaridade_udf())
df_nomes = df_nomes.withColumn("Pais", pais_udf())
df_nomes = df_nomes.withColumn("AnoNascimento", ano_nascimento_udf())

df_nomes.show(10)
```

---

<a id="desafio"></a>
## 🎯 **Desafio**

### **Objetivo**
Transformar dados da camada RAW para a camada TRUSTED em um Data Lake utilizando o AWS Glue. 

---

### **Código do Job 1: CSV para Trusted Zone**
```python
import sys
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Lendo argumentos
raw_path = sys.argv[1]
trusted_path = sys.argv[2]

# Lendo CSV
df = spark.read.csv(raw_path, header=True)

# Salvando como Parquet
df.write.mode("overwrite").parquet(trusted_path)
```

---

### **Código do Job 2: API TMDB para Trusted Zone**
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder.getOrCreate()

# Lendo argumentos
raw_path = sys.argv[1]
trusted_path = sys.argv[2]

# Lendo JSON
df = spark.read.json(raw_path)

# Particionando e salvando
df = df.withColumn("partition_date", current_date())
df.write.mode("overwrite").partitionBy("partition_date").parquet(trusted_path)
```

---

## 🎯 **Conclusão**
Os exercícios e o desafio mostraram como manipular dados de maneira eficiente em Python e Spark. A implementação no AWS Glue permite escalar o processamento em um ambiente distribuído.

![footer-image](#)
