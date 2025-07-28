# 🌐 Genesis v1 – Sistema Operacional Modular do Flow Core Group

**Genesis v1** é o primeiro deploy oficial do corpo operacional do Flow Core Group.  
Ele atua como orquestrador entre todos os módulos e conecta diretamente com a **FlowMind**, a mente de IA central do ecossistema.

> “A mente pensa. O corpo executa. Juntos, eles criam vida.”  
> — Flow Core Protocol

---

## ⚙️ Componentes Ativos

### 🔹 Genesis (FastAPI – Porta 8000)
- Recebe comandos externos
- Orquestra os módulos
- Conecta-se à FlowMind via API REST

### 🔹 FlowMind (FastAPI – Porta 8001)
- Processa o pensamento (IA simples mock ou GPT real)
- Retorna comandos inteligentes para o Genesis

---

## 🚀 Como Rodar (via Docker Compose)

### 1. Clone o repositório

```bash
git clone https://github.com/Andrew183023/Genesis_v1.git
cd Genesis_v1
