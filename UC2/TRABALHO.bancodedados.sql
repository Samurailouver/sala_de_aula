CREATE TABLE IF NOT EXISTS cliente (
    id_cliente  SERIAL  PRIMARY KEY,
    nome        VARCHAR(50) NOT NULL,
    telefone    TEXT NOT NULL,
	email       TEXT NOT NULL UNIQUE, 
);

CREATE TABLE IF NOT EXISTS agendamento (
	id_agendamento SERIAL PRIMARY KEY,
	id_quadra  INTEGER REFERENCES quadra(id_quadra)NOT NULL,
  	tempo_termino_max INTEGER NOT NULL UNIQUE,
	hora DATETIME NOT NULL UNIQUE,
	id_partida INTEGER REFERENCES partida(id_partida)NOT NULL,
);

CREATE TABLE IF NOT EXISTS partida (
	id_partida SERIAL PRIMARY KEY,
	nome_artilheiro VARCHAR(50) NOT NULL,
	total_gols INTEGER NOT NULL,
);

CREATE TABLE IF NOT EXISTS quadra (
	id_quadra SERIAL PRIMARY KEY,
	coberta BOOLEAN NOT NULL,
	preco NUMERIC NOT NULL UNIQUE,
);