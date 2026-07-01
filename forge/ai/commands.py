import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def summarize():
    console.print("[cyan]AI Summarize Command Coming Soon[/cyan]")


@app.command()
def explain():
    console.print("[magenta]AI Explain Command Coming Soon[/magenta]")