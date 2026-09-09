Interpreta `$ARGUMENTS` para extrair:
- **nome do utilizador** (obrigatório): primeiro bloco de texto antes do `|` ou vírgula
- **nome da trilha** (obrigatório): bloco após o separador `|` ou vírgula

Se algum dos dois estiver em falta, pede ao utilizador antes de continuar.

Lê o ficheiro `projeto_final_Deal_Explorer/data/trilhas_Deal.json` e busca a trilha pelo nome ou tecnologia para enriquecer o certificado (módulos, XP, tecnologia, nível). Se não encontrar, usa apenas os dados fornecidos pelo utilizador.

Gera o certificado no seguinte formato Markdown e exibe no chat:

---

<div align="center">

# 🎓 CERTIFICADO DE CONCLUSÃO

### Digital Innovation One — DIO
🔗 [www.dio.me](https://www.dio.me)

---

## Certificamos que

# {NOME DO UTILIZADOR EM MAIÚSCULAS}

concluiu com êxito a trilha de formação:

## 📚 {Nome da Trilha}

| Campo               | Detalhe                  |
|---------------------|--------------------------|
| 🏷️ Tecnologia       | {tecnologia}             |
| 📊 Nível            | {nivel}                  |
| 📦 Módulos Concluídos | {numero_de_modulos}    |
| ⭐ XP Conquistado    | {xp_total} XP            |

---

📅 **Data de Emissão:** {data atual no formato DD/MM/AAAA}
🔐 **Código de Verificação:** DIO-{4 caracteres aleatórios maiúsculos/números}-{4 caracteres}-{4 caracteres}

---

*Este certificado é fictício e foi gerado para fins educacionais.*
*Emitido pelo Deal Explorer — Projeto Final DIO Formação IBM Bob*

</div>

---

Depois de exibir no chat, salva o certificado como ficheiro usando `write_file` no caminho:
`projeto_final_Deal_Explorer/docs/certificados/{nome_sem_espacos}_{trilha_sem_espacos}_certificado.md`

(Substitui espaços por `_` e remove caracteres especiais no nome do ficheiro.)

Confirma ao utilizador que o ficheiro foi salvo e indica o caminho completo.
