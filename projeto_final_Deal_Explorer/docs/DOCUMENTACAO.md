# 📚 Deal Explorer — Documentação Completa do Projeto

> Projeto Final — Formação IBM Bob | DIO - Digital Innovation One
> Repositório: https://github.com/vcr1985/projeto_final_dio_formacao_bobIBM

---

## Índice

1. [Visão Geral](#visão-geral)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Histórico de Commits](#histórico-de-commits)
4. [Prompts Utilizados](#prompts-utilizados)
5. [Funcionalidades](#funcionalidades)
   - [Slash Commands Bob](#slash-commands-bob)
   - [Módulos Python](#módulos-python)
   - [Testes Unitários](#testes-unitários)
   - [MCP Server](#mcp-server)
6. [Guia de Uso](#guia-de-uso)
7. [Dicas e Boas Práticas](#dicas-e-boas-práticas)
8. [Insights para Futuros Usuários](#insights-para-futuros-usuários)
9. [Referências](#referências)

---

## Visão Geral

O **Deal Explorer** é um projeto educacional construído do zero usando o **IBM Bob** — o assistente de IA da IBM integrado ao VSCode. O objetivo foi demonstrar, na prática, como um desenvolvedor pode usar o Bob para:

- Configurar um repositório Git do zero
- Criar e organizar a estrutura de um projeto
- Gerar dados fictícios estruturados (JSON)
- Criar slash commands personalizados
- Implementar módulos Python com lógica de negócio
- Escrever testes unitários automatizados
- Construir e registrar um servidor MCP (Model Context Protocol)

Todo o projeto foi construído **exclusivamente por meio de prompts em linguagem natural** dentro do chat do Bob — sem digitar uma única linha de código manualmente.

---

## Estrutura do Projeto

```
projeto_final_dio_formacao_bobIBM/
│
├── .bob/                              # Configurações locais do Bob
│   ├── commands/                      # Slash commands do projeto
│   │   ├── trilha.md                  → /trilha
│   │   ├── desafio.md                 → /desafio
│   │   └── certificado.md             → /certificado
│   ├── skills/                        # Skills (auto-invocáveis)
│   │   ├── trilha/SKILL.md
│   │   ├── desafio/SKILL.md
│   │   └── certificado/SKILL.md
│   └── mcp.json                       # Registro do MCP server local
│
├── .bobignore                         # Arquivos/pastas ignorados pelo Bob
├── Hello_world.md                     # Primeiro arquivo do projeto
│
└── projeto_final_Deal_Explorer/
    ├── CRC/                           # Cards de Responsabilidade de Classe
    ├── data/
    │   └── trilhas_Deal.json          # 30 trilhas fictícias da DIO
    ├── commands/                      # Módulos Python dos comandos
    │   ├── trilha.py
    │   ├── desafio.py
    │   └── certificado.py
    ├── docs/
    │   └── certificados/              # Certificados gerados em Markdown
    ├── mcp/                           # Servidor MCP (TypeScript/Node.js)
    │   ├── src/index.ts               # Código-fonte do servidor
    │   ├── build/index.js             # Build compilado (executável)
    │   ├── package.json
    │   ├── tsconfig.json
    │   └── README.md
    └── tests/
        ├── test_commands.py           # 46 testes unitários
        └── resultado_testes.txt       # Relatório de execução
```

---

## Histórico de Commits

| Commit | Mensagem | O que foi feito |
|--------|----------|-----------------|
| `179229f` | Add Hello_world.md | Primeiro arquivo criado e enviado |
| `a9ec7bf` | Add projeto_final_Deal_Explorer structure | Estrutura de pastas criada |
| `205a87c` | Add trilhas_Deal.json with 30 fictional DIO tracks | JSON com 30 trilhas fictícias |
| `ff1469f` | Add .bobignore | Regras de ignore para o Bob |
| `5bc1ad3` | Add slash commands as Bob skills | Skills auto-invocáveis criadas |
| `f65479a` | Add slash commands to .bob/commands/ | Slash commands `/trilha`, `/desafio`, `/certificado` |
| `890e39c` | Add Python modules and unit tests (46 tests, 100%) | Módulos + testes unitários |
| `b07176c` | Add MCP server with stdio + HTTP/SSE/API | Servidor MCP completo |

---

## Prompts Utilizados

Esta seção registra os prompts reais usados para construir cada parte do projeto.

---

### 🔧 Configuração de Git

```
configure o git globalmente para usar o credential.helper garantindo que as
credenciais fiquem salvas de forma persistente no ambiente local do usuário
e não em nenhum arquivo de projetos.
```

**Resultado:** `git config --global credential.helper store`

---

### 📁 Clonagem e Estrutura

```
https://github.com/vcr1985/projeto_final_dio_formacao_bobIBM.git
```
> Apenas colar a URL foi suficiente para o Bob entender que deveria clonar o repositório.

```
quero que dentro do repositório clonado vc crie um arquivo MD chamado
Hello world e que tenha apenas essa mensagem
```

```
agora quero que vc suba para meu repositório remoto
```

```
quero que vc entre dentro da pasta recentemente clonada e crie a seguinte
estrutura de projetos: projeto final Deal Explorer, dentro vai ter pasta com
CRC, data, commands, mcp e docs
```

---

### 📊 Dados JSON

```
dentro da pasta data crie um arquivo chamado trilhas Deal.json
```

```
dentro do arquivo trilha deal json cria uma lista extensa e detalhada de
pelo menos 30 trilhas fictícias da Dio, www.dio.me contendo nome, tecnologia,
nível, número de módulos, xp total, beds disponíveis, promoções, vitalícios
e lives ao vivo
```

---

### 🚫 Configuração de Ignore

```
quero que na raiz do projeto recém clonado você crie um arquivo Bob ignore
e dentro do bob ignore quero que ele seja ignorado as pastas no módulos,
Arquivos, pastas como data, cache, progresso e certificados gerados,
docs certificados emitidos e de quaisquer outros arquivos com extensão TMP
```

---

### ⚡ Slash Commands e Skills

```
bob crie um Slash command chamado /trilha, que recebe o nome de uma
tecnologia e retorna a partir do arquivo data/trilhas.json um plano de estudos
formatado com os módulos daquela trilha, depois crie outro slash command
chamado /desafio que gera um desafio de código aleatório baseado no nível e
tecnologia escolhida pelo usuário, e por fim um último slash command chamado
/certificado que gera um certificado fictício em markdown com o nome do usuário
e a trilha por ele concluída.
```

> O segundo prompt foi usado para criar especificamente os arquivos em `.bob/commands/` (distinção entre Skills e Commands):

```
Bob crie um Slash command dentro do projeto que possa ser invocado pelo
comando /trilha [...] todos esses Slash commands têm que ficar armazenados
de forma local para ser executado apenas neste projeto, mas devo visualizá-los
aqui no chat do Bob
```

---

### 🧪 Testes Unitários

```
Bob crie arquivos de testes unitários e teste estes Fluxo para atingir uma
cobertura de 70% da aprovação, teste os comandos /trilha para consultar trilhas
de JAVA, Gere um arquivo de /desafio para o aluno e um /certificado para o
mesmo, grave os resultados em um arquivo txt para acompanharmos.
```

**Resultado:** 46 testes, 100% de aprovação, relatório em `tests/resultado_testes.txt`

---

### 🤖 MCP Server

```
Bob quero que vc crie um MCP server do projeto recém clonado para que
futuramente pessoas possam vir acessar por um servidor https ou sso ou via
API, use a pasta MCP para isso
```

---

### 📖 Documentação

```
Bob gostaria que você documentasse todo o projeto feito até o momento, com
todos os prompts usados, modos de uso, dicas e insights para futuros usuários
que vão aprender
```

---

## Funcionalidades

### Slash Commands Bob

Digitando `/` no chat do Bob dentro deste workspace, aparecem 3 comandos:

#### `/trilha [tecnologia]`

Consulta o arquivo `trilhas_Deal.json` e retorna um plano de estudos completo.

**Exemplo:**
```
/trilha Java
```

**Saída esperada:**
```markdown
# 📚 Plano de Estudos — Formação Java Developer
| Campo       | Detalhe        |
|-------------|----------------|
| Tecnologia  | Java           |
| Nível       | Intermediário  |
| Módulos     | 12             |
| XP Total    | 18500 XP       |
| Vagas       | 350            |
...
```

---

#### `/desafio [tecnologia] [nivel?]`

Gera um desafio de código aleatório com descrição, requisitos, dicas e exemplos.

**Exemplos:**
```
/desafio Java Intermediário
/desafio Python
/desafio React Avançado
```

---

#### `/certificado [nome] | [trilha]`

Gera um certificado fictício em Markdown, exibe no chat e salva em `docs/certificados/`.

**Exemplo:**
```
/certificado João Silva | Java Developer
```

**Saída esperada:**
```markdown
# 🎓 CERTIFICADO DE CONCLUSÃO
### Digital Innovation One — DIO
## Certificamos que
# JOÃO SILVA
concluiu com êxito: Formação Java Developer
...
📅 Data: 09/09/2026
🔐 Código: DIO-A3K1-B7Z2-C9X4
```

---

### Módulos Python

Cada comando tem um módulo Python independente em `commands/`:

| Arquivo | Função principal | Descrição |
|---------|-----------------|-----------|
| [`trilha.py`](../commands/trilha.py) | `executar(tecnologia)` | Lê JSON e retorna plano formatado |
| [`desafio.py`](../commands/desafio.py) | `executar(tecnologia, nivel)` | Gera desafio aleatório |
| [`certificado.py`](../commands/certificado.py) | `executar(nome, trilha)` | Gera e salva certificado |

**Uso via Python:**
```python
from commands import trilha, desafio, certificado

# Consultar trilha Java
print(trilha.executar("Java"))

# Gerar desafio
print(desafio.executar("Python", "Básico"))

# Gerar certificado
conteudo, caminho = certificado.executar("João Silva", "Java Developer")
print(f"Salvo em: {caminho}")
```

---

### Testes Unitários

**Executar todos os testes:**
```bash
cd projeto_final_Deal_Explorer
python3 tests/test_commands.py
```

**Resultado esperado:**
```
Total de testes  : 46
Aprovados        : 46
Taxa de aprovação: 100.0%
Status           : ✅ META ATINGIDA
```

**Cobertura por módulo:**

| Módulo | Testes | Casos cobertos |
|--------|--------|----------------|
| `trilha.py` | 13 | Carga JSON, busca, formatação, erros |
| `desafio.py` | 14 | Níveis, aleatoriedade, XP, formatação |
| `certificado.py` | 19 | Código único, busca, formatação, salvamento |

---

### MCP Server

O servidor MCP expõe as 3 ferramentas via protocolo MCP, suportando dois modos:

#### Modo stdio (Bob local)
Registrado automaticamente em `.bob/mcp.json`. O Bob carrega o servidor ao abrir o workspace.

#### Modo HTTP/SSE (acesso remoto)

```bash
cd projeto_final_Deal_Explorer/mcp
MCP_TRANSPORT=http PORT=3333 node build/index.js
```

**Endpoints disponíveis:**

| Método | Rota | Parâmetros (JSON body) |
|--------|------|------------------------|
| `GET` | `/health` | — |
| `GET` | `/sse` | — (stream SSE) |
| `POST` | `/tool/trilha` | `{"tecnologia": "Java"}` |
| `POST` | `/tool/desafio` | `{"tecnologia": "Python", "nivel": "Básico"}` |
| `POST` | `/tool/certificado` | `{"nome_aluno": "João", "nome_trilha": "Java"}` |

**Proteção por API Key:**
```bash
MCP_TRANSPORT=http API_KEY=minha-chave-secreta node build/index.js

# Uso com API Key
curl -X POST http://localhost:3333/tool/trilha \
  -H "x-api-key: minha-chave-secreta" \
  -H "Content-Type: application/json" \
  -d '{"tecnologia": "Java"}'
```

**Build do servidor:**
```bash
cd mcp
npm install
npm run build
```

---

## Guia de Uso

### Pré-requisitos

| Ferramenta | Versão mínima | Para que serve |
|-----------|---------------|---------------|
| Git | 2.x | Controle de versão |
| Python | 3.10+ | Módulos e testes |
| Node.js | 18+ | MCP Server |
| IBM Bob | Qualquer | IDE + IA |

### Passo a passo: começar do zero

```bash
# 1. Clonar o repositório
git clone https://github.com/vcr1985/projeto_final_dio_formacao_bobIBM.git

# 2. Abrir no Bob (VSCode)
code projeto_final_dio_formacao_bobIBM

# 3. Buildar o MCP server
cd projeto_final_Deal_Explorer/mcp
npm install && npm run build

# 4. Executar os testes
cd ..
python3 tests/test_commands.py

# 5. Usar os slash commands no chat do Bob
# Digite / no chat para ver os comandos disponíveis
```

---

## Dicas e Boas Práticas

### 💡 Sobre prompts com o Bob

1. **Seja específico no escopo** — "dentro da pasta X, crie Y" é melhor que "crie Y".
2. **Uma coisa de cada vez** — prompts focados geram resultados mais precisos que prompts longos com múltiplas tarefas simultâneas.
3. **Confirme antes de enviar** — peça ao Bob para mostrar o que vai fazer antes de executar ações destrutivas.
4. **Use referências de arquivo** — mencionar `@arquivo.py` no chat carrega o contexto exato do arquivo.
5. **Revisar antes do push** — sempre peça `mostre a árvore do diretório` para confirmar o que foi criado antes de enviar ao GitHub.

### 🗂️ Sobre organização de projetos Bob

- **`.bob/commands/`** → slash commands invocados manualmente com `/`
- **`.bob/skills/`** → skills auto-invocadas pelo Bob quando o contexto bate
- **`.bob/mcp.json`** → registro de servidores MCP locais ao workspace
- **`.bobignore`** → similar ao `.gitignore`, mas para o Bob — impede que ele leia pastas desnecessárias (reduz consumo de contexto)

### 🧪 Sobre testes

- Sempre passe o caminho do arquivo JSON como parâmetro nos testes — nunca dependa do path absoluto hardcoded.
- Use `tempfile.NamedTemporaryFile` para criar fixtures isoladas em testes.
- Grave os resultados em `.txt` para rastreabilidade — facilita auditorias de qualidade.

### 🤖 Sobre o MCP Server

- Use **modo stdio** para desenvolvimento local com o Bob.
- Use **modo HTTP** apenas quando precisar expor para outros sistemas.
- Nunca commite a `API_KEY` no código — use variáveis de ambiente.
- O arquivo `build/index.js` deve ser commited (é o artefato que o Bob executa). O `node_modules/` nunca.

---

## Insights para Futuros Usuários

### 🚀 O que este projeto demonstra

Este projeto é uma prova de conceito de **desenvolvimento guiado por IA**. Todos os arquivos foram gerados pelo Bob a partir de descrições em linguagem natural. Isso demonstra:

1. **O Bob entende contexto acumulado** — cada prompt se apoiou nos arquivos criados anteriormente sem precisar repetir tudo.
2. **Prompts em português funcionam** — não é necessário usar inglês para obter resultados de qualidade.
3. **O Bob mantém consistência** — os módulos Python, os testes e o servidor MCP todos referenciam o mesmo `trilhas_Deal.json` de forma consistente.
4. **IA + Git = rastreabilidade total** — cada decisão ficou registrada no histórico de commits com mensagens claras.

### 🧠 Padrões aprendidos

| Padrão | Prompt de exemplo | Resultado |
|--------|------------------|-----------|
| Criar estrutura de pastas | "crie a seguinte estrutura..." | `mkdir -p` com `.gitkeep` |
| Gerar dados fictícios | "crie uma lista com pelo menos 30..." | JSON detalhado e coerente |
| Criar comandos reutilizáveis | "crie um slash command que..." | `.bob/commands/*.md` |
| Testes automatizados | "crie testes com 70% de cobertura" | unittest com fixtures |
| Servidor de integração | "crie um MCP server com suporte a HTTP" | TypeScript + Express |

### ⚠️ Armadilhas comuns

| Problema | Causa | Solução |
|----------|-------|---------|
| Bob não encontra o slash command | Workspace errado aberto | Abrir a pasta `projeto_final_dio_formacao_bobIBM` no Bob |
| MCP server não conecta | Build não executado | `cd mcp && npm run build` |
| Testes falham com ModuleNotFoundError | `sys.path` errado | Executar da pasta `projeto_final_Deal_Explorer` |
| `.bobignore` bloqueia leitura de arquivos | Padrão muito amplo (ex: `data/`) | Ser mais específico: `data/cache/` |
| Credenciais Git pedidas a cada push | `credential.helper` não configurado | `git config --global credential.helper store` |

### 🎓 Próximos passos sugeridos

Para evoluir este projeto, experimente estes prompts:

```
# Adicionar autenticação JWT ao MCP server
Bob adicione autenticação JWT ao servidor MCP, com endpoint /login
que recebe usuário e senha e retorna um token

# Interface web
Bob crie uma interface web simples em HTML/CSS/JS que consome os
endpoints do MCP server e exibe as trilhas em cards

# Banco de dados
Bob substitua o arquivo JSON por um banco SQLite, mantendo a mesma
API dos módulos Python

# CI/CD
Bob crie um workflow GitHub Actions que execute os testes unitários
automaticamente a cada push na branch main

# Novos dados
Bob adicione mais 20 trilhas ao arquivo trilhas_Deal.json,
focadas em DevOps e Cloud
```

---

## Referências

| Recurso | Link |
|---------|------|
| IBM Bob — Documentação oficial | https://www.ibm.com/docs/bob |
| DIO - Digital Innovation One | https://www.dio.me |
| Model Context Protocol (MCP) | https://modelcontextprotocol.io |
| MCP SDK npm | https://www.npmjs.com/package/@modelcontextprotocol/sdk |
| Repositório deste projeto | https://github.com/vcr1985/projeto_final_dio_formacao_bobIBM |

---

*Documentação gerada pelo IBM Bob — Projeto Final Formação IBM Bob | DIO*
*Data: Setembro de 2026*
