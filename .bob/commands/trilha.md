Lê o ficheiro `projeto_final_Deal_Explorer/data/trilhas_Deal.json`.

Procura no array `trilhas` a entrada cujo campo `tecnologia` ou `nome` contenha (sem distinção de maiúsculas/minúsculas) o valor de `$ARGUMENTS`.

Se nenhuma trilha for encontrada, informa o utilizador e lista os nomes de todas as trilhas disponíveis no ficheiro.

Se encontrada, apresenta o seguinte plano de estudos formatado em Markdown:

---

# 📚 Plano de Estudos — {nome}

| Campo             | Detalhe                  |
|-------------------|--------------------------|
| 🏷️ Tecnologia     | {tecnologia}             |
| 📊 Nível          | {nivel}                  |
| 📦 Módulos        | {numero_de_modulos}      |
| ⭐ XP Total        | {xp_total} XP            |
| 🎓 Vagas          | {beds_disponiveis}       |

## 💰 Promoção
- Vitalício: {sim ou não conforme o campo vitalicio}
- Preço original: R$ {preco_original}
- Preço promocional: R$ {preco_promocional} ({desconto_percentual}% OFF)

## 🗂️ Módulos do Plano
Cria uma lista numerada de {numero_de_modulos} módulos fictícios e coerentes com a tecnologia e nível da trilha. Exemplo para nível Básico:
  1. Introdução e configuração do ambiente
  2. Fundamentos da linguagem
  3. ...

## 📺 Lives ao Vivo Incluídas
{lista as lives_ao_vivo da trilha, uma por linha com bullet}

---
> 🔗 Acesse: https://www.dio.me
