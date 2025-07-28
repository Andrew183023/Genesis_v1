# 🧠 Genesis v1 – Sistema Operacional do Flow Core Group

Genesis é o orquestrador modular que conecta a FlowMind (IA principal) aos módulos do ecossistema Flow.

## 🚀 Como rodar

### 1. Configure o arquivo `.env` na raiz:

```
OPENAI_API_KEY=sua-chave-da-openai-aqui
```

Ou use o `.env.example` como base.

### 2. Rode com Docker Compose:

```bash
docker-compose up --build
```

### 3. Acesse:

- Terminal Genesis: abra `index.html` no navegador
- API Genesis: http://localhost:8000
- API FlowMind: http://localhost:8001

## 🧩 Estrutura

- `genesis/`: corpo operacional (recebe comandos)
- `flowmind/`: IA pensante (GPT-3.5-Turbo)
- `index.html`: painel terminal simples

## 📦 Pronto para publicação!
