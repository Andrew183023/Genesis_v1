from fastapi import FastAPI
import requests

app = FastAPI()

FLOWMIND_URL = "http://flowmind:8001/api/ia/processar"

@app.post("/genesis/comando")
def comando_geral(payload: dict):
    prompt = payload.get("prompt", "Nenhum prompt recebido")

    try:
        resposta = requests.post(FLOWMIND_URL, json={"prompt": prompt})
        resposta_json = resposta.json()
        return {"resposta_da_flowmind": resposta_json["resposta"]}

    except Exception as e:
        return {"erro": str(e)}
