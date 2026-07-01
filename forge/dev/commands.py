import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def init():
    console.print("[green]Project Initializer Coming Soon[/green]")


@app.command()
def dockerize():
    console.print("[blue]Docker Setup Coming Soon[/blue]")