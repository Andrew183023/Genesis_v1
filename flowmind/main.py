from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# ⚙️ Criação da aplicação FastAPI
app = FastAPI()

# 💡 Configuração da chave da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class Prompt(BaseModel):
    prompt: str

@app.post("/api/ia/processar")
def processar_ia(dados: Prompt):
    pensamento = dados.prompt

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é a FlowMind, a mente estratégica do Flow Core Group."},
                {"role": "user", "content": pensamento}
            ],
            max_tokens=200
        )

        resposta_gerada = resposta['choices'][0]['message']['content']
        return {"resposta": resposta_gerada}

    except Exception as e:
        return {"erro": str(e)}

