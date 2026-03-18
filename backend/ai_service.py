from openai import OpenAI
import config


client = OpenAI(api_key=config.OPENAI_API_KEY)

def fix_issues(issues):

    prompt = f"""
    Fix these sonar issues in Java code

    {issues}

    Return corrected code.
    """

    response = client.chat.completions.create(
        model=config.MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
