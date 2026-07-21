from pathlib import Path
import ast

from forge.ai.constants import IGNORE_DIRECTORIES


def get_function_signature(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    """
    Build a readable function signature from an AST node.
    """

    parameters = []

    # Positional arguments
    for arg in node.args.args:
        parameters.append(arg.arg)

    # *args
    if node.args.vararg:
        parameters.append(f"*{node.args.vararg.arg}")

    # Keyword-only arguments
    for arg in node.args.kwonlyargs:
        parameters.append(arg.arg)

    # **kwargs
    if node.args.kwarg:
        parameters.append(f"**{node.args.kwarg.arg}")

    return f"{node.name}({', '.join(parameters)})"


def build_code_map(project_root: str = ".") -> str:
    """
    Build a lightweight code map of the project.

    Includes:
    - Files
    - Classes
    - Functions
    """

    root = Path(project_root).resolve()

    output = []

    for py_file in sorted(root.rglob("*.py")):

        if any(part in IGNORE_DIRECTORIES for part in py_file.parts):
            continue

        try:
            source = py_file.read_text(encoding="utf-8")
            tree = ast.parse(source)

        except Exception:
            continue

        classes = []
        functions = []

        for node in tree.body:

            if isinstance(node, ast.ClassDef):
                classes.append(node.name)

            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append(get_function_signature(node))

        if not classes and not functions:
            continue

        output.append(f"\n{py_file.relative_to(root)}")

        if classes:
            output.append("  Classes:")

            for cls in classes:
                output.append(f"    • {cls}")

        if functions:
            output.append("  Functions:")

            for func in functions:
                output.append(f"    • {func}")

    return "\n".join(output)