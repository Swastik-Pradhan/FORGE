import typer

from forge.db.connection import connect
from forge.db.service import (
    list_tables,
    describe_table,
    execute_query,
)

from forge.utils.console import console

app = typer.Typer(help="Database utilities.")


@app.command()
def connect_db(database: str):
    """
    Connect to a SQLite database.
    """
    connect(database)

    console.print(f"[green]Connected to {database}[/green]")


@app.command()
def tables():
    """
    List database tables.
    """
    tables = list_tables()

    if not tables:
        console.print("[yellow]No tables found.[/yellow]")
        return

    for table in tables:
        console.print(f"- {table}")


@app.command()
def schema(table: str):
    """
    Show table schema.
    """
    rows = describe_table(table)

    for row in rows:
        console.print(row)


@app.command()
def query(sql: str):
    """
    Execute SQL query.
    """
    rows = execute_query(sql)

    for row in rows:
        console.print(row)