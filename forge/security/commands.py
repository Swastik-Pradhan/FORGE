import typer

from forge.security.hashing import sha256
from forge.security.scanner import scan_localhost
from forge.utils.console import console

app = typer.Typer(help="Security utilities.")


@app.command()
def hash(file: str):
    """
    Generate SHA-256 hash.
    """

    digest = sha256(file)

    console.print("\n[bold green]SHA-256[/bold green]\n")

    console.print(digest)


@app.command()
def ports():
    """
    Scan localhost ports.
    """

    ports = scan_localhost()

    if not ports:
        console.print("[yellow]No open ports found.[/yellow]")
        return

    console.print("[bold green]Open Ports[/bold green]\n")

    for port in ports:
        console.print(port)