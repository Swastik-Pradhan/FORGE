import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def connect():
    console.print("[cyan]Database Connection Coming Soon[/cyan]")


@app.command()
def query():
    console.print("[yellow]Database Query Tool Coming Soon[/yellow]")