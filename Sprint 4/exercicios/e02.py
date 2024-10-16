def conta_vogais(texto):
    return len(list(filter(lambda x: x.lower() in 'aeiou', texto)))

print(conta_vogais("teste"))