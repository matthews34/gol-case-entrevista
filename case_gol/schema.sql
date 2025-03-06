DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS stats;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ano INTEGER,
    mes INTEGER,
    aeroporto_de_origem_sigla TEXT,
    aeroporto_de_origem_nome TEXT,
    aeroporto_de_origem_uf TEXT,
    aeroporto_de_origem_regiao TEXT,
    aeroporto_de_origem_pais TEXT,
    aeroporto_de_origem_continente TEXT,
    aeroporto_de_destino_sigla TEXT,
    aeroporto_de_destino_nome TEXT,
    aeroporto_de_destino_uf TEXT,
    aeroporto_de_destino_regiao TEXT,
    aeroporto_de_destino_pais TEXT,
    aeroporto_de_destino_continente TEXT,
    passageiros_pagos INTEGER,
    passageiros_gratis INTEGER,
    carga_paga_kg INTEGER,
    carga_gratis_kg INTEGER,
    correio_kg INTEGER,
    ask INTEGER,
    rpk INTEGER,
    atk INTEGER,
    rtk INTEGER,
    combustivel_litros INTEGER,
    distancia_voada_km INTEGER,
    decolagens INTEGER,
    carga_paga_km INTEGER,
    carga_gratis_km INTEGER,
    correio_km INTEGER,
    assentos INTEGER,
    payload INTEGER,
    horas_voadas REAL,
    bagagem_kg INTEGER,
    mercado TEXT,
    ano_mes TEXT GENERATED ALWAYS AS (printf('%04d-%02d', ano, mes)),
    UNIQUE(aeroporto_de_origem_sigla, aeroporto_de_destino_sigla, ano_mes)
);
