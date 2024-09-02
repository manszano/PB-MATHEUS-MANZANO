<div>
  <img src="https://github.com/user-attachments/assets/80bce710-ada7-4fe1-a4b2-8343a4ac8529" width="100%" alt="Banner">
</div>

&nbsp;
# Desafio: Ecommerce

### 1. Estrutura do Projeto
Estrutura dos diretórios do projeto.
```
ecommerce/
│
├── vendas/
│   └── backup/
│       ├── (Arquivos de backup e relatórios)
│
└── dados_de_vendas.csv (Arquivo de vendas original)
└── processamento_de_vendas.sh
└── consolidados_de_processamento_de_vendas.sh
```
### Scripts:
1. [processamento_de_vendas.sh](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%201/desafio/etapa-1/ecommerce/processamento_de_vendas.sh)
2. [consolidados_de_processamento_de_vendas.sh](https://github.com/manszano/PB-MATHEUS-MANZANO/blob/main/Sprint%201/desafio/etapa-1/ecommerce/consolidador_de_processamento_de_vendas.sh)


## 💡 **1. Script de Backup e Processamento de Vendas (_processamento_de_vendas.sh_)**

### Informações gerais

- **Linguagem utilizada:** Bash
- **Sistema Operacional:** Linux (Ubuntu)
- **Autor:** Matheus de Souza Manzano
- **Localização do script:** `/etapa1/ecommerce/`
- **Objetivo:**  Geração de relatórios.
- **Dependências:** Nenhuma, bash vanilla
- **Entrada de dados:** Arquivo CSV (`dados_de_vendas.csv`) localizado no diretório `/etapa1/ecommerce/`
- **Saída de dados:**
  - Arquivo de backup compactado (`backup-dados-YYYYMMDD.zip`)
  - Relatório em texto (`relatorio-YYYYMMDD.txt`)

### Passo a passo do script
### 1. Definição de Variáveis
No início do script, as variáveis são configuradas para definir os caminhos para os arquivos:

```bash
diretorio="/home/matheus/ecommerce"
pasta_vendas="$diretorio/vendas"
pasta_backup="$pasta_vendas/backup"
data_agora=$(date +"%Y%m%d")
```
- `diretorio`: Caminho do diretório principal onde os dados de vendas estão localizados.
- `pasta_vendas`: Diretório onde o arquivo de vendas está armazenado.
- `pasta_backup`: Diretório onde os backups serão armazenados.
- `data_agora`: Data atual no formato `YYYYMMDD`, usada para dar nome aos de backup.

### 2. Cópia do Arquivo de Vendas
O script faz uma cópia do arquivo de vendas e renomeia essa cópia para indicar que é um backup:
```bash
cp "$diretorio/dados_de_vendas.csv" "$pasta_backup/dados-$data_agora.csv"
mv "$pasta_backup/dados-$data_agora.csv" "$pasta_backup/backup-dados-$data_agora.csv"
```
- **Cópia:** Cria uma cópia do arquivo de vendas com a data no nome.
- **Renomeação:** Renomeia o arquivo copiado para backup.

### 3. Geração de Relatório
O script então gera um relatório com informações sobre o arquivo de vendas:
```bash
{
    echo "data: $(date +"%Y/%m/%d %H:%M")"
    echo "primeiro registro de venda: $(awk -F, 'NR==2 {print $5}' "$pasta_backup/backup-dados-$data_agora.csv")"
    echo "ultimo registro de venda: $(awk -F, 'END {print $5}' "$pasta_backup/backup-dados-$data_agora.csv")"
    echo "total de itens diferentes vendidos: $(awk -F, '{print $2}' "$pasta_backup/backup-dados-$data_agora.csv" | tail -n +2 | sort | uniq | wc -l)"
    echo "Primeiras 10 linhas-$data_agora.csv:"
    head -n 10 "$pasta_backup/backup-dados-$data_agora.csv"
} > "$pasta_backup/relatorio-$data_agora.txt"
```
Esse código gera um relatório com:
- **Data e hora do backup.**
- **Primeiro e último registro de venda.** utilizando o `awk`
- **Total de itens diferentes vendidos.** utilizando o `awk`
- **As primeiras 10 linhas do arquivo de vendas.** `-n 10`

### 4. Compactação do Arquivo de Backup
O arquivo de vendas é compactado em um arquivo `.zip` para economizar espaço:
```bash
zip "$pasta_backup/backup-dados-$data_agora.zip" "$pasta_backup/backup-dados-$data_agora.csv"
```
### 5. Remoção de Arquivos Temporários
logo depois da compactação, os arquivos csv originais são removidos para liberar espaço:
```bash
rm "$pasta_backup/backup-dados-$data_agora.csv"
rm "$pasta_vendas/dados_de_vendas.csv"
```
###  Exemplo de Saída
Relatório feito pelo script:
```txt
data: 2024/09/02 14:30
primeiro registro de venda: [Detalhes do primeiro registro]
ultimo registro de venda: [Detalhes do último registro]
total de itens diferentes vendidos: 10
Primeiras 10 linhas-20240902.csv:
[Primeiras 10 linhas do arquivo de vendas]
```
## 💡 **2. Script de Consolidador de Processamento de Vendas (consolidador_de_processamento_de_vendas.sh_)**

### Informações gerais

- **Linguagem utilizada:** Bash
- **Sistema Operacional:** Linux (Ubuntu)
- **Autor:** Matheus de Souza Manzano
- **Localização do script:** `/etapa1/ecommerce/`
- **Objetivo:** Gerar um arquivo com todos os relatórios concatenados.
- **Dependências:** Nenhuma, bash vanilla
- **Entrada de dados:** Arquivo CSV (`relatorio.txt`) localizado no diretório `/etapa1/ecommerce/vendas/backup`
- **Saída de dados:**
  - Relatório em texto (`relatoriofinal.txt`)

### Passo a passo do script
### 1. Definição do Diretório
   ```bash
   diretorio="./vendas/backup"
```
- Define o diretório onde os arquivos de relatório estão.

### 2. Definição do Arquivo Final:
```bash
relatorio="$diretorio/relatorio_final.txt"
```

### 3. Concatenar Relatórios
```bash
cat "$diretorio"/relatorio-*.txt > "$relatorio"
```
- Utiliza o comando `cat` para concatenar todos os arquivos de relatório que seguem o padrão de nome `relatorio-*.txt`. O conteúdo de todos esses arquivos é combinado e salvo como `relatorio_final.txt`.

## 💡 **3. Script Cron**
- **Sistema Operacional:** Linux (Ubuntu)
- **Autor:** Matheus de Souza Manzano
- **Objetivo:** Criar uma tarefa cron que executa diariamente o `processamento_de_vendas.sh`.
### Informações gerais
### 1. Definição Tarefa cron
```bash
27 15 * * * /home/matheus/ecommerce/processamento_de_vendas.sh
```
- Define a data de execução do script `processamento_de_vendas.sh` para todos os dias as `15:27:00`.
## Resultado
O resultado final é o conjunto de dois scripts que trabalham para criar processo de análise e backup de dados de vendas. O primeiro script cuida da geração de backups e relatórios, O segundo script consolida esses relatórios em um único arquivo.

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
