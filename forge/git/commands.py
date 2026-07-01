import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def commit_msg():
    console.print("[yellow]AI Commit Message Generator Coming Soon[/yellow]")