from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/api/ia/processar")
def processar_ia(dados: Prompt):
    pensamento = dados.prompt
    resposta_gerada = f"Aqui é a FlowMind processando: '{pensamento}'"
    return {"resposta": resposta_gerada}
