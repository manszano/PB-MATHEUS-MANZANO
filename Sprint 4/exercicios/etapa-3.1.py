def encontrar_ator_maior_numero_filmes(csv):
    maior_numero_filmes = 0
    ator_com_mais_filmes = ""

    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]
        
        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            nome_ator = colunas[0]
            try:
                numero_filmes = int(colunas[2])
            except ValueError:
                continue
            
            if numero_filmes > maior_numero_filmes:
                maior_numero_filmes = numero_filmes
                ator_com_mais_filmes = nome_ator

    return ator_com_mais_filmes, maior_numero_filmes

def exibir_em_colunas(ator, numero_filmes):
    largura_nome = 20
    largura_filmes = 10
    
    print(f"{'Ator/Atriz'.ljust(largura_nome)}{'Número de Filmes'.ljust(largura_filmes)}")
    print("-" * (largura_nome + largura_filmes))
    print(f"{ator.ljust(largura_nome)}{str(numero_filmes).ljust(largura_filmes)}")

csv = 'actors.csv'

ator, quantidade_filmes = encontrar_ator_maior_numero_filmes(csv)
exibir_em_colunas(ator, quantidade_filmes)
