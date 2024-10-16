def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    def processar_linha(linha):
        partes = linha.strip().split(',')
        nome = partes[0]
        notas = sorted(map(int, partes[1:]), reverse=True)[:3]
        media = round(sum(notas) / 3, 2)
        return f"Nome: {nome} Notas: {notas} Média: {media}"

    # Ordenar os estudantes por nome e processar as informações
    resultado = sorted(map(processar_linha, linhas))

    for linha in resultado:
        print(linha)

caminho_arquivo = 'estudantes.csv'
processar_arquivo(caminho_arquivo)