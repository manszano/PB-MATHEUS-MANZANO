def listar_atores_por_receita(csv):
    atores_receita = []

    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]

        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            nome_ator = colunas[0]
            try:
                receita_total = float(colunas[1])  # Coluna 'Total Gross'
                atores_receita.append((nome_ator, receita_total))
            except ValueError:
                continue

    atores_receita_ordenados = sorted(atores_receita, key=lambda x: -x[1])

    return atores_receita_ordenados

def escrever_atores_receita(atores_receita_ordenados, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        for ator, receita in atores_receita_ordenados:
            arquivo_saida.write(f"{ator} - ${receita:.2f} milhões\n")

csv = 'actors.csv'
caminho_saida = 'atores_por_receita.txt'

atores_receita_ordenados = listar_atores_por_receita(csv)
escrever_atores_receita(atores_receita_ordenados, caminho_saida)
