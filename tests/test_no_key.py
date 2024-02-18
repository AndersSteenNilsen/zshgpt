import os

from click.testing import CliRunner

del os.environ['OPENAI_API_KEY']


def test_no_key():
    from src.zshgpt.cli import zshgpt

    runner = CliRunner()
    result = runner.invoke(zshgpt, ['# Can I speak with you?'])
    assert result.exit_code == 1
    assert result.exception
