# 🚀 Deal Explorer — Projeto Final DIO Formação IBM Bob

> Construído 100% com prompts em linguagem natural usando o **IBM Bob**

[![DIO](https://img.shields.io/badge/DIO-Digital%20Innovation%20One-blueviolet)](https://www.dio.me)
[![IBM Bob](https://img.shields.io/badge/IBM-Bob%20AI-blue)](https://www.ibm.com)
[![Python](https://img.shields.io/badge/Python-3.12-yellow)](https://www.python.org)
[![Node.js](https://img.shields.io/badge/Node.js-22-green)](https://nodejs.org)
[![Tests](https://img.shields.io/badge/Tests-46%20passed%20100%25-brightgreen)]()

---

## 🎯 Sobre o Projeto

O **Deal Explorer** é uma plataforma fictícia de exploração de trilhas educacionais da DIO.  
Todo o projeto foi construído do zero usando apenas o **IBM Bob** — sem digitar código manualmente.

### O que foi construído:

| Componente | Tecnologia | Descrição |
|---|---|---|
| 📊 Dados | JSON | 30 trilhas fictícias da DIO com XP, promoções e lives |
| ⚡ Slash Commands | Markdown + Bob | `/trilha`, `/desafio`, `/certificado` |
| 🐍 Módulos | Python 3.12 | Lógica de negócio dos 3 comandos |
| 🧪 Testes | unittest | 46 testes, 100% de aprovação |
| 🤖 MCP Server | TypeScript + Node.js | Servidor com suporte a stdio, HTTP/SSE e API REST |

---

## ⚡ Início Rápido

```bash
# Clonar o repositório
git clone https://github.com/vcr1985/projeto_final_dio_formacao_bobIBM.git
cd projeto_final_dio_formacao_bobIBM

# Buildar o MCP server
cd projeto_final_Deal_Explorer/mcp
npm install && npm run build

# Executar os testes
cd ..
python3 tests/test_commands.py
```

---

## 📁 Estrutura

```
├── .bob/
│   ├── commands/        ← Slash commands (/trilha, /desafio, /certificado)
│   ├── skills/          ← Skills auto-invocáveis
│   └── mcp.json         ← Registro do servidor MCP
├── .bobignore           ← Regras de ignore para o Bob
└── projeto_final_Deal_Explorer/
    ├── data/
    │   └── trilhas_Deal.json   ← 30 trilhas fictícias
    ├── commands/               ← Módulos Python
    ├── docs/
    │   └── DOCUMENTACAO.md     ← Documentação completa
    ├── mcp/                    ← Servidor MCP
    └── tests/                  ← 46 testes unitários
```

---

## 💬 Slash Commands

Abra o projeto no Bob e digite `/` no chat:

| Comando | Exemplo | Descrição |
|---|---|---|
| `/trilha` | `/trilha Java` | Plano de estudos da trilha |
| `/desafio` | `/desafio Python Intermediário` | Desafio de código aleatório |
| `/certificado` | `/certificado João Silva \| Java` | Certificado fictício em Markdown |

---

## 🤖 MCP Server — Acesso via API

```bash
# Iniciar em modo HTTP
cd projeto_final_Deal_Explorer/mcp
MCP_TRANSPORT=http PORT=3333 node build/index.js

# Exemplo: consultar trilha Java via curl
curl -X POST http://localhost:3333/tool/trilha \
  -H "Content-Type: application/json" \
  -d '{"tecnologia": "Java"}'
```

Endpoints: `/health` · `/sse` · `/tool/trilha` · `/tool/desafio` · `/tool/certificado`

---

## 📖 Documentação Completa

Consulte [`docs/DOCUMENTACAO.md`](projeto_final_Deal_Explorer/docs/DOCUMENTACAO.md) para:

- Todos os prompts utilizados
- Guia de uso detalhado
- Dicas e boas práticas
- Insights para futuros usuários
- Próximos passos sugeridos

---

## 🧪 Testes

```bash
cd projeto_final_Deal_Explorer
python3 tests/test_commands.py
```

```
Total de testes  : 46
Aprovados        : 46
Taxa de aprovação: 100.0%
Status           : ✅ META ATINGIDA
```

---

*Projeto Final — Formação IBM Bob | DIO — Setembro de 2026*
