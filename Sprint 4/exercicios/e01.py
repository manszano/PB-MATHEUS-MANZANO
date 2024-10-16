caminho_arquivo = 'number.txt'
with open(caminho_arquivo, 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

top_5_pares = numeros_pares_ordenados[:5]

soma_top_5 = sum(top_5_pares)

print(top_5_pares)
print(soma_top_5)