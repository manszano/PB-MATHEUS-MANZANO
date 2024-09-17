<div>
  <img src="https://github.com/user-attachments/assets/6f7f5908-d43a-4998-810d-9795301169a1" width="100%" alt="Banner">
</div>



## 📝 **Instruções/Informações/Anotações**

### **Objetivo do Desafio:**
Desenvolver um projeto utilizando técnicas de modelagem de banco de dados relacionais e dimensionais, aplicando normalização e construção de um modelo dimensional estilo *Snowflake*.

- **Tarefas Realizadas:**  
  - **Normalização do Banco de Dados:**  
    - Aplicação das formas normais (1NF, 2NF, 3NF) para criar um banco de dados relacional eficiente, eliminando redundâncias e garantindo a integridade dos dados.
  - **Criação do Modelo Dimensional:**  
    - Construção de um modelo *Snowflake* para otimização de consultas analíticas, separando as tabelas de dimensão (cliente, carro, vendedor, combustível) e tabela fato (locação).
  - **Adição da Tabela de Tempo:**
    - Inclusão de uma nova dimensão para rastrear dados de tempo, como ano de locação, ano de entrega, etc.

### **Anotações Importantes:**
#### _Aprendizados:_

- **Técnicas Utilizadas:** Modelagem Relacional, Modelagem Dimensional, SQL
- **Desafios Enfrentados:**  
  - Aplicação da normalização e criação de chaves estrangeiras para relacionar as tabelas.
  - Otimização do modelo dimensional para suportar consultas analíticas.
- **Soluções:**  
  - Implementação de tabelas com chaves primárias e estrangeiras para garantir a integridade dos dados.
  - Design do modelo *Snowflake* com foco em eficiência para consultas de análise de locações.


---
## **Exercícios**
_Essa sprint conteve 16 exercícios_
### E01
O objetivo deste exercício era selecionar todos os livros publicados após 31 de dezembro de 2014, ordenando os resultados pelo código do livro de forma ascendente. A cláusula `WHERE` filtra as publicações pela data, e o `ORDER BY cod ASC` garante que a lista seja exibida na ordem crescente dos códigos.
```sql
SELECT * 
FROM livro 
WHERE publicacao > '2014-12-31'
ORDER BY cod ASC;
```

### E02
Aqui, foi necessário listar os títulos dos livros e seus respectivos valores, ordenados pelos valores de forma decrescente. A cláusula `LIMIT 10` limita o número de registros retornados aos 10 livros mais caros.
```sql
SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;
```

### E03
Neste exercício, o foco foi contar quantos livros cada editora publicou, juntamente com o nome da editora e as informações de localização (estado e cidade). Usou-se o `JOIN` para combinar as tabelas de `livro`, `editora` e `endereco`, e o `GROUP BY` para agrupar os resultados por editora e local. A ordenação foi feita de acordo com o número de livros publicados, de forma decrescente, e o `LIMIT 5` restringiu os resultados às 5 editoras com mais publicações.
```sql
SELECT COUNT(livro.cod) AS quantidade, editora.nome, endereco.estado, endereco.cidade
FROM livro
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
GROUP BY editora.codeditora, editora.nome, endereco.estado, endereco.cidade
ORDER BY quantidade DESC
LIMIT 5;
```
### E04
Aqui, o objetivo era listar os autores, suas datas de nascimento e quantos livros eles publicaram. A função de agregação `COUNT` foi usada para contar os livros associados a cada autor, mesmo que não tenha publicado nenhum (por isso o `LEFT JOIN`). Os resultados foram agrupados por autor e ordenados em ordem alfabética de nome.
```sql
SELECT autor.codautor, autor.nome, autor.nascimento, COUNT(livro.cod) AS quantidade
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
GROUP BY autor.codautor, autor.nome, autor.nascimento
ORDER BY autor.nome ASC;
```
### E05
Neste exercício, foi necessário listar os autores que publicaram livros com editoras fora dos estados de Rio Grande do Sul e Paraná. O `JOIN` foi usado para conectar as tabelas de `autor`, `livro`, `editora` e `endereco`, e o filtro `WHERE` excluiu os estados mencionados. A cláusula `ORDER BY` organizou os autores por ordem alfabética.
```sql
SELECT DISTINCT autor.nome
FROM autor
JOIN livro ON autor.codautor = livro.autor
JOIN editora ON livro.editora = editora.codeditora
JOIN endereco ON editora.endereco = endereco.codendereco
WHERE endereco.estado NOT IN ('RIO GRANDE DO SUL', 'PARANÁ')
ORDER BY autor.nome ASC;
```
### E06
Aqui, foi solicitado encontrar o autor com o maior número de publicações. O `JOIN` conectou as tabelas de `autor` e `livro`, e a função `COUNT` contou o número de publicações por autor. A ordenação foi feita pelo número de publicações em ordem decrescente, e o `LIMIT 1` garantiu que apenas o autor com mais publicações fosse retornado.
```sql
SELECT autor.codautor, autor.nome, COUNT(livro.cod) AS quantidade_publicacoes
FROM autor
JOIN livro ON autor.codautor = livro.autor
GROUP BY autor.codautor, autor.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1;
```
### E07
Este exercício exigia listar os autores que ainda não publicaram nenhum livro. O `LEFT JOIN` permitiu identificar esses autores ao filtrar os registros onde o campo `livro.autor` era nulo (`IS NULL`). A lista foi ordenada alfabeticamente.
```sql
SELECT autor.nome
FROM autor
LEFT JOIN livro ON autor.codautor = livro.autor
WHERE livro.autor IS NULL
ORDER BY autor.nome ASC;
```
### E08
Aqui, foi necessário identificar o vendedor com o maior número de vendas concluídas. O `JOIN` entre as tabelas de vendedores e vendas permitiu contar as vendas concluídas (`WHERE vd.status = 'Concluído'`), agrupando os resultados por vendedor e ordenando em ordem decrescente de vendas, retornando apenas o vendedor com mais vendas.
```sql
SELECT
    v.cdvdd,
    v.nmvdd
FROM
    tbvendedor v
JOIN
    tbvendas vd ON v.cdvdd = vd.cdvdd
WHERE
    vd.status = 'Concluído'
GROUP BY
    v.cdvdd, v.nmvdd
ORDER BY
    COUNT(vd.cdven) DESC
LIMIT 1;
```
### E09
Neste exercício, o objetivo era encontrar o produto mais vendido em um intervalo de tempo específico (2014-02-03 a 2018-02-02) e com status de venda concluído. O `GROUP BY` foi utilizado para agrupar as vendas por produto, e a soma da quantidade de vendas (`SUM(v.qtd)`) ajudou a identificar o mais vendido. A ordenação foi feita pela soma em ordem decrescente e retornou o produto com maior quantidade vendida.
```sql
SELECT
    v.cdpro,
    v.nmpro
FROM
    tbvendas v
WHERE
    v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
    AND v.status = 'Concluído'
GROUP BY
    v.cdpro, v.nmpro
ORDER BY
    SUM(v.qtd) DESC
LIMIT 1;
```
### E010
Aqui, o foco foi calcular o valor total de vendas e a comissão de cada vendedor. O `SUM` foi utilizado para somar o total de vendas, e a comissão foi calculada multiplicando o total pelo percentual de comissão do vendedor. O `ROUND` arredondou o valor da comissão para duas casas decimais, e os resultados foram ordenados pela comissão em ordem decrescente.
```sql
SELECT 
    vd.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao / 100, 2) AS comissao
FROM 
    tbvendas v
JOIN 
    tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE 
    v.status = 'Concluído'
GROUP BY 
    vd.nmvdd
ORDER BY 
    comissao DESC;

```
### E011
Neste exercício, era preciso encontrar o cliente que gastou mais em compras. A soma do valor das vendas (`SUM(v.qtd * v.vrunt)`) foi utilizada para calcular o total gasto por cliente, e os resultados foram agrupados por cliente. A ordenação foi feita pelo total gasto em ordem decrescente, e o `LIMIT 1` retornou o cliente com o maior gasto.
```sql
SELECT
    v.cdcli,
    v.nmcli,
    SUM(v.qtd * v.vrunt) AS gasto
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.cdcli, v.nmcli
ORDER BY
    gasto DESC
LIMIT 1;

```
### E012
Aqui, a primeira parte usou uma CTE (`WITH`) para encontrar o vendedor com o menor total de vendas (acima de zero). Depois, essa CTE foi usada para buscar os dependentes do vendedor com o menor total de vendas, ordenando-os por nome.
```sql
WITH VendedorVendas AS (
    SELECT 
        vd.cdvdd,
        SUM(v.qtd * v.vrunt) AS valor_total_vendas
    FROM 
        tbvendas v
    JOIN 
        tbvendedor vd ON v.cdvdd = vd.cdvdd
    WHERE 
        v.status = 'Concluído'
    GROUP BY 
        vd.cdvdd
    HAVING 
        valor_total_vendas > 0
    ORDER BY 
        valor_total_vendas ASC
    LIMIT 1
)
SELECT 
    d.cddep,
    d.nmdep,
    d.dtnasc,
    vv.valor_total_vendas
FROM 
    tbdependente d
JOIN 
    VendedorVendas vv ON d.cdvdd = vv.cdvdd
ORDER BY 
    d.nmdep;

```
### E013
O objetivo deste exercício era listar os produtos vendidos nos canais "Ecommerce" ou "Matriz" e contar o número de vendas concluídas para cada produto. O `GROUP BY` organizou os resultados por produto e canal de vendas, e a função `SUM(v.qtd)` contou a quantidade total de vendas. A ordenação foi feita em ordem crescente pela quantidade de vendas, e o `LIMIT 10` retornou os 10 produtos com menor quantidade de vendas.
```sql
SELECT
    v.cdpro,
    v.nmcanalvendas,
    v.nmpro,
    SUM(v.qtd) AS quantidade_vendas
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
    AND (v.nmcanalvendas = 'Ecommerce' OR v.nmcanalvendas = 'Matriz')
GROUP BY
    v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY
    quantidade_vendas ASC
LIMIT 10;

```
### E014
Neste exercício, foi necessário calcular o gasto médio por estado. A função `ROUND` arredondou a média das vendas para duas casas decimais, e o `GROUP BY` organizou os resultados por estado. Os estados foram ordenados pelo gasto médio em ordem decrescente.
```sql
SELECT
    v.estado,
    ROUND(AVG(v.qtd * v.vrunt), 2) AS gastomedio
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.estado
ORDER BY
    gastomedio DESC;
```
### E015
O foco aqui era listar todas as vendas que foram marcadas como deletadas (`v.deletado = '1'`). A consulta ordenou as vendas deletadas pelo código de venda em ordem crescente.
```sql
SELECT
    v.cdven
FROM
    tbvendas v
WHERE
    v.deletado = '1'
ORDER BY
    v.cdven ASC;
```
### E016
Neste exercício, o objetivo era calcular a quantidade média de produtos vendidos por estado. A função `ROUND` arredondou a média de vendas para quatro casas decimais, e os resultados foram agrupados por estado e produto. A ordenação foi feita pela combinação de estado e nome do produto em ordem crescente.
```sql
SELECT
    v.estado,
    v.nmpro,
    ROUND(AVG(v.qtd), 4) AS quantidade_media
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
GROUP BY
    v.estado, v.nmpro
ORDER BY
    v.estado ASC,
    v.nmpro ASC;
```

---
## **Desafios**

Durante a sprint, realizamos o desafio de `Normalização de um banco de dados relacional e Criação de um modelo dimensional`

1. **Normalização de um banco de dados relacional**: Eliminar redundâncias e inconsistências, garantindo que as normalizalçoes sejam aplicadas corretamente.
2. **Criação de um modelo dimensional**: Adaptar o modelo relacional para uma estrutura dimensional.


## 🔄 Normalização do Modelo Relacional

### Passos Seguidos:

1. **Entendimento da Tabela Inicial**: 
   - A tabela inicial armazenava informações de clientes, carros, vendedores e combustíveis em uma única estrutura. Nosso primeiro passo foi identificar redundâncias.

2. **Aplicação das Formas Normais**:
   - **1ª Forma Normal (1NF)**: Garantimos que todos os valores eram atômicos, eliminando grupos repetitivos.
   - **2ª Forma Normal (2NF)**: Identificamos e removemos dependências parciais. Por exemplo, criamos tabelas para `Cliente`, `Carro`, `Vendedor`, etc.
   - **3ª Forma Normal (3NF)**: Removemos dependências transitivas, como separar os dados de `Combustível` da tabela `Carro`.

### Diagrama após normalização:
![Movie Database](https://github.com/user-attachments/assets/c32f2537-e3c4-4c58-98f8-c46585a2d298)


## 📈 Modelo Dimensional

### 📋 Estrutura do Modelo:

O modelo dimensional segue o padrão **snowflake**, onde as dimensões são parcialmente normalizadas e conectadas à tabela de fatos. Isso facilita análises e consultas eficientes.

- **Tabela Fato (Fato de Locações)**:
  - Dados de locações, como quantidade de diárias, valor, e IDs de referência para as dimensões código:.
- **Tabelas de Dimensões** código::
  - **Dimensão Cliente**: `dim_cliente`
  - **Dimensão Carro** código: `dim_carro`
  - **Dimensão Vendedor** código: `dim_vendedor`
  - **Dimensão Tempo** código: `dim_tempo` código:

### 📊 Diagrama dimensional:
![DimensionalDiagrama](https://github.com/user-attachments/assets/577c8432-39e9-4140-ad4f-91b0b1c57eeb)

---

## 🎓 **Certificados**

### **Certificados Conquistados Durante a Sprint:**

![image](https://github.com/user-attachments/assets/4ee653cb-cb2e-4947-a1e6-22575743eb5a)
![aws-partner-sales-accreditation](https://github.com/user-attachments/assets/6fef0082-71a0-4431-ac96-f89f3836ab10)

---

## 🎯 **Conclusão da Sprint**

Nesta sprint, concluímos com sucesso os objetivos propostos, enfrentamos desafios importantes e adquirimos novos conhecimentos, gostei do projeto e de sua estrutura e estou empolgado para as próximas Sprints!!

![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)

