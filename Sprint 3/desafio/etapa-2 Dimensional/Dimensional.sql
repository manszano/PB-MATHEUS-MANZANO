CREATE TABLE dim_pais (
   idPais         INTEGER PRIMARY KEY,
   pais           TEXT
);

CREATE TABLE dim_estado (
   idEstado       INTEGER PRIMARY KEY,
   estado         TEXT,
   idPais         INTEGER,
   FOREIGN KEY (idPais) REFERENCES dim_pais(idPais)
);

CREATE TABLE dim_cidade (
   idCidade       INTEGER PRIMARY KEY,
   cidade         TEXT
);
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

CREATE TABLE dim_combustivel (
   idCombustivel INTEGER PRIMARY KEY,
   tipoCombustivel TEXT
);

CREATE TABLE dim_vendedor (
   idVendedor    INTEGER PRIMARY KEY,
   nomeVendedor  TEXT,
   sexoVendedor  INTEGER,
   idEstado      INTEGER,
   FOREIGN KEY (idEstado) REFERENCES dim_estado(idEstado)
);

CREATE TABLE dim_tempo (
   idTempo       INTEGER PRIMARY KEY,
   dataCompleta  DATE,
   ano           INTEGER,
   mes           INTEGER,
   dia           INTEGER,
   trimestre     INTEGER,
   semanaDoAno   INTEGER
);

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
