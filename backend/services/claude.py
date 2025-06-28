import os
import anthropic
client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
def generate_mvp_code(idea_description: str):
    prompt = f"""
You are a startup MVP generator. Based on the user's idea, generate an interactive prototype using HTML and JavaScript only.
User idea: {idea_description}
Return ONLY the complete HTML code with inline CSS and JS.
"""
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

