from rich.console import Console


def display_tldr(console: Console, chosen_command: str = None) -> None:
    """Display a list of example commands and their descriptions."""
    # a dictionaly of commands and their descriptions
    commands = {
        "mark": "poetry run execexam <path-to-project> <path-to-tests> --maxfail",
        "report": "poetry run execexam <path-to-project> <path-to-tests> --report <report_type>/<all>",
        "advice-model": "poetry run execexam <path-to-project> <path-to-tests> --advice-model <model> --advice-method <method>",
        "debug": "poetry run execexam <path-to-project> <path-to-tests> <--debug>/<--no-debug>",
        "fancy": "poetry run execexam <path-to-project> <path-to-tests> <--fancy>/<--no-fancy>",
        "verbose": "poetry run execexam <path-to-project> <path-to-tests> <--verbose>/<--no-verbose>",
    }