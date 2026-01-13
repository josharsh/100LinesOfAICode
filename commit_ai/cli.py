import os
from commit_ai.core import generate_commit_message

def get_api_key():
    key = os.getenv("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY not set")
    return key

def real_ai_client(prompt: str) -> str:
    # placeholder for actual API call
    return "feat: example commit"

def main():
    diff = os.popen("git diff").read()
    msg = generate_commit_message(diff, real_ai_client)
    print(msg)

if __name__ == "__main__":
    main()
