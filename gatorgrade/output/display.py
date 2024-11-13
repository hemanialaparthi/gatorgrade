"""Display results from the TLDR."""
from rich.console import Console


def display_tldr(console: Console) -> None:
    """Display a list of example commands and their descriptions."""
    console.print(
        "[bold yellow]Too Lazy; Didn't Read: Example Commands[/bold yellow]\n"
    )

    commands = {
        "1": {
            "command": "",
            "description": "",
        },
        "2": {
            "command": "",
            "description": "",
        },
        "3": {
            "command": "",
            "description": "",
        },
        "4": {
            "command": "",
            "description": "",
        }
    }

    for command_name, command_info in commands.items():
        console.print(f"[bold green]{command_name}[/bold green]")
        console.print(
            f"[bold white]Command:[/bold white] [bold cyan]{command_info['command']}[/bold cyan]"
        )
        console.print(
            f"[bold white]Description:[/bold white] {command_info['description']}"
        )
        console.print()

    console.print(
        "\n[bold yellow]help:[/bold yellow] Use [bold yellow]--help[/bold yellow] to see more options."
    )
