import boto3
import pandas as pd
from io import BytesIO

bucket_name = 'manzano-bucket-sprint5'
object_name = 'ProuniRelatorioDadosAbertos2020.csv'
s3_client = boto3.client('s3',
    aws_access_key_id='ASIAX5ZI6K6J3S2LD6MH',
    aws_secret_access_key='DSb7KbRzjOxGtTQ0+NaFH5qfzAvdhYG41ZgMCGrz',
    aws_session_token = "IQoJb3JpZ2luX2VjEO7//////////wEaCXVzLWVhc3QtMSJIMEYCIQCtNYUXvMNAdkQOMvIBgc5QC4rzsXyO3fCD7ctIiU6IkQIhAOI96NIR8QkvEOJsXhMY7WeHG4eDurviFw+n/dEtnVmjKqMDCGcQABoMNTQ1MDA5ODUwMjU5IgxYR6n4ZLeA2uwWTPsqgANy4n5mcaAixRkKgQ58/R9KGJ0uOKVCKdriDmj3HyUAE8AaVWHwp3JFcqH4IcMOnYyR2Wu3DTk9tK7l2TdJ7TrccV4L63Enf36SUDjPK9S0RxDXfW5vyEPQgqDZ26nwVHRaUyvXN7NiWIihnDYAgQNUiiB6JCi3Gm7X2Mdh36SceCN7CQhQOlr9HJtDuU4j+zctacEHP2IVznZqEBzmWxCrYLPW93Rv+0odcieNUSKL+yGQv2ocY2RzlBUMH9YdYMT93qRVUSoA+Qv09d72/14nnOgriwg3C9tVa9t7v9lhl53z5gjmCrx6C6gjFfA3qrjHjEFYeUIbMJjMr53V8SaleGz0cpWK9HvgES6f3RWOtQai9sWBaLX4Ds0fSExPPy0CNuNRx37LGnm3Nt0qYXpVX9u+cSLZ9wJrcee94FZSAYxEgnBiEAGjpcFlQk2nQ/oP8ekQpgflOWpwQ9s6C90p9tlhkiHi7qsirlTVB9cwoy1tucg4mZf9H8AiqFJOLg0wiaiFuQY6pQHDOcT7qveD1VHM1DBMEgK5nXn7Ch6CM43C8h6JeUARRJuSSdneher5t3EtPHyBn4QajikabDUQrWSU8b+OPD46ya7y0vQRxZ79iBMSsOBgyH9dlOBC3D8/H5eJ5EIR62p7C/ijR5uJFq6ZUzP/S1Jyj2TEdionvssXeGU6KlgDfOpRY6EiXoNv+dp0nn64O6Wdyc4ef1UBtO+gTRteAez9q1HAcpQ=",
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