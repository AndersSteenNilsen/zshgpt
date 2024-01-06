from zshgpt.util import assistant


def test_create_assistant():
    a = assistant.create_assistant()
    assert a


def test_get_assistant():
    a = assistant.get_or_create_assistant()
    assert a
