def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf'), #divisão por zero
        '%': lambda x, y: x % y
    }
    
    resultados = map(lambda op_ope: operacoes[op_ope[0]](op_ope[1][0], op_ope[1][1]), zip(operadores, operandos))
    return max(resultados)

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))