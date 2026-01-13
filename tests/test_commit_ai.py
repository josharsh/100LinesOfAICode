import pytest
from commit_ai.core import (
    validate_diff,
    generate_commit_prompt,
    generate_commit_message,
)

def dummy_client(prompt: str) -> str:
    return "feat: add new feature"

def test_validate_diff():
    assert validate_diff("+ new code")
    assert not validate_diff("")
    assert not validate_diff("   ")

def test_generate_prompt():
    diff = "+ test"
    prompt = generate_commit_prompt(diff)
    assert diff in prompt
    assert "Generate a conventional commit" in prompt

def test_generate_commit_message_success():
    diff = "+ new function"
    msg = generate_commit_message(diff, dummy_client)
    assert msg.startswith("feat:")

def test_generate_commit_message_empty_diff():
    msg = generate_commit_message("", dummy_client)
    assert msg == ""

def test_invalid_client_response():
    def bad_client(prompt):
        return None

    with pytest.raises(ValueError):
        generate_commit_message("+ test", bad_client)
