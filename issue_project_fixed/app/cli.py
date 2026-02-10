import click
from rich import print
from dotenv import load_dotenv
from .config import load_config

load_dotenv()


@click.command()
def main():
    config = load_config()
    print(f"[green]API Base URL:[/green] {config.api_base_url}")
