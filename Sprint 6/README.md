<div>
  <img src="https://github.com/user-attachments/assets/9a2399c2-09f5-406d-8094-e1f2fa56d06e">
</div>

<br> 

<p align="center">
 <a href="#Sobre">Sobre</a> •
 <a href="#ex">Exercicío</a> •
 <a href="#desafio">Desafio</a> •
 <a href="#Certificados">Exercícios Docker</a>
</p>

---

<a id="Sobre"></a>
## 📝 **Sobre**

### **Objetivo da Sprint**
Desenvolver um projeto em Python para manipulação e análise de dados do Prouni, integrando armazenamento em nuvem com AWS S3 via `boto3`.

---

### **Tarefas Realizadas**

- **Upload para o S3**
  - Carregado o arquivo original `ProuniRelatorioDadosAbertos2020.csv` para um bucket S3.
  - Utilizada a biblioteca `boto3` para configurar o cliente e realizar o upload do arquivo.

- **Manipulação de Dados**
  - Carregado o arquivo do bucket S3 para um DataFrame com `pandas`.
  - Realizadas as seguintes operações no DataFrame:
    - **Filtro com múltiplos operadores lógicos:** Seleção de bolsas do tipo integral na região Sudeste.
    - **Funções de agregação:** Contagem de bolsas por curso e cálculo da média de idade dos beneficiários.
    - **Funções condicionais:** Criação da coluna `MAIOR_30`, indicando se o beneficiário possui 30 anos ou mais.
    - **Conversão de colunas:** Criação da coluna `SEXO_MASCULINO`, com valores booleanos para sexo masculino.
    - **Funções de manipulação de data:** Conversão de `DATA_NASCIMENTO` para o ano de nascimento.
    - **Funções de string:** Transformação dos nomes dos cursos para letras maiúsculas.

- **Salvamento e Upload do Arquivo Processado**
  - O DataFrame manipulado foi salvo localmente como `ProuniRelatorioProcessado.csv`.
  - O arquivo processado foi enviado de volta ao bucket S3 para armazenamento final.

---

### **Anotações Importantes**

#### _Aprendizados_

- Configuração do cliente `boto3` para operações de upload e download em buckets S3.
- Manipulação de dados com `pandas`, incluindo operações de filtro, agregação e transformação de strings e datas.
- Importância de definir o encoding correto ao carregar arquivos CSV para evitar problemas de decodificação.

#### _Tecnologias Utilizadas_

- Python 3.12
- pandas
- boto3 (integração com AWS S3)

---

### **Desafios Enfrentados e Soluções**

- **Problemas de Encoding**
  - **Desafio:** Erros de decodificação devido ao encoding incompatível (UTF-8) do CSV.
  - **Solução:** Utilização do encoding `latin1`, compatível com caracteres acentuados em português.

- **Manipulação de Datas com Valores Nulos**
  - **Desafio:** Valores nulos ao calcular idades, devido a dados de nascimento inválidos.
  - **Solução:** Uso do parâmetro `errors='coerce'` para converter valores inválidos em `NaT` (valores nulos).

- **Tratamento de Dados de Data e String**
  - **Desafio:** Necessidade de extração e transformação de colunas de data e texto.
  - **Solução:** Aplicação de funções de `pandas` para manipulação de strings e extração de dados de data, mantendo a consistência no DataFrame.

---

<a id="ex"></a>
## **Exercicío: Configuração de Bucket S3 para Hospedagem de Site Estático**

Para configurar o Amazon S3 como um servidor de hospedagem de site estático, foram seguidas as etapas abaixo. Esse processo permitiu armazenar e disponibilizar arquivos de forma pública, acessíveis através de um endpoint de site gerado pelo S3.

### **Etapas Realizadas**

- **Etapa 1:** Criar um Bucket
  - Criado um bucket no S3 (_manzano.bucket.com_) para armazenar os arquivos do site.

- **Etapa 2:** Habilitar Hospedagem de Site Estático
  - Nas configurações do bucket, habilitada a opção de "Hospedagem de site estático", permitindo que o bucket sirva páginas web.

- **Etapa 3:** Editar Configurações de Bloqueio de Acesso Público
  - Modificadas as configurações para desativar o bloqueio de acesso público, habilitando o bucket para acesso público.

- **Etapa 4:** Adicionar Política de Bucket para Acesso Público
  - Adicionada uma política de bucket para tornar todo o conteúdo do bucket acessível publicamente. Essa política permite que qualquer usuário acesse os arquivos armazenados.

- **Etapa 5:** Configurar Documento de Índice
  - Definido um arquivo HTML: [index.html](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%205/exercicios/index.html), como o documento de índice, para que o site mostre essa página inicial automaticamente ao ser acessado.

- **Etapa 6:** Configurar Documento CSV
  - Configurado um documento csv: [nomes.csv](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%205/exercicios/nomes.csv) para pode ser efetuado do download.

- **Etapa 7:** Testar o Endpoint do Site
  - O endpoint gerado pelo S3 foi testado e é o seguinte: _http://manzano.bucket.com.s3-website-us-east-1.amazonaws.com/_.

### **Considerações Finais e evidências**

Essas configurações permitiu que o bucket em questão (_manzano.bucket.com_) sirva como uma hospedagem estática simples.

![bucket-site-estático](https://github.com/user-attachments/assets/64d291b9-79a7-410f-a3f5-911f00344e5e)
![site-estático](https://github.com/user-attachments/assets/20650125-2d97-40c9-b16d-0ce0e8b5416f)

---

<a id="desafio"></a>
## 🎯 **Desafio**

### Etapa 1: Upload do Arquivo para o Bucket S3

Para iniciar o desafio, foi criado um bucket S3 e realizado o upload do arquivo `ProuniRelatorioDadosAbertos2020.csv` com a biblioteca `boto3`.
Arquivo em questão: [Arquivo.py](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%205/desafio/consulta.py)
```python
import boto3

# Configuração do cliente S3
s3_client = boto3.client('s3',
    aws_access_key_id='XXXX',
    aws_secret_access_key='XXXX',
 aws_session_token = "XXXXXX",
    region_name='us-east-1'
)

# Nome do bucket e arquivo
bucket_name = "manzano-bucket-sprint5"
file_name = "ProuniRelatorioDadosAbertos2020.csv"

# Upload do arquivo
s3_client.upload_file(file_name, bucket_name, file_name)
```

### Etapa 2: Manipulação dos Dados com Pandas

Após o upload do arquivo, ele foi baixado do bucket S3, carregado em um DataFrame `pandas` e submetido a várias operações de manipulação.

```python
import pandas as pd

# Download do arquivo para leitura
    response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
    file_content = response['Body'].read()

# Carregar o arquivo em um DataFrame
df = pd.read_csv('local_Prouni.csv', delimiter=';', encoding='latin1')

# Aplicar manipulação de datas
df['DATA_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'], errors='coerce')

if df['DATA_NASCIMENTO'].isnull().any():
  print("Data de Nascimento nula!")

# Aplicar filtros, funções de agregação e manipulações
ano_atual = pd.Timestamp('today').year
df['IDADE'] = ano_atual - df['DATA_NASCIMENTO'].dt.year

df_filtrado = df[(df['TIPO_BOLSA'] == 'INTEGRAL') & (df['REGIAO_BENEFICIARIO'] == 'SUDESTE')]
contagem_bolsas = df_filtrado['NOME_CURSO_BOLSA'].value_counts()
media_idade = df_filtrado['IDADE'].mean()
df['MAIOR_30'] = df['IDADE'].apply(lambda x: 'Sim' if x >= 30 else 'Não')
df['SEXO_MASCULINO'] = df['SEXO_BENEFICIARIO'].apply(lambda x: True if x == 'M' else False)
df['ANO_NASCIMENTO'] = df['DATA_NASCIMENTO'].dt.year
df['NOME_CURSO_BOLSA'] = df['NOME_CURSO_BOLSA'].str.upper()

```

### Etapa 3: Salvar e Recarregar o Arquivo Processado no S3

O DataFrame manipulado foi salvo em um novo arquivo CSV e enviado novamente ao bucket S3.

```python
# Salvar o DataFrame processado em CSV e Upload no S3
processed_file_name = 'ProuniRelatorioProcessado.csv'
df.to_csv(processed_file_name, index=False, encoding='latin1')
s3_client.upload_file(processed_file_name, bucket_name, processed_file_name)
print(f"Arquivo '{processed_file_name}' salvo e carregado com sucesso no bucket '{bucket_name}'.")
```
### **Considerações Finais e evidências**

Com isso foi possível utilzar a api da AWS para fazer alterações em um bucket do S3.
![bucket-desafio](https://github.com/user-attachments/assets/b50642a8-3a45-45ac-a3e1-0b14dfe26377)
![execução-aws](https://github.com/user-attachments/assets/b657dbee-6356-4620-b29e-4c05ad51f1ac)

---

<a id="Certificados"></a>
## 🎓 **Certificados**

### **Certificados Conquistados Durante a Sprint:**
![Cloud-Quest](https://github.com/user-attachments/assets/654e64f4-daa8-4613-9a4e-b8176e26716f)

*AWS Cloud Quest: Cloud Practitioner*


## 🎯 **Conclusão da Sprint**

Nesta sprint, concluímos com sucesso os objetivos propostos, enfrentamos desafios importantes e adquirimos novos conhecimentos, gostei de aprender sobre AWS e de sua estrutura e estou empolgado para as próximas Sprints!!

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
