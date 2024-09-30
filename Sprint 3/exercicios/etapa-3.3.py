def encontrar_ator_maior_media_receita(csv):
    maior_media_receita = 0
    ator_com_maior_media = ""

    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]
        
        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            try:
                media_receita = float(colunas[3])
                nome_ator = colunas[0]
                
                if media_receita > maior_media_receita:
                    maior_media_receita = media_receita
                    ator_com_maior_media = nome_ator
            except ValueError:
                continue

    return ator_com_maior_media, maior_media_receita

def exibir_ator_maior_media_em_colunas(ator, media_receita):
    largura_nome = 20
    largura_media = 15
    
    print(f"{'Ator/Atriz'.ljust(largura_nome)}{'Média de Receita por Filme'.ljust(largura_media)}")
    print("-" * (largura_nome + largura_media))
    print(f"{ator.ljust(largura_nome)}{f'${media_receita:.2f} milhões'.ljust(largura_media)}")

csv = 'actors.csv'

ator, media_receita = encontrar_ator_maior_media_receita(csv)
exibir_ator_maior_media_em_colunas(ator, media_receita)
