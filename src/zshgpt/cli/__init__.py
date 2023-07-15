# SPDX-FileCopyrightText: 2023-present Anders Steen <asteennilsen@gmail.com
#
# SPDX-License-Identifier: MIT
import os

import click
import openai

from zshgpt.__about__ import __version__
from zshgpt.cli.messages import messages


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='zshgpt')
@click.option(
    '--key', prompt=not os.environ.get('OPENAI_API_KEY'), hide_input=True,
    default=lambda: os.environ.get('OPENAI_API_KEY', '')
)
@click.argument('user_query')
def zshgpt(user_query: str, key: str):
     response = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages=[*messages, {'role': 'user', 'content': user_query}])
     click.echo(response['choices'][0]['message']['content'])

