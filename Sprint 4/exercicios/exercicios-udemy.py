with open('arquivo_texto.txt', 'r', encoding='utf-8') as file:
    for linha in file:
        print(linha, end='')
# E14
def imprimir_parametros(*par, **par2):

    for num in par:
        print(str(num).strip())
    for key, value in par2.items():
        print(f"{value}")

imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
 
# E15
class Lampada:
    def __init__(self, ligada: bool):
        self.ligada = ligada  

    def liga(self):
        self.ligada = True 

    def desliga(self):
        self.ligada = False 

    def esta_ligada(self) -> bool:
        return self.ligada  



lampada = Lampada(False)  

lampada.liga()
print(f"A lâmpada está ligada? {lampada.esta_ligada()}") 


lampada.desliga()
print(f"A lâmpada ainda está ligada? {lampada.esta_ligada()}")
# E16
def soma_numeros(string_numeros: str) -> int:
    numeros = map(int, string_numeros.split(','))
    return sum(numeros)

string = "1,3,4,6,10,76"
resultado = soma_numeros(string)
print(resultado)
 
# E17
def dividir_lista_em_tres(lista):
    tamanho = len(lista) // 3
    parte1 = lista[:tamanho]
    parte2 = lista[tamanho:tamanho * 2]
    parte3 = lista[tamanho * 2:]
    # Formata a saída como uma string
    return f"{parte1} {parte2} {parte3}"

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
resultado = dividir_lista_em_tres(lista)
print(resultado)
 
# E18
speed = {
    'jan': 47, 
    'feb': 52, 
    'march': 47, 
    'April': 44, 
    'May': 52, 
    'June': 53, 
    'july': 54, 
    'Aug': 44, 
    'Sept': 54
}

valores_unicos = list(set(speed.values()))

print(valores_unicos)  
# E19
import random 

random_list = random.sample(range(500), 50)

sorted_list = sorted(random_list)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

n = len(sorted_list)
if n % 2 == 0:
    mediana = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
else:
    mediana = sorted_list[n // 2]

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
# E20
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
reversed_list = a[::-1]
print(reversed_list)
# E21
class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse.")


class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

pato = Pato()
pardal = Pardal()

print("Pato")
pato.voar()
pato.emitir_som()

print("Pardal")
pardal.voar()
pardal.emitir_som()
# E22
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = ""

    @property
    def nome(self):
        return self.__nome  

    @nome.setter
    def nome(self, valor):
        self.__nome = valor 


pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)  
# E23
class Calculo:
    def somar(self, x, y):
        return x + y  # Retorna a soma de x e y

    def subtrair(self, x, y):
        return x - y  # Retorna a subtração de x e y


# Valores para teste
x = 4
y = 5

# Criando uma instância da classe Calculo
calculo = Calculo()

# Calculando a soma e a subtração
soma = calculo.somar(x, y)
subtracao = calculo.subtrair(x, y)

# Imprimindo os resultados
print(f"Somando: {x}+{y} = {soma}")
print(f"Subtraindo: {x}-{y} = {subtracao}")
# E24
class Ordenadora:
    def __init__(self, lista_baguncada):
        self.listaBaguncada = lista_baguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)  

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)  



crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])


resultado_crescente = crescente.ordenacaoCrescente()
resultado_decrescente = decrescente.ordenacaoDecrescente()

print(resultado_crescente) 
print(resultado_decrescente)  
# E25
class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"  


avioes = [
    Aviao("BOIENG456", "1500 km/h", 400),
    Aviao("Embraer Praetor 600", "863 km/h", 14),
    Aviao("Antonov An-2", "258 km/h", 12)
]

for aviao in avioes:
    print(f"O avião de modelo \"{aviao.modelo}\" possui uma velocidade máxima de \"{aviao.velocidade_maxima}\", "
          f"capacidade para \"{aviao.capacidade}\" passageiros e é da cor \"{aviao.cor}\".")