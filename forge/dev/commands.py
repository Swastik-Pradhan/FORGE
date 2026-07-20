import typer

from forge.dev.generator import (
    generate_readme,
    generate_dockerfile,
    generate_gitignore,
)

from forge.utils.console import console

app = typer.Typer(help="Developer utilities.")


@app.command()
def readme(project: str):
    generate_readme(project)
    console.print("[green]README generated.[/green]")


@app.command()
def dockerize():
    generate_dockerfile()
    console.print("[green]Dockerfile generated.[/green]")


@app.command()
def gitignore():
    generate_gitignore()
    console.print("[green].gitignore generated.[/green]")