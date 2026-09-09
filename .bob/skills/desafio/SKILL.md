---
name: desafio
description: Use when the user types /desafio followed by a technology and optional level — generates a random fictional coding challenge based on the chosen technology and level.
metadata:
  argument-hint: "[tecnologia] [nivel?]"
  disable-model-invocation: true
---

# /desafio — Gerador de Desafio de Código

## Objetivo
Gerar um desafio de código aleatório e fictício com base na tecnologia e nível escolhidos pelo utilizador.

## Passos

1. **Extrair argumentos**
   - Argumento 1 (obrigatório): tecnologia (ex: Python, Java, React)
   - Argumento 2 (opcional): nível — `Básico`, `Intermediário` ou `Avançado`. Se não fornecido, escolhe aleatoriamente.

2. **Selecionar categoria do desafio**
   Escolhe aleatoriamente uma das categorias abaixo conforme o nível:

   - **Básico:** algoritmos simples, manipulação de strings, loops, condicionais
   - **Intermediário:** estruturas de dados, APIs, CRUD, autenticação, padrões de projeto
   - **Avançado:** concorrência, otimização, design patterns avançados, sistemas distribuídos, segurança

3. **Gerar o desafio** no seguinte formato Markdown:

```
# ⚔️ Desafio de Código — <tecnologia>

| Campo       | Detalhe           |
|-------------|-------------------|
| 🏷️ Tecnologia | <tecnologia>    |
| 📊 Nível     | <nivel>          |
| 🎲 Categoria  | <categoria>     |
| ⭐ XP        | <xp gerado aleatoriamente entre 500 e 5000> |
| ⏱️ Tempo     | <tempo estimado: 30min / 1h / 2h / 4h> |

## 📋 Descrição
<Descrição clara e objetiva do desafio, com 3 a 5 frases explicando o problema a resolver>

## ✅ Requisitos
- <requisito 1>
- <requisito 2>
- <requisito 3>
- (adicione mais conforme o nível)

## 💡 Dicas
- <dica 1 coerente com a tecnologia>
- <dica 2>

## 📥 Exemplo de Entrada
<Exemplo de input esperado pelo programa/função>

## 📤 Exemplo de Saída
<Exemplo de output esperado>

## 🏆 Critérios de Avaliação
- Funcionamento correto
- Código limpo e legível
- Boas práticas da tecnologia escolhida
- (adicione critérios extras conforme o nível)

---
> 💬 Boa sorte! Compartilhe sua solução na DIO: https://www.dio.me
```

4. **Exibir o desafio formatado** na resposta do chat.
   - Cada chamada ao comando deve gerar um desafio diferente (varia categoria, enunciado e exemplos).
