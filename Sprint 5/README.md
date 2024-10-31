<div>
  <img src="https://github.com/user-attachments/assets/9a2399c2-09f5-406d-8094-e1f2fa56d06e">
</div>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#Relatórios">Relatórios</a> •
 <a href="#exercicios-p">Exercícios Python</a> •
 <a href="#exercicios-d">Exercícios Docker</a> •
 <a href="#Certificados">Certificados</a>
</p>

## 📝 **Instruções/Informações/Anotações**

### **Objetivo da Sprint:**
Desenvolver um projeto Docker para execução de scripts Python.

- **Tarefas Realizadas:**  
  - **Docker:**
    - Criada uma imagem Docker para executar o script `carguru.py`.
    - Utilizado Python 3.9 como base da imagem.
    - Gerado o `Dockerfile` com as instruções para copiar e executar o script no container.
  - **Docker - Reutilização de Containers:**
    - Demonstrado como reutilizar containers parados, reiniciando containers existentes.
  - **Docker - Interação com Container:**
    - Criado um novo script Python que recebe uma string, gera um hash SHA-1, e imprime o resultado.
    - Criada uma nova imagem Docker chamada `mascarar-dados` para executar o script com interação via terminal.

### **Anotações Importantes:**
#### _Aprendizados:_

- Como criar e configurar imagens Docker usando `Dockerfile`.
- Como reutilizar containers no Docker e a importância de nomes únicos para containers.
- Como permitir a interação do usuário com containers em execução.

- **Tecnologias Utilizadas:**
  - Docker
  - Python 3.9
  - Algoritmo de hash SHA-1

- **Desafios Enfrentados:**  
  - Conflito de nomes ao tentar criar containers com o mesmo nome.
  - Manuseio de containers interativos com Docker.

- **Soluções:**  
  - Utilizar `docker rm` para remover containers antigos, ou renomeá-los para evitar conflitos.
  - Usar o parâmetro `-it` ao rodar containers para permitir interação com o terminal.

---
## **Exercícios**

Diretório: [Exercícios Docker](#) 

### E01
```python
caminho_arquivo = 'number.txt'
with open(caminho_arquivo, 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines()))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

top_5_pares = numeros_pares_ordenados[:5]

soma_top_5 = sum(top_5_pares)

print(top_5_pares)
print(soma_top_5)
```

---

### E02
```python
def conta_vogais(texto):
    return len(list(filter(lambda x: x.lower() in 'aeiou', texto)))

print(conta_vogais("teste"))
```
---

### E03
```python
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

```
---

### E04
```python
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

```
---

### E05
```python
def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    def processar_linha(linha):
        partes = linha.strip().split(',')
        nome = partes[0]
        notas = sorted(map(int, partes[1:]), reverse=True)[:3]
        media = round(sum(notas) / 3, 2)
        return f"Nome: {nome} Notas: {notas} Média: {media}"

    # Ordenar os estudantes por nome e processar as informações
    resultado = sorted(map(processar_linha, linhas))

    for linha in resultado:
        print(linha)

caminho_arquivo = 'estudantes.csv'
processar_arquivo(caminho_arquivo)
```
---

### E06
```python
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

```
---

### E07
```python
def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i

for par in pares_ate(10):
    print(par)
```

## 🎯 **Desafio**

Diretório: [Desafio](#) 

### Etapa 1: Criar Imagem Docker com `carguru.py`

```dockerfile
# Dockerfile para criar a imagem do script carguru.py
FROM python:3.9
WORKDIR /app
COPY carguru.py .
CMD ["python", "carguru.py"]
```
### Comandos para construir e executar:
```bash
# Construir a imagem Docker
docker build -t carguru-image .

# Rodar o container com o script
docker run --name carguru-container carguru-image
```

### Etapa 2: Reutilizar Containers
Reutilizar containers parados:

```bash
docker start carguru-container
```
Remover containers antigos:

```bash
docker rm carguru-container
```
### Etapa 3: Criar Script Interativo e Imagem Docker

```python
# hash_generator.py
import hashlib

while True:
    string = input("Digite uma string para gerar o hash (ou 'sair' para encerrar): ")
    if string.lower() == 'sair':
        break
    
    hash_object = hashlib.sha1(string.encode())
    print("Hash SHA-1:", hash_object.hexdigest())
```

Dockerfile:

```dockerfile
Copiar código
FROM python:3.9
WORKDIR /app
COPY hash_generator.py .
CMD ["python", "hash_generator.py"]
```

Comandos para construir e executar:

```bash
# Construir a imagem
docker build -t mascarar-dados .

# Executar o container interativo
docker run -it mascarar-dados
````
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
![image](https://github.com/user-attachments/assets/bb8cdcec-6a86-42fc-adc0-11e76b2500d6)

*AWS Partner: Credenciamento (Técnico) (Português) | AWS Partner: Accreditation
(Technical) (Portuguese)*


## 🎯 **Conclusão da Sprint**

Nesta sprint, concluímos com sucesso os objetivos propostos, enfrentamos desafios importantes e adquirimos novos conhecimentos, gostei do projeto e de sua estrutura e estou empolgado para as próximas Sprints!!

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
