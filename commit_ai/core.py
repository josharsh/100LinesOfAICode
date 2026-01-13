import os

def validate_diff(diff: str) -> bool:
    return bool(diff.strip())

def generate_commit_prompt(diff: str) -> str:
    return f"Generate a conventional commit message for this diff:\n{diff}"

def generate_commit_message(diff: str, client) -> str:
    if not validate_diff(diff):
        return ""

    prompt = generate_commit_prompt(diff)
    response = client(prompt)

    if not isinstance(response, str):
        raise ValueError("Invalid response from AI client")

    return response.strip()
