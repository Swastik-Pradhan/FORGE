import typer

from forge.ai.service import summarize_file
from forge.utils.console import console

app = typer.Typer(
    help="AI-powered developer commands."
)


@app.command()
def summarize(file: str):
    """
    Summarize a source code file using the local AI model.

    Example:
        forge ai summarize main.py
    """
    try:
        result = summarize_file(file)

        console.print(f"\n[bold blue]File:[/bold blue] {result.file_name}")
        console.print(f"[bold blue]Model:[/bold blue] {result.model}")

        console.print("\n[bold green]Summary[/bold green]\n")
        console.print(result.summary)

    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] File '{file}' not found.")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")