---
name: certificado
description: Use when the user types /certificado followed by their name and a track name — generates a fictional DIO completion certificate in Markdown format.
metadata:
  argument-hint: "[nome do usuario] | [nome da trilha]"
  disable-model-invocation: true
---

# /certificado — Gerador de Certificado Fictício DIO

## Objetivo
Gerar um certificado fictício de conclusão em Markdown com o nome do utilizador e a trilha concluída.

## Passos

1. **Extrair argumentos**
   - Argumento 1 (obrigatório): nome do utilizador (ex: João Silva)
   - Argumento 2 (obrigatório): nome da trilha (ex: Python, React, AWS)
   - Se algum argumento estiver em falta, peça ao utilizador antes de continuar.

2. **Ler o ficheiro de dados** (opcional para enriquecer)
   - Use `read_file` em `projeto_final_Deal_Explorer/data/trilhas_Deal.json` para buscar detalhes da trilha (tecnologia, módulos, XP).
   - Se a trilha não for encontrada, continue com os dados fornecidos pelo utilizador.

3. **Gerar o certificado** no seguinte formato Markdown:

```
---

<div align="center">

# 🎓 CERTIFICADO DE CONCLUSÃO

### Digital Innovation One — DIO
🔗 [www.dio.me](https://www.dio.me)

---

## Certificamos que

# <NOME DO UTILIZADOR EM MAIÚSCULAS>

concluiu com êxito a trilha de formação:

## 📚 <Nome da Trilha>

**Tecnologia:** <tecnologia>
**Nível:** <nivel>
**Módulos concluídos:** <numero_de_modulos>
**XP conquistado:** <xp_total> XP

---

📅 **Data de emissão:** <data atual no formato DD/MM/AAAA>
🔐 **Código de verificação:** <gerar código aleatório no formato DIO-XXXX-XXXX-XXXX usando letras maiúsculas e números>

---

> *Este certificado é fictício e foi gerado para fins educacionais e de demonstração.*
> *Emitido pelo Deal Explorer — Projeto Final DIO Formação IBM Bob*

</div>

---
```

4. **Salvar o certificado** como ficheiro Markdown:
   - Caminho: `projeto_final_Deal_Explorer/docs/certificados/<nome_sem_espacos>_<trilha_sem_espacos>_certificado.md`
   - Use `write_file` para criar o ficheiro (substitua espaços por `_` no nome do ficheiro).

5. **Confirmar ao utilizador** que o certificado foi gerado e exibir o conteúdo completo no chat.
