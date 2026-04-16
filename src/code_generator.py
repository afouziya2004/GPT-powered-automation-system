from openai_client import generate_response

def generate_eda_code():
    prompt = """
Generate Python code for Exploratory Data Analysis using:
- pandas
- matplotlib
- seaborn

Include:
1. Loading dataset
2. Basic info (head, info, describe)
3. Handling missing values
4. Correlation heatmap
5. Histogram plots

Make code clean and ready to run.
"""

    return generate_response(prompt)


# Test block
if __name__ == "__main__":
    result = generate_eda_code()
    print(result)
