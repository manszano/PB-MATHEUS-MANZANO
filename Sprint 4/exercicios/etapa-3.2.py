def calcular_media_receita_bilheteria(csv):
    total_receita = 0
    quantidade_atores = 0
    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]
        
        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            try:
                receita_bilheteria = float(colunas[5])
                total_receita += receita_bilheteria
                quantidade_atores += 1
            except ValueError:
                continue

    if quantidade_atores == 0:
        return 0
    else:
        return total_receita / quantidade_atores

def exibir_media_em_colunas(media_receita):
    largura_titulo = 30
    largura_valor = 15
    print(f"{'Média da Receita Bruta dos Principais Filmes'.ljust(largura_titulo)}{'Valor'.ljust(largura_valor)}")
    print("-" * (largura_titulo + largura_valor))
    print(f"{'Média por Ator/Atriz'.ljust(largura_titulo)}{f'${media_receita:.2f} milhões'.ljust(largura_valor)}")

csv = 'actors.csv'

media_receita = calcular_media_receita_bilheteria(csv)
exibir_media_em_colunas(media_receita)
