---
name: trilha
description: Use when the user types /trilha followed by a technology name — reads data/trilhas_Deal.json and returns a formatted study plan for that track.
metadata:
  argument-hint: "[tecnologia]"
  disable-model-invocation: true
---

# /trilha — Plano de Estudos DIO

## Objetivo
Ler o ficheiro `projeto_final_Deal_Explorer/data/trilhas_Deal.json` e apresentar um plano de estudos detalhado para a tecnologia pedida.

## Passos

1. **Ler o ficheiro de dados**
   - Use `read_file` para carregar `projeto_final_Deal_Explorer/data/trilhas_Deal.json`.

2. **Localizar a trilha**
   - Procura no array `trilhas` a entrada cujo campo `tecnologia` ou `nome` contenha (case-insensitive) o argumento passado pelo utilizador.
   - Se nenhuma for encontrada, informe o utilizador e liste as tecnologias disponíveis.

3. **Formatar o plano de estudos**
   Apresenta o resultado no seguinte formato Markdown:

```
# 📚 Plano de Estudos — <nome da trilha>

| Campo              | Detalhe                          |
|--------------------|----------------------------------|
| 🏷️ Tecnologia      | <tecnologia>                     |
| 📊 Nível           | <nivel>                          |
| 📦 Módulos         | <numero_de_modulos>              |
| ⭐ XP Total         | <xp_total> XP                   |
| 🎓 Vagas           | <beds_disponiveis>               |

## 💰 Promoção
- Vitalício: <sim/não>
- Preço original: R$ <preco_original>
- Preço promocional: R$ <preco_promocional> (<desconto_percentual>% OFF)

## 🎯 Módulos do Plano
Liste <numero_de_modulos> módulos fictícios numerados e coerentes com a tecnologia, criados por você com base no nível e tecnologia da trilha. Exemplo:
  1. Fundamentos de <tecnologia>
  2. Configuração do ambiente
  3. ...

## 📺 Lives ao Vivo
- <live 1>
- <live 2>
- <live 3>

---
> 🔗 Acesse em: https://www.dio.me
```

4. **Exibir o plano formatado** na resposta do chat.
