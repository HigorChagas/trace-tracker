from openai import OpenAI

from schemas.settings import settings

client = OpenAI(
    base_url=settings.ai_host,
    api_key="ollama",
)


def analyze_error(error: str):
    content = f"""
    Você é um especialista em análise de erros de programação Python.
    Baseie-se estritamente na linguagem Python real: nunca invente funções,
    métodos, parâmetros ou sintaxes que não existem. Se não tiver certeza
    de algo, não afirme como fato.

    Analise o erro abaixo e responda organizando o conteúdo EXATAMENTE nestas
    4 seções, nesta ordem, cada uma iniciada por um cabeçalho markdown "## "
    com o título exato indicado (sem seções extras, sem texto antes da primeira seção):

    ## Erros
    Explicação simples do que é esse erro.

    ## Causas possíveis
    As causas mais prováveis desse erro ter ocorrido.

    ## Como corrigir
    Como corrigir, com exemplo de código. Todo bloco de código deve usar
    a sintaxe markdown de bloco cercado com a linguagem indicada, assim:
    ```python
    codigo aqui
    ```

    ## Onde investigar
    Em quais pontos do código ou do fluxo vale a pena investigar primeiro.

    Erro: {error}
    """

    response = client.chat.completions.create(
        model=settings.ai_model,
        messages=[{"role": "user", "content": content}],
        temperature=0.2,
    )
    return response.choices[0].message.content
