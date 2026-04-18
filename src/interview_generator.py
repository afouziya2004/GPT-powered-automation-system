from src.openai_client import generate_response

def generate_interview_questions(language):
    prompt = f"""
Generate 10 interview questions for {language} programming language.

Requirements:
- Suitable for freshers
- Mix of theory + coding
- Clear and concise
"""

    return generate_response(prompt)


# Test block
if __name__ == "__main__":
    result = generate_interview_questions("Python")
    print(result)
