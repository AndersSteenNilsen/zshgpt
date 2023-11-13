# SPDX-FileCopyrightText: 2023-present Anders Steen <asteennilsen@gmail.com
#
# SPDX-License-Identifier: MIT
import time

import click
import openai
from openai.error import AuthenticationError

from zshgpt.__about__ import __version__
from zshgpt.cli.messages import messages


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='zshgpt')
@click.argument('user_query')
def zshgpt(user_query: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', messages=[*messages, {'role': 'user', 'content': user_query}], stream=True
        )
    except AuthenticationError as auth_error:
        raise click.ClickException(auth_error.user_message) from auth_error
    for chunk in response:
        if 'content' not in chunk['choices'][0]['delta']:
            return
        click.echo(chunk['choices'][0]['delta']['content'], nl=False)
        time.sleep(0.2)
