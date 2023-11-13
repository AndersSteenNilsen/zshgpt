from zshgpt.settings import settings
from zshgpt.util.client import client


def create_assistant():
    client.beta.assistants.create(
        name=settings.assistant_name,
        description="""You are a zsh terminal assistant. Everything you return will be returned directly in a terminal.
If the user wants a textual answer, remember to put '#' in front of all lines that should not run.
If the user is looking for a terminal command, return the command without #
You are allowed to explain what the command does as long as you put '#' in front of the explenation lines
""",
        model=settings.model,
        tools=[{'type': 'code_interpreter'}],
    )


def get_assistant():
    pass
