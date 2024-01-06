from click.testing import CliRunner

from zshgpt.cli import zshgpt


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(zshgpt, ['Hello chatgpt'])
    assert result.exit_code == 0
    assert result.output
