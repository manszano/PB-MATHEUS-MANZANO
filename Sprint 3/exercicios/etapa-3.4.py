from collections import Counter

def contar_aparicoes_filmes(csv):
    contagem_filmes = Counter()

    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]

        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            filme = colunas[4]  # Coluna '#1 Movie'
            contagem_filmes[filme] += 1

    return contagem_filmes

def escrever_resultados(contagem_filmes, caminho_saida):
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        for filme, quantidade in filmes_ordenados:
            arquivo_saida.write(f"O filme ({filme}) aparece {quantidade} vezes no dataset\n")

csv = 'actors.csv'
caminho_saida = 'resultados_filmes.txt'

contagem_filmes = contar_aparicoes_filmes(csv)
escrever_resultados(contagem_filmes, caminho_saida)
