from click.testing import CliRunner

from src.zshgpt.cli import zshgpt


def test_no_key():
    runner = CliRunner()
    result = runner.invoke(zshgpt, ['# Can I speak with you?'])
    assert result.exit_code == 1
    assert result.exception
