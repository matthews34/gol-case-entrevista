import csv
import sqlite3
from flask import current_app

import click
import requests


def populate_db(db: sqlite3.Connection):
    r = requests.get(current_app.config["ANAC_DATA_URL"], stream=True)

    lines = r.iter_lines()

    # skip first line
    next(lines)

    reader = csv.DictReader(
        (line.decode("utf-8-sig") for line in lines),
        delimiter=";",
    )

    c = db.cursor()
    c.execute("begin")

    insert_stmt = """INSERT INTO stats (
        ano,
        mes,
        aeroporto_de_origem_sigla,
        aeroporto_de_origem_nome,
        aeroporto_de_origem_uf,
        aeroporto_de_origem_regiao,
        aeroporto_de_origem_pais,
        aeroporto_de_origem_continente,
        aeroporto_de_destino_sigla,
        aeroporto_de_destino_nome,
        aeroporto_de_destino_uf,
        aeroporto_de_destino_regiao,
        aeroporto_de_destino_pais,
        aeroporto_de_destino_continente,
        passageiros_pagos,
        passageiros_gratis,
        carga_paga_kg,
        carga_gratis_kg,
        correio_kg,
        ask,
        rpk,
        atk,
        rtk,
        combustivel_litros,
        distancia_voada_km,
        decolagens,
        carga_paga_km,
        carga_gratis_km,
        correio_km,
        assentos,
        payload,
        horas_voadas,
        bagagem_kg,
        mercado
    ) VALUES (
        :ANO,
        :MES,
        :AEROPORTO_DE_ORIGEM_SIGLA,
        :AEROPORTO_DE_ORIGEM_NOME,
        :AEROPORTO_DE_ORIGEM_UF,
        :AEROPORTO_DE_ORIGEM_REGIAO,
        :AEROPORTO_DE_ORIGEM_PAIS,
        :AEROPORTO_DE_ORIGEM_CONTINENTE,
        :AEROPORTO_DE_DESTINO_SIGLA,
        :AEROPORTO_DE_DESTINO_NOME,
        :AEROPORTO_DE_DESTINO_UF,
        :AEROPORTO_DE_DESTINO_REGIAO,
        :AEROPORTO_DE_DESTINO_PAIS,
        :AEROPORTO_DE_DESTINO_CONTINENTE,
        :PASSAGEIROS_PAGOS,
        :PASSAGEIROS_GRATIS,
        :CARGA_PAGA_KG,
        :CARGA_GRATIS_KG,
        :CORREIO_KG,
        :ASK,
        :RPK,
        :ATK,
        :RTK,
        :COMBUSTIVEL_LITROS,
        :DISTANCIA_VOADA_KM,
        :DECOLAGENS,
        :CARGA_PAGA_KM,
        :CARGA_GRATIS_KM,
        :CORREIO_KM,
        :ASSENTOS,
        :PAYLOAD,
        :HORAS_VOADAS,
        :BAGAGEM_KG,
        :mercado
    ) ON CONFLICT DO NOTHING"""

    # TODO: criar coluna mercado manualmente
    def iter_reader():
        for i, row in enumerate(reader):
            if i % 1000 == 0:
                click.echo(f"Processing row {i}...")
            if (
                row["EMPRESA_SIGLA"],
                row["GRUPO_DE_VOO"],
                row["NATUREZA"],
            ) == (
                "GLO",
                "REGULAR",
                "DOMÉSTICA",
            ):
                row["mercado"] = "".join(
                    sorted(
                        (
                            row["AEROPORTO_DE_ORIGEM_SIGLA"],
                            row["AEROPORTO_DE_DESTINO_SIGLA"],
                        )
                    )
                )
                yield row

    c.executemany(insert_stmt, iter_reader())
    c.execute("commit")
