import click
from rich import print
from .config import load_config


@click.command()
def main():
    config = load_config()
    print(f"[green]API Base URL:[/green] {config.api_base_url}")
