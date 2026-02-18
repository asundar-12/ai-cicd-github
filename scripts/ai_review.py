from google import genai
import sys

client = genai.Client()


def _extract_text(response) -> str:
    """Extract text from response, including thought parts (gemini-2.5 uses thinking)."""
    if response.text:
        return response.text
    # Fallback: extract all text parts including thoughts (response.text skips them)
    if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
        return "".join(
            p.text or ""
            for p in response.candidates[0].content.parts
            if isinstance(getattr(p, "text", None), str)
        )
    return ""


def review_code(code: str) -> str:
    prompt = f"{code}\n\nPlease review the code for security, bugs, performance."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return _extract_text(response) or "(No review text returned - check prompt_feedback for blocks)"


def main():
    if len(sys.argv) > 1:
        diff_file = sys.argv[1]
        with open(diff_file, "r") as f:
            diff_content = f.read()
    else:
        diff_content = sys.stdin.read()
    review = review_code(diff_content)
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    if output_file:
        with open(output_file, "w") as f:
            f.write(review)
    else:
        print(review, flush=True)


if __name__ == "__main__":
    main()