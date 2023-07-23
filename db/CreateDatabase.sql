USE Pycodebr;

CREATE TABLE clientes (
    id integer not null auto_increment,
    nome varchar(100),
    bairro varchar(100),
    idade integer,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collection_connection = utf8_general_ci;

INSERT INTO clientes (nome, bairro, idade)
VALUES ('Macmiller', 'Andaraí', 41);

INSERT INTO clientes (nome, bairro, idade)
VALUES ('Cristiane', 'Campo Grande', 30);

INSERT INTO clientes (nome, bairro, idade)
VALUES ('Danielle', 'Tijuca', 24);

INSERT INTO clientes (nome, bairro, idade)
VALUES ('Clarissa', 'Copacabana', 22);