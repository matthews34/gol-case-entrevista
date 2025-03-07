from __future__ import annotations
import sqlite3
from typing import TYPE_CHECKING
from case_gol.utils.populate_db import populate_db as _populate_db

import click
from flask import current_app, g

if TYPE_CHECKING:
    from flask import Flask


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db(populate_db=False):
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))

    if populate_db:
        _populate_db(db)


@click.command("init-db")
@click.option("--populate-db", default=False)
def init_db_command(populate_db=False):
    """Clear the existing data and create new tables."""
    init_db(populate_db)
    click.echo("Initialized the database.")


@click.command("populate-db")
def populate_db_command():
    """Populates DB with data from ANAC"""
    _populate_db(get_db())
    click.echo("Populated DB.")


def init_app(app: Flask):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(populate_db_command)
