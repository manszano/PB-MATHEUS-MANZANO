def maiores_que_media(conteudo):
    media = sum(conteudo.values()) / len(conteudo)
    produtos_acima_media = filter(lambda item: item[1] > media, conteudo.items())
    return sorted(produtos_acima_media, key=lambda item: item[1])

conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))