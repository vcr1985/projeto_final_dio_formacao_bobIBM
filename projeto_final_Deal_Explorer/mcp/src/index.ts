#!/usr/bin/env node
/**
 * Deal Explorer MCP Server
 * ========================
 * Expõe as ferramentas /trilha, /desafio e /certificado via MCP.
 *
 * Transports suportados:
 *   - stdio  (padrão — usado pelo Bob localmente)
 *   - HTTP/SSE (MCP_TRANSPORT=http — para acesso remoto via HTTPS ou API)
 *
 * Variáveis de ambiente:
 *   MCP_TRANSPORT  "stdio" | "http"   (default: stdio)
 *   PORT           número de porta    (default: 3333)
 *   API_KEY        chave de acesso    (opcional — protege o endpoint HTTP)
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import crypto from "crypto";

// ---------------------------------------------------------------------------
// Helpers de caminho
// ---------------------------------------------------------------------------
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Arquivo de dados relativo à pasta mcp/build → sobe 3 níveis até projeto_final_Deal_Explorer
const DATA_FILE = path.resolve(__dirname, "..", "..", "data", "trilhas_Deal.json");
const CERTIFICADOS_DIR = path.resolve(__dirname, "..", "..", "docs", "certificados");

// ---------------------------------------------------------------------------
// Leitura do JSON de trilhas
// ---------------------------------------------------------------------------
function carregarTrilhas(): any[] {
  const raw = fs.readFileSync(DATA_FILE, "utf-8");
  return JSON.parse(raw).trilhas ?? [];
}

function buscarTrilha(termo: string, trilhas: any[]): any | null {
  const t = termo.trim().toLowerCase();
  return trilhas.find(
    (x) =>
      x.tecnologia?.toLowerCase().includes(t) ||
      x.nome?.toLowerCase().includes(t)
  ) ?? null;
}

// ---------------------------------------------------------------------------
// Lógica /trilha
// ---------------------------------------------------------------------------
function executarTrilha(tecnologia: string): string {
  if (!tecnologia.trim()) return "❌ Informe a tecnologia. Ex: trilha Java";
  const trilhas = carregarTrilhas();
  const trilha = buscarTrilha(tecnologia, trilhas);
  if (!trilha) {
    const lista = trilhas.map((t: any) => `- ${t.nome}`).join("\n");
    return `❌ Trilha '${tecnologia}' não encontrada.\n\n**Disponíveis:**\n${lista}`;
  }
  const promo = trilha.promocoes ?? {};
  const vitalicio = promo.vitalicio ? "✅ Sim" : "❌ Não";
  const lives = (trilha.lives_ao_vivo ?? []).map((l: string) => `- ${l}`).join("\n");
  const modulos = Array.from({ length: trilha.numero_de_modulos }, (_, i) =>
    `  ${i + 1}. Módulo ${i + 1} — ${trilha.tecnologia.split("/")[0].trim()}`
  ).join("\n");

  return `# 📚 Plano de Estudos — ${trilha.nome}

| Campo            | Detalhe                        |
|------------------|--------------------------------|
| 🏷️ Tecnologia    | ${trilha.tecnologia}           |
| 📊 Nível         | ${trilha.nivel}                |
| 📦 Módulos       | ${trilha.numero_de_modulos}    |
| ⭐ XP Total       | ${trilha.xp_total} XP         |
| 🎓 Vagas         | ${trilha.beds_disponiveis}     |

## 💰 Promoção
- Vitalício: ${vitalicio}
- Preço original: R$ ${promo.preco_original}
- Preço promocional: R$ ${promo.preco_promocional} (${promo.desconto_percentual}% OFF)

## 🗂️ Módulos do Plano
${modulos}

## 📺 Lives ao Vivo
${lives}

---
> 🔗 https://www.dio.me`;
}

// ---------------------------------------------------------------------------
// Lógica /desafio
// ---------------------------------------------------------------------------
const CATEGORIAS: Record<string, string[]> = {
  "básico": ["Algoritmos", "Manipulação de Strings", "Loops e Condicionais"],
  "intermediário": ["Estruturas de Dados", "APIs REST", "CRUD", "Autenticação"],
  "avançado": ["Concorrência", "Otimização", "Design Patterns", "Segurança"],
};
const TEMPOS: Record<string, string> = {
  "básico": "30 minutos",
  "intermediário": "1 hora",
  "avançado": "2 a 4 horas",
};
const DESAFIOS_BASE = [
  {
    titulo: "Calculadora de XP",
    descricao: "Implemente uma função que recebe uma lista de módulos concluídos e calcula o XP total acumulado.",
    entrada: "[100, 250, 500, 150]",
    saida: "XP Total: 1000",
  },
  {
    titulo: "Filtro de Trilhas por Nível",
    descricao: "Crie uma função que filtra trilhas de um array JSON pelo campo 'nivel'.",
    entrada: '[{"nome":"Java","nivel":"Intermediário"},{"nome":"Python","nivel":"Básico"}], nivel: "Básico"',
    saida: '[{"nome":"Python","nivel":"Básico"}]',
  },
  {
    titulo: "Ranking por XP",
    descricao: "Ordene um array de trilhas pelo campo xp_total em ordem decrescente.",
    entrada: '[{"nome":"ML","xp":32000},{"nome":"Java","xp":18500}]',
    saida: '[{"nome":"ML","xp":32000},{"nome":"Java","xp":18500}]',
  },
];

function executarDesafio(tecnologia: string, nivel: string): string {
  if (!tecnologia.trim()) return "❌ Informe a tecnologia. Ex: desafio Java Intermediário";
  const nivelNorm = nivel.trim().toLowerCase() || ["básico", "intermediário", "avançado"][Math.floor(Math.random() * 3)];
  const nivelValido = CATEGORIAS[nivelNorm] ? nivelNorm : "intermediário";
  const categoria = CATEGORIAS[nivelValido][Math.floor(Math.random() * CATEGORIAS[nivelValido].length)];
  const base = DESAFIOS_BASE[Math.floor(Math.random() * DESAFIOS_BASE.length)];
  const xp = Math.floor(Math.random() * 4501) + 500;
  const tempo = TEMPOS[nivelValido];

  return `# ⚔️ Desafio de Código — ${tecnologia}

| Campo          | Detalhe                  |
|----------------|--------------------------|
| 🏷️ Tecnologia  | ${tecnologia}            |
| 📊 Nível       | ${nivelValido.charAt(0).toUpperCase() + nivelValido.slice(1)} |
| 🎲 Categoria   | ${categoria}             |
| ⭐ XP           | ${xp} XP                |
| ⏱️ Tempo Est.  | ${tempo}                 |

## 📋 ${base.titulo}
${base.descricao}

## ✅ Requisitos
- Implemente em ${tecnologia}
- Código limpo e bem comentado
- Boas práticas da linguagem
- Trate entradas inválidas

## 💡 Dicas
- Consulte a documentação oficial de ${tecnologia}
- Comece pelo caso mais simples

## 📥 Exemplo de Entrada
\`\`\`
${base.entrada}
\`\`\`

## 📤 Saída Esperada
\`\`\`
${base.saida}
\`\`\`

---
> 💬 Boa sorte! https://www.dio.me`;
}

// ---------------------------------------------------------------------------
// Lógica /certificado
// ---------------------------------------------------------------------------
function codigoVerificacao(): string {
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  const parte = () => Array.from({ length: 4 }, () => chars[Math.floor(Math.random() * chars.length)]).join("");
  return `DIO-${parte()}-${parte()}-${parte()}`;
}

function executarCertificado(nomeAluno: string, nomeTrilha: string): { markdown: string; caminhoSalvo: string } {
  const trilhas = carregarTrilhas();
  const trilha = buscarTrilha(nomeTrilha, trilhas);
  const hoje = new Date().toLocaleDateString("pt-BR");
  const codigo = codigoVerificacao();

  const tecnologia = trilha?.tecnologia ?? "N/A";
  const nivel = trilha?.nivel ?? "N/A";
  const modulos = trilha?.numero_de_modulos ?? "N/A";
  const xp = trilha?.xp_total ?? "N/A";
  const trilhaNome = trilha?.nome ?? nomeTrilha;

  const markdown = `<div align="center">

# 🎓 CERTIFICADO DE CONCLUSÃO

### Digital Innovation One — DIO
🔗 [www.dio.me](https://www.dio.me)

---

## Certificamos que

# ${nomeAluno.toUpperCase()}

concluiu com êxito a trilha de formação:

## 📚 ${trilhaNome}

| Campo                 | Detalhe        |
|-----------------------|----------------|
| 🏷️ Tecnologia         | ${tecnologia}  |
| 📊 Nível              | ${nivel}       |
| 📦 Módulos Concluídos | ${modulos}     |
| ⭐ XP Conquistado      | ${xp} XP      |

---

📅 **Data de Emissão:** ${hoje}
🔐 **Código de Verificação:** ${codigo}

---

*Certificado fictício gerado para fins educacionais.*
*Deal Explorer — Projeto Final DIO Formação IBM Bob*

</div>`;

  // Salva o arquivo
  fs.mkdirSync(CERTIFICADOS_DIR, { recursive: true });
  const nomeArquivo = `${nomeAluno.replace(/\s+/g, "_")}_${nomeTrilha.replace(/\s+/g, "_")}_certificado.md`;
  const caminhoSalvo = path.join(CERTIFICADOS_DIR, nomeArquivo);
  fs.writeFileSync(caminhoSalvo, markdown, "utf-8");

  return { markdown, caminhoSalvo };
}

// ---------------------------------------------------------------------------
// Instância do servidor MCP
// ---------------------------------------------------------------------------
const server = new McpServer({
  name: "deal-explorer-mcp",
  version: "1.0.0",
});

// --- Tool: trilha ---
server.tool(
  "trilha",
  "Retorna o plano de estudos de uma trilha DIO a partir do arquivo trilhas_Deal.json",
  {
    tecnologia: z.string().describe("Nome da tecnologia ou trilha. Ex: Java, Python, React"),
  },
  async ({ tecnologia }) => ({
    content: [{ type: "text", text: executarTrilha(tecnologia) }],
  })
);

// --- Tool: desafio ---
server.tool(
  "desafio",
  "Gera um desafio de código aleatório baseado na tecnologia e nível escolhidos",
  {
    tecnologia: z.string().describe("Tecnologia do desafio. Ex: Java, Python"),
    nivel: z.string().optional().describe("Nível: Básico | Intermediário | Avançado (opcional)"),
  },
  async ({ tecnologia, nivel }) => ({
    content: [{ type: "text", text: executarDesafio(tecnologia, nivel ?? "") }],
  })
);

// --- Tool: certificado ---
server.tool(
  "certificado",
  "Gera e salva um certificado fictício em Markdown para o aluno e a trilha concluída",
  {
    nome_aluno: z.string().describe("Nome completo do aluno"),
    nome_trilha: z.string().describe("Nome ou tecnologia da trilha concluída. Ex: Java Developer"),
  },
  async ({ nome_aluno, nome_trilha }) => {
    if (!nome_aluno.trim()) {
      return { content: [{ type: "text", text: "❌ Informe o nome do aluno." }], isError: true };
    }
    if (!nome_trilha.trim()) {
      return { content: [{ type: "text", text: "❌ Informe a trilha concluída." }], isError: true };
    }
    const { markdown, caminhoSalvo } = executarCertificado(nome_aluno, nome_trilha);
    return {
      content: [
        { type: "text", text: markdown },
        { type: "text", text: `\n\n📄 Certificado salvo em: ${caminhoSalvo}` },
      ],
    };
  }
);

// ---------------------------------------------------------------------------
// Bootstrap — stdio (padrão) ou HTTP/SSE
// ---------------------------------------------------------------------------
const transport = process.env.MCP_TRANSPORT ?? "stdio";
const PORT = parseInt(process.env.PORT ?? "3333", 10);
const API_KEY = process.env.API_KEY ?? "";

async function startStdio(): Promise<void> {
  const t = new StdioServerTransport();
  await server.connect(t);
  console.error("✅ deal-explorer-mcp running on stdio");
}

async function startHttp(): Promise<void> {
  const { default: express } = await import("express");
  const { default: cors } = await import("cors");

  const app = express();
  app.use(cors());
  app.use(express.json());

  // Middleware de autenticação por API Key (opcional)
  app.use((req, res, next) => {
    if (!API_KEY) return next();
    const key = req.headers["x-api-key"] ?? req.query["api_key"];
    if (key !== API_KEY) {
      res.status(401).json({ error: "Unauthorized — invalid or missing API key" });
      return;
    }
    next();
  });

  // Endpoint de health-check
  app.get("/health", (_req, res) => {
    res.json({ status: "ok", server: "deal-explorer-mcp", version: "1.0.0" });
  });

  // Endpoint SSE — mantém conexão aberta para clientes MCP remotos
  app.get("/sse", async (req, res) => {
    res.setHeader("Content-Type", "text/event-stream");
    res.setHeader("Cache-Control", "no-cache");
    res.setHeader("Connection", "keep-alive");
    res.flushHeaders();

    // Envia capabilities imediatamente
    const caps = {
      tools: ["trilha", "desafio", "certificado"],
      server: "deal-explorer-mcp",
      version: "1.0.0",
    };
    res.write(`data: ${JSON.stringify({ type: "capabilities", payload: caps })}\n\n`);

    req.on("close", () => {
      console.error("SSE client disconnected");
    });
  });

  // Endpoint REST — chama tools diretamente via POST JSON
  app.post("/tool/:name", async (req, res) => {
    const { name } = req.params;
    const args = req.body ?? {};
    try {
      let result: string;
      if (name === "trilha") {
        result = executarTrilha(args.tecnologia ?? "");
      } else if (name === "desafio") {
        result = executarDesafio(args.tecnologia ?? "", args.nivel ?? "");
      } else if (name === "certificado") {
        const { markdown, caminhoSalvo } = executarCertificado(args.nome_aluno ?? "", args.nome_trilha ?? "");
        res.json({ success: true, markdown, caminhoSalvo });
        return;
      } else {
        res.status(404).json({ error: `Tool '${name}' not found. Available: trilha, desafio, certificado` });
        return;
      }
      res.json({ success: true, result });
    } catch (err) {
      res.status(500).json({ error: String(err) });
    }
  });

  app.listen(PORT, () => {
    console.error(`✅ deal-explorer-mcp HTTP server running on port ${PORT}`);
    console.error(`   Health : http://localhost:${PORT}/health`);
    console.error(`   SSE    : http://localhost:${PORT}/sse`);
    console.error(`   API    : POST http://localhost:${PORT}/tool/<name>`);
    if (API_KEY) console.error(`   🔐 API Key protection enabled`);
  });
}

if (transport === "http") {
  startHttp().catch((e) => { console.error(e); process.exit(1); });
} else {
  startStdio().catch((e) => { console.error(e); process.exit(1); });
}
