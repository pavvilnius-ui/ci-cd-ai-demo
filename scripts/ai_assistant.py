import os
from openai import OpenAI

def analyze_logs(log_path):
    if not os.path.exists(log_path):
        print("No logs found.")
        return

    with open(log_path, "r") as f:
        logs = f.read()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ No OpenAI API key found. Please set OPENAI_API_KEY in GitHub Secrets.")
        return

    client = OpenAI(api_key=api_key)

    print("=== AI Assistant Analysis (via OpenAI) ===")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant that analyzes CI/CD pipeline errors and suggests fixes. "
                        "Always provide a complete, ready-to-use code snippet if a test is failing."
                    )
                },
                {
                    "role": "user",
                    "content": f"Here are the CI/CD logs:\n\n{logs}\n\nExplain the error and provide the corrected test code completely."
                }
            ],
            max_tokens=350
        )

        # Print GPT suggestion
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"⚠️ Error calling OpenAI API: {e}")

    print("==========================================")

if __name__ == "__main__":
    analyze_logs("failed_pipeline.log")
