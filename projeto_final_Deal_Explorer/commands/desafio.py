"""
Comando /desafio
Gera um desafio de código aleatório baseado na tecnologia e nível escolhidos.
"""

import random
import datetime

CATEGORIAS_POR_NIVEL = {
    "básico": ["Algoritmos", "Manipulação de Strings", "Loops e Condicionais", "Funções Básicas"],
    "intermediário": ["Estruturas de Dados", "APIs REST", "CRUD", "Autenticação", "Padrões de Projeto"],
    "avançado": ["Concorrência", "Otimização de Performance", "Design Patterns Avançados", "Sistemas Distribuídos", "Segurança"],
}

TEMPOS_POR_NIVEL = {
    "básico": "30 minutos",
    "intermediário": "1 hora",
    "avançado": "2 a 4 horas",
}

DESAFIOS_BASE = [
    {
        "titulo": "Calculadora de XP",
        "descricao": "Crie uma função que recebe uma lista de módulos concluídos e calcula o XP total acumulado pelo aluno.",
        "entrada": "[100, 250, 500, 150]",
        "saida": "XP Total: 1000",
    },
    {
        "titulo": "Filtro de Trilhas",
        "descricao": "Implemente uma função que filtra trilhas por nível a partir de uma lista de objetos JSON.",
        "entrada": '[{"nome":"Java","nivel":"Intermediário"},{"nome":"Python","nivel":"Básico"}]\nnivel: "Básico"',
        "saida": '[{"nome":"Python","nivel":"Básico"}]',
    },
    {
        "titulo": "Gerador de Certificado",
        "descricao": "Crie uma função que recebe nome do aluno e trilha concluída e retorna uma string formatada de certificado.",
        "entrada": 'nome="João Silva", trilha="Java Developer"',
        "saida": "CERTIFICADO: João Silva concluiu Java Developer em 01/01/2025",
    },
    {
        "titulo": "Buscador de Promoções",
        "descricao": "Dada uma lista de trilhas com preços, retorne apenas as que possuem desconto acima de 30%.",
        "entrada": '[{"nome":"Java","desconto":40},{"nome":"Go","desconto":20}]',
        "saida": '[{"nome":"Java","desconto":40}]',
    },
    {
        "titulo": "Ranking de Trilhas por XP",
        "descricao": "Ordene uma lista de trilhas pelo campo xp_total em ordem decrescente.",
        "entrada": '[{"nome":"Java","xp":18500},{"nome":"Python","xp":14200},{"nome":"ML","xp":32000}]',
        "saida": '[{"nome":"ML","xp":32000},{"nome":"Java","xp":18500},{"nome":"Python","xp":14200}]',
    },
]


def gerar_desafio(tecnologia: str, nivel: str = "") -> dict:
    """Gera os dados de um desafio aleatório."""
    nivel_norm = nivel.strip().lower() if nivel else random.choice(list(CATEGORIAS_POR_NIVEL.keys()))
    if nivel_norm not in CATEGORIAS_POR_NIVEL:
        nivel_norm = "intermediário"

    categoria = random.choice(CATEGORIAS_POR_NIVEL[nivel_norm])
    base = random.choice(DESAFIOS_BASE)
    xp = random.randint(500, 5000)
    tempo = TEMPOS_POR_NIVEL[nivel_norm]

    return {
        "tecnologia": tecnologia,
        "nivel": nivel_norm.capitalize(),
        "categoria": categoria,
        "xp": xp,
        "tempo": tempo,
        "titulo": base["titulo"],
        "descricao": base["descricao"],
        "entrada": base["entrada"],
        "saida": base["saida"],
    }


def formatar_desafio(dados: dict) -> str:
    """Formata os dados do desafio em Markdown."""
    return f"""
# ⚔️ Desafio de Código — {dados['tecnologia']}

| Campo          | Detalhe                  |
|----------------|--------------------------|
| 🏷️ Tecnologia  | {dados['tecnologia']}    |
| 📊 Nível       | {dados['nivel']}         |
| 🎲 Categoria   | {dados['categoria']}     |
| ⭐ XP           | {dados['xp']} XP        |
| ⏱️ Tempo Est.  | {dados['tempo']}         |

## 📋 {dados['titulo']}
{dados['descricao']}

## ✅ Requisitos
- Implemente a solução em {dados['tecnologia']}
- O código deve ser legível e bem comentado
- Utilize boas práticas da linguagem
- Trate casos de entrada vazia ou inválida

## 💡 Dicas
- Consulte a documentação oficial de {dados['tecnologia']}
- Comece pelo caso mais simples antes de generalizar

## 📥 Exemplo de Entrada
```
{dados['entrada']}
```

## 📤 Exemplo de Saída Esperada
```
{dados['saida']}
```

## 🏆 Critérios de Avaliação
- Funcionamento correto conforme os exemplos
- Código limpo e legível
- Boas práticas de {dados['tecnologia']}
- Cobertura de casos extremos (edge cases)

---
> 💬 Boa sorte! Compartilhe sua solução: https://www.dio.me
""".strip()


def executar(tecnologia: str, nivel: str = "") -> str:
    """Ponto de entrada do comando /desafio."""
    if not tecnologia or not tecnologia.strip():
        return "❌ Informe a tecnologia. Exemplo: /desafio Java Intermediário"
    dados = gerar_desafio(tecnologia, nivel)
    return formatar_desafio(dados)
