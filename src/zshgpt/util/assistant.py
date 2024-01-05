from openai.types.beta.assistant import Assistant

from zshgpt.settings import Settings, settings
from zshgpt.util.client import client


def get_or_create_assistant():
    if settings.assistant_id:
        return get_assistant(settings.assistant_id)
    existing_assistants = client.beta.assistants.list().data
    existing_zshgpt_assistants = filter(lambda a: a.name == settings.assistant_name, existing_assistants)
    if existing_zshgpt_assistants:
        assistant = next(existing_zshgpt_assistants)
        assistant_id = assistant.id
        settings.assistant_id = assistant_id
        Settings.model_validate(settings)
        return assistant
    new_assistant = create_assistant()
    assistant_id = new_assistant.id
    settings.assistant_id = assistant_id
    Settings.model_validate(settings)
    return new_assistant


def create_assistant() -> Assistant:
    return client.beta.assistants.create(
        name=settings.assistant_name,
        instructions="""You are a zsh terminal assistant. Everything you return will be returned directly in a terminal.
If the user wants a textual answer, remember to put '#' in front of all lines that should not run.
If the user is looking for a terminal command, return the command without #
You are allowed to explain what the command does as long as you put '#' in front of the explenation lines
""",
        model=settings.model,
        tools=[{'type': 'code_interpreter'}],
    )


def get_assistant(assistant_id: str) -> Assistant:
    return client.beta.assistants.retrieve(assistant_id)
