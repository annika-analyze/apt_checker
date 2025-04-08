import google.generativeai as genai


def generate_response(prompt: str, model, api_key) -> str:
    """
    Generates a response from the LLM using the provided prompt.
    """

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt)

    return response.text
