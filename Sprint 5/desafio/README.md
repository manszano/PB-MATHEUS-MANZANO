<div>
  <img src="https://github.com/user-attachments/assets/4a9d5922-a944-4f6e-8a6c-b07e44b00df2" width="100%" alt="Banner">
</div>

&nbsp;
# 🐳 Desafio Docker: Aplicações com Imagens Docker

Bem-vindo ao projeto de criação de imagens Docker para a execução de scripts Python e interações com contêineres! 🎉 Nesssa sprint, exploramos o uso de Docker para criar e gerenciar contêineres, automatizar a execução de scripts, e implementar um algoritimo com hashes SHA-1. 

#Para visualização e execução dos contêineres, utilize o Dockerfile e os scripts fornecidos!

## 📂 Estrutura do Projeto

O projeto está organizado em várias etapas, conforme descrito abaixo:

### 1. Dockerfile para a Aplicação `carguru.py`

Neste primeiro passo, criamos um **Dockerfile** para executar o script `carguru.py` dentro de um contêiner Docker.

#### Dockerfile:

```dockerfile
# Usando a imagem base do Python 3.9
FROM python:3.9

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o script Python para o contêiner
COPY carguru.py .

# Definindo o comando padrão para rodar o script
CMD ["python", "carguru.py"]
```

#### Comandos para Construir e Executar a Imagem:

- Construir a imagem Docker:

```bash
docker build -t carguru-image .
```

- Executar o contêiner criado a partir da imagem:

```bash
docker run --name carguru-container carguru-image
```

### 2. Reutilização de Contêineres

- Sim é possivel reutilizar contâineres!
- Aprendemos a reutilizar contêineres já criados para evitar a necessidade de criar novos contêineres a cada execução.

#### Comando para Reiniciar Contêiner Parado:

- Reiniciar o contêiner existente:

```bash
docker start carguru-container
```

#### Remover Contêiner:

- Para remover contêineres antigos e liberar o nome:

```bash
docker rm carguru-container
```

### 3. Script de Mascaramento de Dados com Hash SHA-1

Criamos um novo script Python, `hash_generator.py`, que recebe uma string de entrada, gera o hash SHA-1, e imprime o hash resultante. Esse script foi containerizado para facilitar sua execução e interação via terminal.

#### Código `hash_generator.py`:

```python
import hashlib

while True:
    # Solicitar a entrada de uma string
    string = input("Digite uma string para gerar o hash (ou 'sair' para encerrar): ")
    
    if string.lower() == 'sair':
        break
    
    # Gerar o hash SHA-1 da string
    hash_object = hashlib.sha1(string.encode())
    
    # Exibir o hash resultante
    print("Hash SHA-1:", hash_object.hexdigest())
```

#### Dockerfile para o Script de Mascaramento:

```dockerfile
# Usando a imagem base do Python 3.9
FROM python:3.9

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o script Python para o contêiner
COPY hash_generator.py .

# Definindo o comando padrão para rodar o script
CMD ["python", "hash_generator.py"]
```

#### Comandos para Construir e Executar o Contêiner Interativo:

- Construir a imagem Docker:

```bash
docker build -t mascarar-dados .
```

- Executar o contêiner de forma interativa para permitir entrada de dados:

```bash
docker run -it mascarar-dados
```

### 4. Conclusão

Neste desafio, aprendemos a construir e executar imagens Docker para diferentes aplicações!

O uso do Docker para containerizar aplicativos simplifica o desenvolvimento e a implantação.



![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
