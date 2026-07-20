import typer

from forge.git.service import (
    is_git_repository,
    get_git_status,
    generate_commit_message,
)
from forge.utils.console import console

app = typer.Typer(help="Git utilities.")


@app.command()
def status():
    """
    Show git status.
    """
    try:
        if not is_git_repository():
            console.print("[bold red]Error:[/bold red] Not a Git repository.")
            return

        console.print(get_git_status())

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")


@app.command("commit-msg")
def commit_msg():
    """
    Generate an AI commit message.
    """
    try:
        if not is_git_repository():
            console.print("[bold red]Error:[/bold red] Not a Git repository.")
            return

        message = generate_commit_message()

        console.print("\n[bold green]Suggested Commit Message[/bold green]\n")
        console.print(message)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")