"""
Comando /certificado
Gera um certificado fictício em Markdown para o aluno e a trilha concluída.
"""

import json
import random
import string
import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "trilhas_Deal.json"
CERTIFICADOS_DIR = Path(__file__).parent.parent / "docs" / "certificados"


def _codigo_verificacao() -> str:
    """Gera um código aleatório no formato DIO-XXXX-XXXX-XXXX."""
    chars = string.ascii_uppercase + string.digits
    partes = ["".join(random.choices(chars, k=4)) for _ in range(3)]
    return "DIO-" + "-".join(partes)


def buscar_trilha_por_nome(nome_trilha: str, caminho: Path = DATA_FILE) -> dict | None:
    """Busca detalhes de uma trilha no JSON pelo nome ou tecnologia."""
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
        termo = nome_trilha.strip().lower()
        for t in dados.get("trilhas", []):
            if termo in t.get("nome", "").lower() or termo in t.get("tecnologia", "").lower():
                return t
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None


def gerar_certificado(nome_aluno: str, nome_trilha: str, caminho_dados: Path = DATA_FILE) -> dict:
    """Gera os dados do certificado."""
    trilha = buscar_trilha_por_nome(nome_trilha, caminho_dados)
    data_emissao = datetime.date.today().strftime("%d/%m/%Y")
    codigo = _codigo_verificacao()

    return {
        "nome_aluno": nome_aluno.strip(),
        "nome_trilha": trilha["nome"] if trilha else nome_trilha.strip(),
        "tecnologia": trilha["tecnologia"] if trilha else "N/A",
        "nivel": trilha["nivel"] if trilha else "N/A",
        "modulos": trilha["numero_de_modulos"] if trilha else "N/A",
        "xp_total": trilha["xp_total"] if trilha else "N/A",
        "data_emissao": data_emissao,
        "codigo": codigo,
    }


def formatar_certificado(dados: dict) -> str:
    """Formata o certificado em Markdown."""
    return f"""<div align="center">

# 🎓 CERTIFICADO DE CONCLUSÃO

### Digital Innovation One — DIO
🔗 [www.dio.me](https://www.dio.me)

---

## Certificamos que

# {dados['nome_aluno'].upper()}

concluiu com êxito a trilha de formação:

## 📚 {dados['nome_trilha']}

| Campo                 | Detalhe                |
|-----------------------|------------------------|
| 🏷️ Tecnologia         | {dados['tecnologia']}  |
| 📊 Nível              | {dados['nivel']}       |
| 📦 Módulos Concluídos | {dados['modulos']}     |
| ⭐ XP Conquistado      | {dados['xp_total']} XP |

---

📅 **Data de Emissão:** {dados['data_emissao']}
🔐 **Código de Verificação:** {dados['codigo']}

---

*Este certificado é fictício e foi gerado para fins educacionais.*
*Emitido pelo Deal Explorer — Projeto Final DIO Formação IBM Bob*

</div>""".strip()


def salvar_certificado(conteudo: str, nome_aluno: str, nome_trilha: str,
                       destino: Path = CERTIFICADOS_DIR) -> Path:
    """Salva o certificado como arquivo Markdown e retorna o caminho."""
    destino.mkdir(parents=True, exist_ok=True)
    nome_arquivo = f"{'_'.join(nome_aluno.split())}_{nome_trilha.replace(' ', '_')}_certificado.md"
    caminho = destino / nome_arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)
    return caminho


def executar(nome_aluno: str, nome_trilha: str,
             caminho_dados: Path = DATA_FILE,
             destino: Path = CERTIFICADOS_DIR) -> tuple[str, Path]:
    """
    Ponto de entrada do comando /certificado.
    Retorna (conteudo_markdown, caminho_arquivo_salvo).
    """
    if not nome_aluno or not nome_aluno.strip():
        return "❌ Informe seu nome. Exemplo: /certificado João Silva | Java Developer", None
    if not nome_trilha or not nome_trilha.strip():
        return "❌ Informe a trilha concluída. Exemplo: /certificado João Silva | Java Developer", None

    dados = gerar_certificado(nome_aluno, nome_trilha, caminho_dados)
    conteudo = formatar_certificado(dados)
    caminho = salvar_certificado(conteudo, nome_aluno, nome_trilha, destino)
    return conteudo, caminho
