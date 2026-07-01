import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def ports():
    console.print("[red]Port Scanner Coming Soon[/red]")


@app.command()
def hash():
    console.print("[magenta]Hash Generator Coming Soon[/magenta]")