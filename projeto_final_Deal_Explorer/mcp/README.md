# Deal Explorer MCP Server

Servidor MCP que expõe as ferramentas `/trilha`, `/desafio` e `/certificado` do projeto DIO Deal Explorer.

Suporta dois modos de transporte:
- **stdio** — padrão, usado pelo Bob localmente
- **HTTP/SSE + REST API** — para acesso remoto via HTTPS, SSO ou integração com outras ferramentas

---

## 🚀 Instalação

```bash
cd mcp
npm install
npm run build
```

---

## 🔧 Uso

### Modo stdio (Bob local)
```bash
node build/index.js
```

### Modo HTTP (servidor remoto)
```bash
MCP_TRANSPORT=http PORT=3333 node build/index.js
```

### Com proteção por API Key
```bash
MCP_TRANSPORT=http PORT=3333 API_KEY=minha-chave-secreta node build/index.js
```

---

## 🌐 Endpoints HTTP

| Método | Endpoint           | Descrição                            |
|--------|--------------------|--------------------------------------|
| GET    | `/health`          | Health check do servidor             |
| GET    | `/sse`             | Stream SSE para clientes MCP remotos |
| POST   | `/tool/trilha`     | Consulta plano de estudos            |
| POST   | `/tool/desafio`    | Gera desafio de código               |
| POST   | `/tool/certificado`| Gera certificado fictício            |

### Exemplos via curl

```bash
# Trilha Java
curl -X POST http://localhost:3333/tool/trilha \
  -H "Content-Type: application/json" \
  -d '{"tecnologia": "Java"}'

# Desafio Python Intermediário
curl -X POST http://localhost:3333/tool/desafio \
  -H "Content-Type: application/json" \
  -d '{"tecnologia": "Python", "nivel": "Intermediário"}'

# Certificado
curl -X POST http://localhost:3333/tool/certificado \
  -H "Content-Type: application/json" \
  -d '{"nome_aluno": "João Silva", "nome_trilha": "Java Developer"}'

# Com API Key
curl -X POST http://localhost:3333/tool/trilha \
  -H "Content-Type: application/json" \
  -H "x-api-key: minha-chave-secreta" \
  -d '{"tecnologia": "React"}'
```

---

## 🔐 Autenticação

| Método    | Como usar                                                        |
|-----------|------------------------------------------------------------------|
| API Key   | Header `x-api-key: <chave>` ou query `?api_key=<chave>`         |
| SSO/HTTPS | Configure um proxy reverso (nginx, Caddy, Cloudflare) na frente |

---

## 🤖 Registrar no Bob (mcp.json)

```json
{
  "mcpServers": {
    "deal-explorer": {
      "command": "node",
      "args": ["/caminho/absoluto/mcp/build/index.js"],
      "env": {}
    }
  }
}
```

---

## 🛠️ Ferramentas expostas

| Tool          | Parâmetros                              | Descrição                              |
|---------------|-----------------------------------------|----------------------------------------|
| `trilha`      | `tecnologia: string`                    | Plano de estudos a partir do JSON      |
| `desafio`     | `tecnologia: string`, `nivel?: string`  | Desafio de código aleatório            |
| `certificado` | `nome_aluno: string`, `nome_trilha: string` | Certificado fictício em Markdown  |
