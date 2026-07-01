import typer
from rich.console import Console

from forge.ai.commands import app as ai_app
from forge.git.commands import app as git_app
from forge.dev.commands import app as dev_app
from forge.db.commands import app as db_app
from forge.security.commands import app as sec_app

app = typer.Typer(
    help="Forge - AI Powered Developer CLI"
)

console = Console()

# Register subcommands
app.add_typer(ai_app, name="ai")
app.add_typer(git_app, name="git")
app.add_typer(dev_app, name="dev")
app.add_typer(db_app, name="db")
app.add_typer(sec_app, name="sec")


@app.command()
def version():
    """Show Forge version"""
    console.print("[bold green]Forge v0.1.0[/bold green]")


if __name__ == "__main__":
    app()