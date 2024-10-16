<div>
  <img src="https://github.com/user-attachments/assets/c2fd8287-fc6a-47a5-a634-f26610ab4b93" width="100%" alt="Banner">
</div>

### Arquivos da sprint
[Desafio](https://github.com/manszano/PB-MATHEUS-MANZANO/tree/main/Sprint%203/desafio/Jupyter)
[Exercicios](https://github.com/manszano/PB-MATHEUS-MANZANO/tree/main/Sprint%203/exercicios)
[Evidências](https://github.com/manszano/PB-MATHEUS-MANZANO/tree/main/Sprint%203/evidencias)
[Certificados](https://github.com/manszano/PB-MATHEUS-MANZANO/tree/main/Sprint%203/certificados)


## 📝 **Instruções/Informações/Anotações**

### **Objetivo da Sprint:**
Desenvolver um projeto de Ánalise de dados utilizando Python para manipulação de dados a partir de arquivos CSV. O desafio envolve duas partes principais: processamento de dados do arquivo *actors.csv* e análise de dados do arquivo *googleplaystore.csv*.

- **Tarefas Realizadas:**  
  - **Processamento ETL do arquivo actors.csv:**
  - Utilizado python vanilla
    - Realizado em 5 etapas, cada uma armazenada em arquivos `.txt`, onde o conteúdo do arquivo CSV foi lido, transformado e analisado.
  - **Análise do arquivo googleplaystore.csv:**  
    - Limpeza de dados, remoção de duplicatas e criação de gráficos de visualização com as bibliotecas `Pandas` e `Matplotlib`.
  
### **Anotações Importantes:**
#### _Aprendizados:_

- **Tecnologias Utilizadas:** Python (`Pandas`, `Matplotlib`)
- **Desafios Enfrentados:**  
  - Manipulação direta de arquivos CSV e formatação correta dos dados para visualização.
  - Geração de gráficos que respeitem escalas corretas e tenham boa visibilidade, considerando as grandes quantidades de dados.
- **Soluções:**  
  - Utilização das bibliotecas `Pandas` para limpeza e manipulação dos dados.
  - Criação de gráficos com `Matplotlib`, aplicando técnicas para melhorar a legibilidade, como ajuste de escalas e espaçamento entre rótulos.

---
## **Exercícios**
Diretório: [Exercicios Udemy](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%203/exercicios/exercicios-udemy.py)
### E01
```python
nome = "MATHEUS"
idade = 14

para_100 = 100 - idade
ano_100 = 2024 + para_100

print(ano_100)
```

---
### E02
```python
numeros = []

for i in range(1, 4):
    numeros.append(i)

for numero in numeros:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Ímpar: {numero}")
```

---
### E03
```python
for numero in range(0, 21, 2):
    print(numero)
```

---
### E04
```python

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

for numero in range(1, 101):
    if primo(numero):
        print(numero)
```

---
### E05
```python
dia, mes, ano = 22, 10, 2022

print(f"{dia}/{mes}/{ano}")

```

---
### E06
```python
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

comum = list(set(a) & set(b))

print(comum)

```

---
### E07
```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impares = [numero for numero in a if numero % 2 != 0]

print(impares)
```

---
### E08
```python
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")

```

---
### E09
```python
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, primeiroNome in enumerate(primeirosNomes):
    print(f"{i} - {primeiroNome} {sobreNomes[i]} está com {idades[i]} anos")

```

---
### E10
```python
def remover_duplicados(lista):
    return list(set(lista))

lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_sem_duplicados = remover_duplicados(lista_teste)
print(lista_sem_duplicados)
 
```

---
### E11
```python
import json

with open('person.json', 'r', encoding='utf-8') as file:
    dados = json.load(file)

print(dados)
 
```

---
### E12
```python
def my_map(lista, f):
    return [f(x) for x in lista]

def potencia_de_2(x):
    return x ** 2
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(entrada, potencia_de_2)

print(resultado)
```

---
### E13
```python
with open('arquivo_texto.txt', 'r', encoding='utf-8') as file:
    for linha in file:
        print(linha, end='')
```

---
### E14
```python
def imprimir_parametros(*par, **par2):

    for num in par:
        print(str(num).strip())
    for key, value in par2.items():
        print(f"{value}")

imprimir_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
 
```

---
### E15
```python
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

```

---
### E16
```python
def soma_numeros(string_numeros: str) -> int:
    numeros = map(int, string_numeros.split(','))
    return sum(numeros)

string = "1,3,4,6,10,76"
resultado = soma_numeros(string)
print(resultado)
 
```

---
### E17
```python
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
 
```

---
### E18
```python
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
```

---
### E19
```python
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
```

---
### E20
```python
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
reversed_list = a[::-1]
print(reversed_list)
```

---
### E21
```python
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

```

---
### E22
```python
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
```

---
### E23
```python
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

```

---
### E24
```python
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

```

---
### E25
```python
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

```
## 📝 **Exercicios ETL**

Durante o desenvolvimento do desafio, segui as seguintes etapas para processar o arquivo `actors.csv` e obter as informações solicitadas.

### **Etapa 1: Ator/Atriz com Maior Número de Filmes**
- **Objetivo:** Apresentar o ator/atriz com o maior número de filmes e a respectiva quantidade de filmes.
- **Processamento:** 
  - A partir da coluna `Number of movies`, percorri o dataset para identificar qual ator ou atriz possuía o maior número de filmes.
  - O resultado foi o nome do ator/atriz com o maior número de participações, juntamente com a quantidade de filmes.
```python
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
```
---
### **Etapa 2: Média de Receita Bruta dos Principais Filmes**
- **Objetivo:** Calcular a média de receita bruta dos principais filmes considerando todos os atores.
- **Processamento:** 
  - Utilizei a coluna `Gross` para calcular a média de receita bruta entre todos os registros de filmes no dataset.
  - Esse valor representa o valor médio bruto arrecadado pelos principais filmes do conjunto de dados.
```python
def calcular_media_receita_bilheteria(csv):
    total_receita = 0
    quantidade_atores = 0
    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]
        
        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            try:
                receita_bilheteria = float(colunas[5])
                total_receita += receita_bilheteria
                quantidade_atores += 1
            except ValueError:
                continue

    if quantidade_atores == 0:
        return 0
    else:
        return total_receita / quantidade_atores

def exibir_media_em_colunas(media_receita):
    largura_titulo = 30
    largura_valor = 15
    print(f"{'Média da Receita Bruta dos Principais Filmes'.ljust(largura_titulo)}{'Valor'.ljust(largura_valor)}")
    print("-" * (largura_titulo + largura_valor))
    print(f"{'Média por Ator/Atriz'.ljust(largura_titulo)}{f'${media_receita:.2f} milhões'.ljust(largura_valor)}")

csv = 'actors.csv'

media_receita = calcular_media_receita_bilheteria(csv)
exibir_media_em_colunas(media_receita)
```
---
### **Etapa 3: Ator/Atriz com Maior Média de Receita Bruta por Filme**
- **Objetivo:** Identificar o ator ou atriz com a maior média de receita bruta por filme.
- **Processamento:** 
  - A partir da coluna `Average per Movie`, analisei o dataset para calcular a média de bilheteria por filme de cada ator.
  - Com esses dados, determinei qual ator/atriz possui a maior média de bilheteria entre todos os filmes que participou.
```python
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
```
---
### **Etapa 4: Contagem de Aparições dos Filmes de Maior Bilheteria**
- **Objetivo:** Contar as aparições dos filmes de maior bilheteria, presentes na coluna `#1 Movie`.
- **Processamento:** 
  - Realizei uma contagem de quantas vezes cada filme presente na coluna `#1 Movie` aparece no dataset.
  - Ordenei os resultados de forma decrescente pelo número de aparições e, em caso de empate, ordenei alfabeticamente pelo nome do filme.
```python
from collections import Counter

def contar_aparicoes_filmes(csv):
    contagem_filmes = Counter()

    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]

        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            filme = colunas[4]  # Coluna '#1 Movie'
            contagem_filmes[filme] += 1

    return contagem_filmes

def escrever_resultados(contagem_filmes, caminho_saida):
    filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        for filme, quantidade in filmes_ordenados:
            arquivo_saida.write(f"O filme ({filme}) aparece {quantidade} vezes no dataset\n")

csv = 'actors.csv'
caminho_saida = 'resultados_filmes.txt'

contagem_filmes = contar_aparicoes_filmes(csv)
escrever_resultados(contagem_filmes, caminho_saida)
```
- **Resultado:** O formato de saída foi "O filme (nome do filme) aparece (quantidade) vez(es) no dataset", e os resultados foram armazenados no arquivo `resultados_filmes.txt`.
---
### **Etapa 5: Lista de Atores Ordenada pela Receita Bruta de Seus Filmes**
- **Objetivo:** Apresentar a lista de atores ordenada pela receita bruta total de seus filmes.
- **Processamento:** 
  - Utilizei a coluna `Total Gross` para calcular a receita total bruta de todos os filmes de cada ator.
  - A lista de atores foi então ordenada em ordem decrescente com base na receita bruta total.
```python
def listar_atores_por_receita(csv):
    atores_receita = []

    with open(csv, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        cabecalho = linhas[0].strip().split(',')
        dados = linhas[1:]

        for linha in dados:
            colunas = [coluna.strip() for coluna in linha.split(',')]
            nome_ator = colunas[0]
            try:
                receita_total = float(colunas[1])  # Coluna 'Total Gross'
                atores_receita.append((nome_ator, receita_total))
            except ValueError:
                continue

    atores_receita_ordenados = sorted(atores_receita, key=lambda x: -x[1])

    return atores_receita_ordenados

def escrever_atores_receita(atores_receita_ordenados, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
        for ator, receita in atores_receita_ordenados:
            arquivo_saida.write(f"{ator} - ${receita:.2f} milhões\n")

csv = 'actors.csv'
caminho_saida = 'atores_por_receita.txt'

atores_receita_ordenados = listar_atores_por_receita(csv)
escrever_atores_receita(atores_receita_ordenados, caminho_saida)
```
- **Resultado:** O formato de saída foi "(nome do ator) - (receita total bruta)", e os resultados foram salvos no arquivo `atores_por_receita.txt`.

---
## **Desafio**

Durante a sprint, realizamos desafio em análise de dados.

1. **Desafio 1: Análise de Dados com googleplaystore.csv**  
   - **Objetivo:** Realizar a análise de dados do arquivo `googleplaystore.csv` utilizando as bibliotecas `Pandas` e `Matplotlib`.
   - **Atividades Realizadas:**  
     1. Leitura e remoção de duplicatas do dataset.
     2. Geração de um gráfico de barras com os top 5 apps por número de instalações.
     3. Criação de um gráfico de pizza mostrando a distribuição das categorias de apps.
     4. Identificação do app mais caro no dataset.
     5. Contagem de apps classificados como "Mature 17+".
     6. Exibição do top 10 apps por número de reviews, ordenados de forma decrescente.
     7. Cálculos adicionais: Média de avaliação por gênero e distribuição de tamanhos dos apps.
     8. Gráficos adcionais de disperção e linha.
   - **Resultado:** Todas as análises foram implementadas e os gráficos gerados com sucesso.


## 📸 **Evidências**

### **Resultados:**
Aqui estão as evidências do que foi realizado durante a sprint.

**Evidência 1:**\
![image](https://github.com/user-attachments/assets/627053ea-c0c5-4803-b7e0-29759e244cf2)
_execução da etapa 1 do desafio_

**Evidência 2:**\
![image](https://github.com/user-attachments/assets/4590fb56-b072-4abf-9667-6358110c6907)
_código hash etapa3_

**Evidência 3:**\
![image](https://github.com/user-attachments/assets/6c126e0d-1378-4743-86c4-8a70ed7b4b31)

_execução imagem etapa3_


---

## 🎓 **Certificados**

### **Certificados Conquistados Durante a Sprint:**
[13246_3_6280596_1729098232_AWS Course Completion Certificate.pdf](https://github.com/user-attachments/files/17400092/13246_3_6280596_1729098232_AWS.Course.Completion.Certificate.pdf)
*AWS Partner: Credenciamento (Técnico) (Português) | AWS Partner: Accreditation
(Technical) (Portuguese)*

---

## 🎯 **Conclusão da Sprint**

Nesta sprint, concluímos com sucesso os objetivos propostos, enfrentamos desafios importantes e adquirimos novos conhecimentos, gostei do projeto e de sua estrutura e estou empolgado para as próximas Sprints!!

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)

