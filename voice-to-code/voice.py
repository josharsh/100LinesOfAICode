#!/usr/bin/env python3
"""Voice to Code - Speak your code in <100 lines."""
import os, sys, argparse
from pathlib import Path
try:
    import speech_recognition as sr
except ImportError:
    print("Install: pip install SpeechRecognition pyaudio")
    sys.exit(1)
from anthropic import Anthropic

class VoiceToCode:
    def __init__(self, api_key: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.recognizer = sr.Recognizer()

    def listen(self, timeout: int = 10) -> str:
        """Listen to microphone and convert speech to text."""
        with sr.Microphone() as source:
            print("🎤 Listening... (speak now)")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=30)
                print("🔄 Processing...")
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.WaitTimeoutError:
                return "❌ No speech detected"
            except sr.UnknownValueError:
                return "❌ Could not understand audio"
            except sr.RequestError as e:
                return f"❌ Error: {e}"

    def generate_code(self, description: str, language: str = "python") -> dict:
        """Generate code from natural language description."""
        prompt = f"""Convert this description to {language} code:

"{description}"

Requirements:
1. Write clean, working code
2. Add comments explaining key parts
3. Follow {language} best practices
4. Include error handling
5. Make it production-ready

Output format:
- First, explain what the code will do (1-2 sentences)
- Then provide the complete code
- Finally, add usage example if applicable"""

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )
        return {"description": description, "code": response.content[0].text, "language": language}

    def speak_and_code(self, language: str = "python", save: bool = False, filename: str = None) -> dict:
        """Main function: listen to speech and generate code."""
        description = self.listen()

        if description.startswith("❌"):
            return {"error": description}

        print(f"\n💭 You said: \"{description}\"\n")
        result = self.generate_code(description, language)

        if save:
            file_ext = {"python": ".py", "javascript": ".js", "typescript": ".ts",
                       "java": ".java", "go": ".go", "rust": ".rs"}.get(language, ".txt")
            filename = filename or f"generated{file_ext}"
            # Extract code block from response
            code = result['code']
            if "```" in code:
                code = code.split("```")[1]
                if code.startswith(language) or code.startswith("python") or code.startswith("javascript"):
                    code = "\n".join(code.split("\n")[1:])
            Path(filename).write_text(code)
            result['saved_to'] = filename

        return result

def main():
    parser = argparse.ArgumentParser(description="Voice to Code - Speak your code into existence")
    parser.add_argument("--lang", default="python", help="Programming language (python, javascript, java, etc.)")
    parser.add_argument("--save", action="store_true", help="Save generated code to file")
    parser.add_argument("--file", help="Output filename (default: generated.<ext>)")
    parser.add_argument("--text", help="Skip voice input, use text description")
    args = parser.parse_args()

    v2c = VoiceToCode()

    if args.text:
        print(f"💭 Description: \"{args.text}\"\n")
        result = v2c.generate_code(args.text, args.lang)
        if args.save:
            file_ext = {"python": ".py", "javascript": ".js", "typescript": ".ts"}.get(args.lang, ".txt")
            filename = args.file or f"generated{file_ext}"
            code = result['code']
            if "```" in code:
                code = code.split("```")[1]
                if code.startswith(args.lang): code = "\n".join(code.split("\n")[1:])
            Path(filename).write_text(code)
            print(f"✓ Code saved to {filename}")
    else:
        result = v2c.speak_and_code(args.lang, args.save, args.file)
        if "error" in result:
            print(result["error"])
            sys.exit(1)

    print(f"\n{'='*60}")
    print(result['code'])
    print(f"{'='*60}\n")

    if 'saved_to' in result:
        print(f"✓ Code saved to {result['saved_to']}")

if __name__ == "__main__":
    main()
