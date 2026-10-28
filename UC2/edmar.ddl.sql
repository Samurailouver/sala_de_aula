-- Active: 1791333808542@@127.0.0.1@5432@clinica
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente              SERIAL PRIMARY KEY,
    nome                    VARCHAR(50) NOT NULL,
    email                   TEXT   NOT NULL UNIQUE,
    endereco                TEXT   NOT NULL,
    data_de_nascimento      INTEGER NOT NULL,
    cpf                     TEXT    NOT NULL UNIQUE        
);




CREATE TABLE IF NOT EXISTS medico (
    id_medico              SERIAL PRIMARY KEY,
    nome                    VARCHAR(50) NOT NULL,
    email                   TEXT   NOT NULL UNIQUE,
    endereco                TEXT   NOT NULL,
    data_de_nascimento      INTEGER NOT NULL,
    cpf                     TEXT    NOT NULL UNIQUE        
);


CREATE TABLE atendimento (
    id_atendimento        SERIAL PRIMARY KEY,
    id_cliente            INTEGER REFERENCES cliente(id_cliente) NOT NULL,
    id_medico             INTEGER REFERENCES medico(id_medico) NOT NULL,
   	horario               TIMESTAMP NOT NULL
);