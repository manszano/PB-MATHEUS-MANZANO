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
);