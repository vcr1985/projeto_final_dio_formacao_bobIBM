"""
Comando /trilha
Recebe o nome de uma tecnologia e retorna o plano de estudos da trilha
lido a partir de data/trilhas_Deal.json.
"""

import json
import os
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "trilhas_Deal.json"


def carregar_trilhas(caminho: Path = DATA_FILE) -> list:
    """Carrega e retorna a lista de trilhas do arquivo JSON."""
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados.get("trilhas", [])


def buscar_trilha(tecnologia: str, trilhas: list) -> dict | None:
    """Busca (case-insensitive) uma trilha pelo nome ou tecnologia."""
    termo = tecnologia.strip().lower()
    for trilha in trilhas:
        if termo in trilha.get("tecnologia", "").lower() or termo in trilha.get("nome", "").lower():
            return trilha
    return None


def formatar_plano(trilha: dict) -> str:
    """Formata o plano de estudos de uma trilha em Markdown."""
    promo = trilha.get("promocoes", {})
    vitalicio = "✅ Sim" if promo.get("vitalicio") else "❌ Não"
    lives = "\n".join(f"- {live}" for live in trilha.get("lives_ao_vivo", []))

    modulos_lista = "\n".join(
        f"  {i+1}. Módulo {i+1} — {trilha['tecnologia'].split('/')[0].strip()}"
        for i in range(trilha.get("numero_de_modulos", 0))
    )

    return f"""
# 📚 Plano de Estudos — {trilha['nome']}

| Campo             | Detalhe                        |
|-------------------|--------------------------------|
| 🏷️ Tecnologia     | {trilha['tecnologia']}         |
| 📊 Nível          | {trilha['nivel']}              |
| 📦 Módulos        | {trilha['numero_de_modulos']}  |
| ⭐ XP Total        | {trilha['xp_total']} XP       |
| 🎓 Vagas          | {trilha['beds_disponiveis']}   |

## 💰 Promoção
- Vitalício: {vitalicio}
- Preço original: R$ {promo.get('preco_original', 'N/A')}
- Preço promocional: R$ {promo.get('preco_promocional', 'N/A')} ({promo.get('desconto_percentual', 0)}% OFF)

## 🗂️ Módulos do Plano
{modulos_lista}

## 📺 Lives ao Vivo Incluídas
{lives}

---
> 🔗 Acesse: https://www.dio.me
""".strip()


def executar(tecnologia: str, caminho: Path = DATA_FILE) -> str:
    """Ponto de entrada do comando /trilha."""
    if not tecnologia or not tecnologia.strip():
        return "❌ Informe o nome de uma tecnologia. Exemplo: /trilha Java"
    trilhas = carregar_trilhas(caminho)
    trilha = buscar_trilha(tecnologia, trilhas)
    if not trilha:
        nomes = "\n".join(f"- {t['nome']}" for t in trilhas)
        return f"❌ Trilha '{tecnologia}' não encontrada.\n\n**Trilhas disponíveis:**\n{nomes}"
    return formatar_plano(trilha)
