<div>
  <img src="https://github.com/user-attachments/assets/c2fd8287-fc6a-47a5-a634-f26610ab4b93" width="100%" alt="Banner">
</div>



## 📝 **Instruções/Informações/Anotações**

### **Objetivo da Sprint:**
Desenvolver um projeto de ETL utilizando Python para manipulação de dados a partir de arquivos CSV. O desafio envolve duas partes principais: processamento de dados do arquivo *actors.csv* e análise de dados do arquivo *googleplaystore.csv*.

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

---
## **Desafios**

Durante a sprint, realizamos dois desafios de ETL e análise de dados.

1. **Desafio 1: Processamento de ETL com actors.csv**  
   - **Objetivo:** Aplicar os fundamentos de ETL (Extract-Transform-Load) no arquivo `actors.csv` em 5 etapas distintas, armazenando as saídas em arquivos de texto.
   - **Etapas Realizadas:**  
     - Criação de 5 arquivos `.txt` (etapa-1.txt, etapa-2.txt, etc.) para armazenar as respostas de cada parte do processamento.
     - Leitura e extração de dados do arquivo `actors.csv`.
     - Transformação dos dados conforme as perguntas orientadoras.
     - Armazenamento das respostas obtidas nos respectivos arquivos.
   - **Resultado:** Todas as etapas foram concluídas, e as respostas foram salvas com sucesso.

2. **Desafio 2: Análise de Dados com googleplaystore.csv**  
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
![image](https://github.com/user-attachments/assets/f77c5741-c00d-4aa7-80a0-6734cd0800c9)

*Top 5 Apps por Número de Instalações*

**Evidência 2:**
![image](https://github.com/user-attachments/assets/67fafd3c-ff18-46c2-aa74-bdd01d05505d)

*Distribuição de Categorias de Apps*

**Evidência 3:**\
![image](https://github.com/user-attachments/assets/b172ce6d-f893-4742-8fbc-817183653f94)
*App mais caro*

**Evidência 4:**\
![image](https://github.com/user-attachments/assets/41c9d5e9-43a3-49e9-bc12-6a28783684b0)
*Apps são classificados como 'Mature 17+*

**Evidência 5:**\
![image](https://github.com/user-attachments/assets/dde35a22-9c31-4630-81c9-b99ab79a3449)
*Top 10 apps por número de reviews.*

*Evidência 6:**\
![image](https://github.com/user-attachments/assets/65423c09-a95d-4a95-8793-dd7eca8029e4)

*Cálculos sobre o dataset*

*Evidência 7:**\
![image](https://github.com/user-attachments/assets/460fdd9c-e350-4cac-9140-440e99c93eba)

*Top 10 Apps por Número de Reviews*

*Evidência 8:**\
![image](https://github.com/user-attachments/assets/e0976420-0a1f-44cc-aaf9-4490440d55ec)

*Dispersão entre Tamanho do Aplicativo*

*Evidência 9:**\
![image](https://github.com/user-attachments/assets/21b4169b-1ef7-4ad6-a1de-d3730356728c)

*Média de Avaliação por Gênero de Aplicativo*



---

## 🎓 **Certificados**

### **Certificados Conquistados Durante a Sprint:**
![image](https://github.com/user-attachments/assets/6f61eb74-0ab6-4ea4-8ca1-6f6d5af59fbc)
*Parceiros da AWS: Aspectos econômicos da nuvem (Portugues) | AWS Partner:
Cloud Economics (Portuguese)*

---

## 🎯 **Conclusão da Sprint**

Nesta sprint, concluímos com sucesso os objetivos propostos, enfrentamos desafios importantes e adquirimos novos conhecimentos, gostei do projeto e de sua estrutura e estou empolgado para as próximas Sprints!!

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)

