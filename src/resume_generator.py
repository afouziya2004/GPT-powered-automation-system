from openai_client import generate_response

def generate_resume(paragraph):
    prompt = f"""
Convert the following paragraph into a professional resume.

Include:
- Name (if not given, keep placeholder)
- Summary
- Skills
- Projects
- Education

Make it clean, structured, and professional.

Paragraph:
{paragraph}
"""

    return generate_response(prompt)


# Test block
if __name__ == "__main__":
    sample_input = """
I am a computer science student skilled in Python, AI, and data analysis.
I have built machine learning and NLP projects and I am interested in AI development.
"""

    result = generate_resume(sample_input)
    print(result)v
