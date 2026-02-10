from click.testing import CliRunner
from app.cli import main


def test_cli_runs():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0
