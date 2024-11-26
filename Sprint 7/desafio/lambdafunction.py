import json
import boto3
import os
from datetime import datetime
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = os.environ['chave']

movie = Movie()
s3_client = boto3.client('s3')
bucket1 = 'manzano-datalake'

def as_obj_to_dict(obj):
    if isinstance(obj, dict):
        return {k: as_obj_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [as_obj_to_dict(i) for i in obj]
    elif hasattr(obj, '__dict__'):
        return as_obj_to_dict(obj.__dict__)
    else:
        return obj

def lambda_handler(event, context):
    base_path = 'Raw/TMDB/JSON'
    today = datetime.utcnow().strftime('%Y/%m/%d')
    movies = movie.popular()

    movies_data = []
    for m in movies:
        movie_dict = as_obj_to_dict(m) 
        movies_data.append(movie_dict)

    grouped_data = [movies_data[i:i + 100] for i in range(0, len(movies_data), 100)]

    for index, group in enumerate(grouped_data):
        file_name = f"{base_path}/{today}/part-{index}.json"
        json_data = json.dumps(group, indent=4)
        s3_client.put_object(
            Bucket=bucket1,
            Key=file_name,
            Body=json_data,
            ContentType='application/json'
        )
        print(f"Arquivo {file_name} gravado com sucesso no bucket {bucket1}.")
    
    return {
        'statusCode': 200,
        'body': "Função executada com sucesso!"
    }
