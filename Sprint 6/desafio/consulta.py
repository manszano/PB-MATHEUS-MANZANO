import boto3
import pandas as pd
from io import BytesIO

bucket_name = 'manzano-bucket-sprint5'
object_name = 'ProuniRelatorioDadosAbertos2020.csv'
s3_client = boto3.client('s3',
    aws_access_key_id='XXXX',
    aws_secret_access_key='XXXX',
    aws_session_token = "XXXX",
    region_name='us-east-1'
)
try:
    response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
    file_content = response['Body'].read()
    
    df = pd.read_csv(BytesIO(file_content), sep=';', encoding='latin1')

    df['DATA_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'], errors='coerce')

    if df['DATA_NASCIMENTO'].isnull().any():
        print("Data de Nascimento nula!")

    ano_atual = pd.Timestamp('today').year
    df['IDADE'] = ano_atual - df['DATA_NASCIMENTO'].dt.year

    df_filtrado = df[(df['TIPO_BOLSA'] == 'INTEGRAL') & (df['REGIAO_BENEFICIARIO'] == 'SUDESTE')]
    contagem_bolsas = df_filtrado['NOME_CURSO_BOLSA'].value_counts()
    media_idade = df_filtrado['IDADE'].mean()
    df['MAIOR_30'] = df['IDADE'].apply(lambda x: 'Sim' if x >= 30 else 'Não')
    df['SEXO_MASCULINO'] = df['SEXO_BENEFICIARIO'].apply(lambda x: True if x == 'M' else False)
    df['ANO_NASCIMENTO'] = df['DATA_NASCIMENTO'].dt.year
    df['NOME_CURSO_BOLSA'] = df['NOME_CURSO_BOLSA'].str.upper()

    processed_file_name = 'ProuniRelatorioProcessado.csv'
    df.to_csv(processed_file_name, index=False, encoding='latin1')
    s3_client.upload_file(processed_file_name, bucket_name, processed_file_name)
    print(f"Arquivo '{processed_file_name}' salvo e carregado com sucesso no bucket '{bucket_name}'.")

except Exception as e:
    print(f"Erro durante o processamento: {e}")
