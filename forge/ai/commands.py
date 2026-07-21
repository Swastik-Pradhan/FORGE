import typer

from forge.ai.service import (
    summarize_file,
    scan_current_project,
    index_project,
    project_summary,
)
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
        raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}")
        raise typer.Exit(code=1)


@app.command()
def scan(
    path: str = typer.Argument(
        ".",
        help="Path to the project directory to scan."
    )
):
    """
    Scan a project and display project statistics.

    Examples:
        forge ai scan
        forge ai scan forge/ai
        forge ai scan D:/Projects/MyProject
    """

    try:
        result = scan_current_project(path)

        console.print("\n[bold cyan]Project Scan[/bold cyan]\n")

        console.print(f"[bold blue]Project:[/bold blue] {result.project_name}")
        console.print(f"[bold blue]Root:[/bold blue] {result.root_path}")

        console.print()

        console.print(
            f"[bold green]Total Files:[/bold green] {result.total_files}"
        )
        console.print(
            f"[bold green]Directories:[/bold green] {result.total_directories}"
        )
        console.print(
            f"[bold green]Project Size:[/bold green] {result.total_size} bytes"
        )

        console.print()

        console.print("[bold yellow]File Types[/bold yellow]")

        if result.file_types:
            for extension, count in sorted(result.file_types.items()):
                console.print(f"{extension:<10} {count}")
        else:
            console.print("[dim]No supported files found.[/dim]")

        console.print()

        console.print(
            f"[bold magenta]Largest File:[/bold magenta] "
            f"{result.largest_file or 'N/A'}"
        )

        console.print(
            f"[bold magenta]Largest File Size:[/bold magenta] "
            f"{result.largest_file_size} bytes"
        )

        console.print("\n[bold green]✓ Scan Complete[/bold green]")

    except (FileNotFoundError, NotADirectoryError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}")
        raise typer.Exit(code=1)

@app.command()
def index(
    path: str = typer.Argument(
        ".",
        help="Path to the project directory to index."
    )
):
    """
    Create a project index for faster AI operations.

    Examples:
        forge ai index
        forge ai index forge
        forge ai index D:/Projects/MyProject
    """

    try:
        console.print("[bold cyan]Scanning project...[/bold cyan]")
        console.print(f"[bold blue]Path:[/bold blue] {path}\n")

        index_path = index_project(path)

        console.print("[bold green]✓ Project indexed successfully![/bold green]")

        console.print(
            f"[bold blue]Index Location:[/bold blue] {index_path}"
        )

    except (FileNotFoundError, NotADirectoryError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}")
        raise typer.Exit(code=1)
    
@app.command("project-summary")
def project_summary_command(
    path: str = typer.Argument(
        ".",
        help="Path to the indexed project."
    )
):
    """
    Generate an AI summary of the entire project.

    Examples:
        forge ai project-summary
        forge ai project-summary forge
        forge ai project-summary D:/Projects/MyProject
    """

    try:
        console.print("[bold cyan]Loading project index...[/bold cyan]")
        console.print(f"[bold blue]Path:[/bold blue] {path}\n")

        summary = project_summary(path)

        console.print("\n[bold green]Project Summary[/bold green]\n")
        console.print(summary)

    except FileNotFoundError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]Unexpected Error:[/bold red] {e}")
        raise typer.Exit(code=1)