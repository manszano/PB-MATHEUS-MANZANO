import random

# Gerando uma lista com 250 inteiros aleatórios entre 1 e 1000
lista_inteiros = [random.randint(1, 1000) for _ in range(250)]

# Aplicando o método reverse
lista_inteiros.reverse()

# Imprimindo a lista invertida
print(lista_inteiros)
