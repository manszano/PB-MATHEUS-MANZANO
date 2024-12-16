import random

import csv

animais = [
    "Cachorro", "Gato", "Papagaio", "Elefante", "Zebra",
    "Leão", "Tigre", "Urso", "Raposa", "Lobo",
    "Cavalo", "Jacaré", "Tartaruga", "Pinguim", "Coelho",
    "Cobra", "Águia", "Tubarão", "Golfinho", "Girafa"
]

animais.sort()
[print(animal) for animal in animais]

with open('animais.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for animal in animais:
        escritor_csv.writerow([animal])

print("Arquivo 'animais.csv' criado com sucesso")

