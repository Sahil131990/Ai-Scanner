from openai import OpenAI

client = OpenAI()

def generate_tests(code):

    prompt = f"""
    Generate JUnit test cases for this Java code

    {code}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content