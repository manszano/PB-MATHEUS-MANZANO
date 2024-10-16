from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda lanc: lanc[0] if lanc[1] == 'C' else -lanc[0], lancamentos)
    return reduce(lambda saldo, valor: saldo + valor, valores)

lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))