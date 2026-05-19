from openai import OpenAI

from schemas.settings import settings

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)


def analyze_error(error: str):
    content = f"""
    Você é um especialista em análise de erros de programação.
    Analise o seguinte erro e retorne:
    1. Explicação simples do que é esse erro
    2. Causa provável
    3. Como corrigir com exemplo de código

    Erro: {error}
    """

    response = client.chat.completions.create(
        model="llama3.2", messages=[{"role": "user", "content": content}]
    )
    return response.choices[0].message.content
