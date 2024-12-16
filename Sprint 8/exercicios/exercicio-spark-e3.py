import random
import names
import os

random.seed(40)
qtd_nomes_unicos = 3008
qtd_nomes_aleatorios = 10000000

nomes_unicos = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")
nomes_aleatorios = [random.choice(nomes_unicos) for _ in range(qtd_nomes_aleatorios)]
nome_arquivo = "nomes_aleatorios.txt"
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_txt:
    for nome in nomes_aleatorios:
        arquivo_txt.write(f"{nome}\n")

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

os.system(f"head -n 10 {nome_arquivo}")
