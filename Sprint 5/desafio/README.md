<div>
  <img src="https://github.com/user-attachments/assets/4a9d5922-a944-4f6e-8a6c-b07e44b00df2" width="100%" alt="Banner">
</div>

&nbsp;
# ☁️ Desafio de Manipulação de Dados com boto3 e Pandas

Neste projeto, realizamos o upload e manipulação de um dataset de dados do ProUni usando a biblioteca `boto3` para interagir com o Amazon S3 e `pandas` para as transformações no arquivo.

#Para replicação e execução do código, utilize o script Python com as credenciais configuradas no boto3 e o DataFrame resultante no pandas!

## 📂 Estrutura do Projeto

O projeto está dividido em várias etapas, conforme detalhado a seguir:

### 1. Upload do Arquivo para o Bucket S3

Neste primeiro passo, foi criado um bucket S3 e realizado o upload do arquivo `ProuniRelatorioDadosAbertos2020.csv` usando `boto3`.

#### Código Python para o Upload:

```python
import boto3

# Configuração do cliente S3
s3_client = boto3.client('s3',
    aws_access_key_id='SEU_ACCESS_KEY',
    aws_secret_access_key='SEU_SECRET_KEY',
    region_name='us-east-1'
)

# Nome do bucket e arquivo
bucket_name = "manzano-bucket-sprint5"
file_name = "ProuniRelatorioDadosAbertos2020.csv"

# Upload do arquivo
s3_client.upload_file(file_name, bucket_name, file_name)
```

### 2. Manipulação dos Dados com Pandas

Após o upload do arquivo, ele foi baixado do bucket S3, carregado em um DataFrame com `pandas`, e diversas operações de manipulação foram aplicadas.

#### Código Python para Manipulações:

```python
import pandas as pd

# Download do arquivo para leitura
s3_client.download_file(bucket_name, file_name, 'local_Prouni.csv')

# Carregar o arquivo em um DataFrame
df = pd.read_csv('local_Prouni.csv', delimiter=';', encoding='latin1')

# Aplicar filtros, funções de agregação e manipulações
df_filtrado = df[(df['TIPO_BOLSA'] == 'INTEGRAL') & (df['REGIAO_BENEFICIARIO'] == 'SUDESTE')]

# Funções de agregação
df_agg = df_filtrado.groupby('NOME_CURSO_BOLSA').agg(
    total_bolsas=('NOME_CURSO_BOLSA', 'count'),
    idade_media=('IDADE', 'mean')
).reset_index()

# Função condicional
df['MAIOR_30'] = df['IDADE'] >= 30

# Conversão de colunas
df['SEXO_MASCULINO'] = df['SEXO_BENEFICIARIO'].apply(lambda x: x == 'M')

# Função de data e string
df['ANO_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'], errors='coerce').dt.year
df['NOME_CURSO_BOLSA'] = df['NOME_CURSO_BOLSA'].str.upper()
```

### 3. Salvar e Recarregar o Arquivo Processado no S3

O DataFrame manipulado foi salvo em um novo arquivo CSV e enviado novamente ao bucket S3.

#### Código Python para o Salvamento:

```python
# Salvar o DataFrame processado em CSV
processed_file_name = "ProuniRelatorioProcessado.csv"
df.to_csv(processed_file_name, index=False)

# Upload do arquivo processado para o S3
s3_client.upload_file(processed_file_name, bucket_name, processed_file_name)
```

---

## 📸 **Evidências**

### **Resultados:**
Aqui estão as evidências do que foi realizado durante o desafio.

**Script executado:**\
<div>
  <img src="https://github.com/user-attachments/assets/aef6c17d-1ff6-41f7-813b-1072bced3acb" width="50%" alt="Upload do arquivo original para o bucket S3">
</div>
_Execução das manipulações e transformações no DataFrame_


**Bucket Desafio:**\
<div>
  <img src="https://github.com/user-attachments/assets/f1cc1002-34f5-4900-afe8-8bb16479de6e">
</div>
_Print do bucket S3_


---

<div>
  <img src="https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891" width="100%" alt="bottom">
</div>
