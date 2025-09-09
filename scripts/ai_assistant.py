import os
import openai

log_file = os.getenv("PIPELINE_LOG", "failed_pipeline.log")

with open(log_file, "r") as f:
    log_text = f.read()

prompt = f"""Analyze this CI/CD pipeline error and suggest a fix in simple language:

{log_text}
"""

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

suggestion = response.choices[0].message["content"]
print("=== AI SUGGESTION ===")
print(suggestion)
