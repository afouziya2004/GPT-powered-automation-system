from openai_client import src.generate_response

def summarize_meeting(notes):
    prompt = f"""
Summarize the following meeting notes into key points.

Requirements:
- Keep it concise
- Highlight important updates
- Use bullet points

Meeting Notes:
{notes}
"""
    return generate_response(prompt)


# Test block
if __name__ == "__main__":
    sample_notes = """
    Max: Profits up 50%
    Ruby: New servers are online
    Kyle: Need more time to fix software
    Walker: Happy to help
    Parkman: Beta testing almost done
    """

    result = summarize_meeting(sample_notes)
    print(result)
