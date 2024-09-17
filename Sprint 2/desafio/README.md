<div>
  <img src="https://github.com/user-attachments/assets/49e248b9-295b-4b5c-b275-3d28a4151f27" width="100%" alt="Banner">
</div>



&nbsp;
# 📊  Desafio: Desafio de Modelagem de Dados

Bem-vindo(a) ao **Desafio de Modelagem de Dados**, onde abordamos as etapas de **normalização** e a criação de um **modelo dimensional**. Aqui está o resumo dos passos que segui para transformar os dados
---

## 🛠️ Descrição Geral

Este projeto consiste em dois principais objetivos:

1. **Normalização de um banco de dados relacional**: Eliminar redundâncias e inconsistências, garantindo que as normalizalçoes sejam aplicadas corretamente.
2. **Criação de um modelo dimensional**: Adaptar o modelo relacional para uma estrutura dimensional.

---

## 🔄 Normalização do Modelo Relacional

### Passos Seguidos:

1. **Entendimento da Tabela Inicial**: 
   - A tabela inicial armazenava informações de clientes, carros, vendedores e combustíveis em uma única estrutura. Nosso primeiro passo foi identificar redundâncias.

2. **Aplicação das Formas Normais**:
   - **1ª Forma Normal (1NF)**: Garantimos que todos os valores eram atômicos, eliminando grupos repetitivos.
   - **2ª Forma Normal (2NF)**: Identificamos e removemos dependências parciais. Por exemplo, criamos tabelas para `Cliente`, `Carro`, `Vendedor`, etc.
   - **3ª Forma Normal (3NF)**: Removemos dependências transitivas, como separar os dados de `Combustível` da tabela `Carro`.

### 🔑 Resultado:
Após a normalização, obtivemos as seguintes tabelas:
- **Tabela 1**: `tb_locacao` código:
```sql
CREATE TABLE tb_locacao (
   idLocacao      INTEGER PRIMARY KEY,
   idCliente      INTEGER,
   idCarro        INTEGER,
   dataLocacao    DATETIME,
   horaLocacao    TIME,
   qtdDiaria      INTEGER,
   vlrDiaria      REAL,
   dataEntrega    DATE,
   horaEntrega    TIME,
   idVendedor     INTEGER,
   FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
   FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro),
   FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
```
- **Tabelas 2**: `tb_cliente`, `tb_carro`, `tb_combustivel`, `tb_vendedor` código:
```sql
CREATE TABLE tb_cliente (
   idCliente      INTEGER PRIMARY KEY,
   nomeCliente    TEXT,
   idCidade       INTEGER,
   idEstado       INTEGER,
   idPais         INTEGER,
   FOREIGN KEY (idCidade) REFERENCES tb_cidade(idCidade),
   FOREIGN KEY (idEstado) REFERENCES tb_estado(idEstado),
   FOREIGN KEY (idPais) REFERENCES tb_pais(idPais)
);

CREATE TABLE tb_carro (
   idCarro        INTEGER PRIMARY KEY,
   kmCarro        INTEGER,
   classiCarro    TEXT,
   marcaCarro     TEXT,
   modeloCarro    TEXT,
   anoCarro       INTEGER,
   idCombustivel  INTEGER,
   FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
); CREATE TABLE tb_combustivel (
   idCombustivel  INTEGER PRIMARY KEY,
   tipoCombustivel TEXT
);

CREATE TABLE tb_vendedor (
   idVendedor     INTEGER PRIMARY KEY,
   nomeVendedor   TEXT,
   sexoVendedor   INTEGER,
   idEstado       INTEGER,
   FOREIGN KEY (idEstado) REFERENCES tb_estado(idEstado)
);
```
**Tabelas 3**: `tb_pais`, `tb_estado`, `tb_cidade` código:
```sql
CREATE TABLE tb_pais (
   idPais         INTEGER PRIMARY KEY,
   pais           TEXT
);

CREATE TABLE tb_estado (
   idEstado       INTEGER PRIMARY KEY,
   estado         TEXT,
   idPais         INTEGER,
   FOREIGN KEY (idPais) REFERENCES tb_pais(idPais)
);
--tb 2 ci
CREATE TABLE tb_cidade (
   idCidade       INTEGER PRIMARY KEY,
   cidade         TEXT
);
```
### 📊 Diagrama completo:
![Movie Database](https://github.com/user-attachments/assets/3a3062c3-bc3c-4a34-8a14-2e5306f2053f)


Essas tabelas estão interligadas por chaves estrangeiras, garantindo a integridade referencial e a eliminação de redundâncias.

---

## 📈 Modelo Dimensional

### 📋 Estrutura do Modelo:

O modelo dimensional segue o padrão **snowflake**, onde as dimensões são parcialmente normalizadas e conectadas à tabela de fatos. Isso facilita análises e consultas eficientes.

- **Tabela Fato (Fato de Locações)**:
  - Dados de locações, como quantidade de diárias, valor, e IDs de referência para as dimensões código:.
```sql
CREATE TABLE fact_locacao (
   idLocacao     INTEGER PRIMARY KEY,
   idCliente     INTEGER,
   idCarro       INTEGER,
   idTempoLocacao INTEGER,  
   idTempoEntrega INTEGER,  
   qtdDiaria     INTEGER,
   vlrDiaria     REAL,
   idVendedor    INTEGER,
   FOREIGN KEY (idCliente) REFERENCES dim_cliente(idCliente),
   FOREIGN KEY (idCarro) REFERENCES dim_carro(idCarro),
   FOREIGN KEY (idTempoLocacao) REFERENCES dim_tempo(idTempo),  
   FOREIGN KEY (idTempoEntrega) REFERENCES dim_tempo(idTempo),  
   FOREIGN KEY (idVendedor) REFERENCES dim_vendedor(idVendedor)
);
```

- **Tabelas de Dimensões** código::
  - **Dimensão Cliente**: `dim_cliente`
```sql
CREATE TABLE dim_cliente (
   idCliente     INTEGER PRIMARY KEY,
   nomeCliente   TEXT,
   idCidade      INTEGER,
   idEstado      INTEGER,
   idPais        INTEGER,
   FOREIGN KEY (idCidade) REFERENCES dim_cidade(idCidade),
   FOREIGN KEY (idEstado) REFERENCES dim_estado(idEstado),
   FOREIGN KEY (idPais) REFERENCES dim_pais(idPais)
);
```
  - **Dimensão Carro** código:: `dim_carro`
```sql
CREATE TABLE dim_carro (
   idCarro       INTEGER PRIMARY KEY,
   kmCarro       INTEGER,
   classiCarro   TEXT,
   marcaCarro    TEXT,
   modeloCarro   TEXT,
   anoCarro      INTEGER,
   idCombustivel INTEGER,
   FOREIGN KEY (idCombustivel) REFERENCES dim_combustivel(idCombustivel)
);

```
  - **Dimensão Vendedor** código:: `dim_vendedor`
```sql
CREATE TABLE dim_vendedor (
   idVendedor    INTEGER PRIMARY KEY,
   nomeVendedor  TEXT,
   sexoVendedor  INTEGER,
   idEstado      INTEGER,
   FOREIGN KEY (idEstado) REFERENCES dim_estado(idEstado)
);
```
  - **Dimensão Combustível** código:: `dim_combustivel`
```sql
CREATE TABLE dim_combustivel (
   idCombustivel INTEGER PRIMARY KEY,
   tipoCombustivel TEXT
);
```
  - **Dimensão Tempo** código:: `dim_tempo` código:
```sql
CREATE TABLE dim_tempo (
   idTempo       INTEGER PRIMARY KEY,
   dataCompleta  DATE,
   ano           INTEGER,
   mes           INTEGER,
   dia           INTEGER,
   trimestre     INTEGER,
   semanaDoAno   INTEGER
   );
```
 
### 📊 Diagrama completo:
![DimensionalDiagrama](https://github.com/user-attachments/assets/4da4d97c-28aa-4aac-8d06-a5d94bcbcbe3)

### 💡 Vantagens do Modelo Dimensional:

- **Performance Otimizada**: Consultas analíticas que exigem agregação de dados são muito mais rápidas.
- **Facilidade para Relatórios**: A estrutura dimensional é ideal para gerar relatórios dinâmicos e dashboards, explorando dados de maneira granular.

---

## 📝 Conclusão

Este desafio demonstrou a importância de:

- **Normalização**: Evitar redundâncias e garantir a integridade dos dados através das formas normais.
- **Modelo Dimensional**: Oferecer uma estrutura eficiente para consultas analíticas, essencial em ambientes de **Business Intelligence (BI)**.

Com essas etapas, o banco de dados está pronto tanto para operações transacionais quanto para análises complexas. 🚀

---

## 📂 Estrutura do Projeto

- **Tabelas Relacionais**: 
  - `tb_locacao`, `tb_cliente`, `tb_carro`, `tb_combustivel`, `tb_vendedor`
  
- **Tabelas Dimensionais**: 
  - `tb_fato_locacao`, `dim_cliente`, `dim_carro`, `dim_combustivel`, `dim_vendedor`, `dim_tempo`


![bottom](https://github.com/user-attachments/assets/a06b7240-a4be-45d7-86e7-9427136b3891)
