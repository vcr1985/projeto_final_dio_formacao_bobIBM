"""
Testes unitários — Deal Explorer Slash Commands
Cobre os fluxos: /trilha (Java), /desafio e /certificado
Meta: ≥ 70% de cobertura de aprovação
"""

import sys
import os
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Garante que o pacote commands é encontrado
sys.path.insert(0, str(Path(__file__).parent.parent))

import commands.trilha as cmd_trilha
import commands.desafio as cmd_desafio
import commands.certificado as cmd_certificado

# ---------------------------------------------------------------------------
# Fixture — JSON mínimo para testes
# ---------------------------------------------------------------------------
TRILHAS_FIXTURE = {
    "plataforma": "DIO - Digital Innovation One",
    "url": "https://www.dio.me",
    "trilhas": [
        {
            "id": 1,
            "nome": "Formação Java Developer",
            "tecnologia": "Java",
            "nivel": "Intermediário",
            "numero_de_modulos": 12,
            "xp_total": 18500,
            "beds_disponiveis": 350,
            "promocoes": {
                "vitalicio": True,
                "desconto_percentual": 40,
                "preco_original": 199.90,
                "preco_promocional": 119.90
            },
            "lives_ao_vivo": [
                "Introdução ao Java 21",
                "Design Patterns na prática",
                "Spring Boot do Zero"
            ]
        },
        {
            "id": 2,
            "nome": "Formação Python Developer",
            "tecnologia": "Python",
            "nivel": "Básico",
            "numero_de_modulos": 10,
            "xp_total": 14200,
            "beds_disponiveis": 500,
            "promocoes": {
                "vitalicio": True,
                "desconto_percentual": 50,
                "preco_original": 179.90,
                "preco_promocional": 89.90
            },
            "lives_ao_vivo": [
                "Python para Iniciantes",
                "Automação com Python",
                "APIs com FastAPI"
            ]
        }
    ]
}


def criar_json_temp() -> Path:
    """Cria um arquivo JSON temporário com a fixture e retorna o Path."""
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    )
    json.dump(TRILHAS_FIXTURE, tmp, ensure_ascii=False)
    tmp.close()
    return Path(tmp.name)


# ===========================================================================
# TESTES — /trilha
# ===========================================================================
class TestComandoTrilha(unittest.TestCase):

    def setUp(self):
        self.json_path = criar_json_temp()

    def tearDown(self):
        os.unlink(self.json_path)

    # --- carregar_trilhas ---
    def test_carregar_trilhas_retorna_lista(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        self.assertIsInstance(trilhas, list)
        self.assertEqual(len(trilhas), 2)

    def test_carregar_trilhas_arquivo_inexistente(self):
        with self.assertRaises(FileNotFoundError):
            cmd_trilha.carregar_trilhas(Path("/nao/existe.json"))

    # --- buscar_trilha ---
    def test_buscar_trilha_java_encontrada(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        resultado = cmd_trilha.buscar_trilha("Java", trilhas)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nome"], "Formação Java Developer")

    def test_buscar_trilha_case_insensitive(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        resultado = cmd_trilha.buscar_trilha("jAvA", trilhas)
        self.assertIsNotNone(resultado)

    def test_buscar_trilha_por_nome_parcial(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        resultado = cmd_trilha.buscar_trilha("python", trilhas)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["tecnologia"], "Python")

    def test_buscar_trilha_inexistente_retorna_none(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        resultado = cmd_trilha.buscar_trilha("COBOL", trilhas)
        self.assertIsNone(resultado)

    # --- formatar_plano ---
    def test_formatar_plano_contém_nome_trilha(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        trilha = cmd_trilha.buscar_trilha("Java", trilhas)
        plano = cmd_trilha.formatar_plano(trilha)
        self.assertIn("Formação Java Developer", plano)

    def test_formatar_plano_contém_xp(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        trilha = cmd_trilha.buscar_trilha("Java", trilhas)
        plano = cmd_trilha.formatar_plano(trilha)
        self.assertIn("18500", plano)

    def test_formatar_plano_contém_lives(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        trilha = cmd_trilha.buscar_trilha("Java", trilhas)
        plano = cmd_trilha.formatar_plano(trilha)
        self.assertIn("Introdução ao Java 21", plano)

    def test_formatar_plano_contém_promocao_vitalicia(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        trilha = cmd_trilha.buscar_trilha("Java", trilhas)
        plano = cmd_trilha.formatar_plano(trilha)
        self.assertIn("Sim", plano)

    def test_formatar_plano_número_de_módulos(self):
        trilhas = cmd_trilha.carregar_trilhas(self.json_path)
        trilha = cmd_trilha.buscar_trilha("Java", trilhas)
        plano = cmd_trilha.formatar_plano(trilha)
        self.assertIn("12", plano)

    # --- executar ---
    def test_executar_java_retorna_plano(self):
        resultado = cmd_trilha.executar("Java", self.json_path)
        self.assertIn("Formação Java Developer", resultado)

    def test_executar_tecnologia_vazia_retorna_erro(self):
        resultado = cmd_trilha.executar("", self.json_path)
        self.assertIn("❌", resultado)

    def test_executar_tecnologia_nao_encontrada_lista_disponiveis(self):
        resultado = cmd_trilha.executar("COBOL", self.json_path)
        self.assertIn("não encontrada", resultado)
        self.assertIn("Formação Java Developer", resultado)


# ===========================================================================
# TESTES — /desafio
# ===========================================================================
class TestComandoDesafio(unittest.TestCase):

    def test_gerar_desafio_retorna_dict_com_chaves_obrigatorias(self):
        dados = cmd_desafio.gerar_desafio("Java", "Intermediário")
        for chave in ["tecnologia", "nivel", "categoria", "xp", "tempo", "titulo", "descricao"]:
            self.assertIn(chave, dados)

    def test_gerar_desafio_tecnologia_preservada(self):
        dados = cmd_desafio.gerar_desafio("Java", "Básico")
        self.assertEqual(dados["tecnologia"], "Java")

    def test_gerar_desafio_nivel_basico(self):
        dados = cmd_desafio.gerar_desafio("Python", "Básico")
        self.assertEqual(dados["nivel"], "Básico")

    def test_gerar_desafio_nivel_avancado(self):
        dados = cmd_desafio.gerar_desafio("React", "Avançado")
        self.assertEqual(dados["nivel"], "Avançado")

    def test_gerar_desafio_nivel_intermediario(self):
        dados = cmd_desafio.gerar_desafio("Node.js", "Intermediário")
        self.assertEqual(dados["nivel"], "Intermediário")

    def test_gerar_desafio_nivel_invalido_usa_intermediario(self):
        dados = cmd_desafio.gerar_desafio("Go", "SuperAvançado")
        self.assertEqual(dados["nivel"], "Intermediário")

    def test_gerar_desafio_nivel_omitido_escolhe_aleatorio(self):
        dados = cmd_desafio.gerar_desafio("Python")
        self.assertIn(dados["nivel"], ["Básico", "Intermediário", "Avançado"])

    def test_gerar_desafio_xp_dentro_do_intervalo(self):
        for _ in range(20):
            dados = cmd_desafio.gerar_desafio("Java")
            self.assertGreaterEqual(dados["xp"], 500)
            self.assertLessEqual(dados["xp"], 5000)

    def test_formatar_desafio_contém_tecnologia(self):
        dados = cmd_desafio.gerar_desafio("Java", "Intermediário")
        texto = cmd_desafio.formatar_desafio(dados)
        self.assertIn("Java", texto)

    def test_formatar_desafio_contém_nivel(self):
        dados = cmd_desafio.gerar_desafio("Java", "Intermediário")
        texto = cmd_desafio.formatar_desafio(dados)
        self.assertIn("Intermediário", texto)

    def test_formatar_desafio_contém_secoes_markdown(self):
        dados = cmd_desafio.gerar_desafio("Java", "Básico")
        texto = cmd_desafio.formatar_desafio(dados)
        self.assertIn("## ✅ Requisitos", texto)
        self.assertIn("## 💡 Dicas", texto)
        self.assertIn("## 📥 Exemplo de Entrada", texto)
        self.assertIn("## 📤 Exemplo de Saída Esperada", texto)

    def test_executar_retorna_string_nao_vazia(self):
        resultado = cmd_desafio.executar("Java", "Básico")
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 50)

    def test_executar_tecnologia_vazia_retorna_erro(self):
        resultado = cmd_desafio.executar("")
        self.assertIn("❌", resultado)

    def test_executar_sem_nivel_funciona(self):
        resultado = cmd_desafio.executar("Python")
        self.assertIn("Python", resultado)


# ===========================================================================
# TESTES — /certificado
# ===========================================================================
class TestComandoCertificado(unittest.TestCase):

    def setUp(self):
        self.json_path = criar_json_temp()
        self.tmpdir = Path(tempfile.mkdtemp())

    def tearDown(self):
        os.unlink(self.json_path)
        for f in self.tmpdir.iterdir():
            f.unlink()
        self.tmpdir.rmdir()

    # --- _codigo_verificacao ---
    def test_codigo_formato_correto(self):
        codigo = cmd_certificado._codigo_verificacao()
        partes = codigo.split("-")
        self.assertEqual(partes[0], "DIO")
        self.assertEqual(len(partes), 4)
        for parte in partes[1:]:
            self.assertEqual(len(parte), 4)

    def test_codigo_unico_em_chamadas_consecutivas(self):
        codigos = {cmd_certificado._codigo_verificacao() for _ in range(20)}
        self.assertGreater(len(codigos), 1)

    # --- buscar_trilha_por_nome ---
    def test_buscar_trilha_java_encontrada(self):
        trilha = cmd_certificado.buscar_trilha_por_nome("Java", self.json_path)
        self.assertIsNotNone(trilha)
        self.assertIn("Java", trilha["tecnologia"])

    def test_buscar_trilha_inexistente_retorna_none(self):
        trilha = cmd_certificado.buscar_trilha_por_nome("COBOL", self.json_path)
        self.assertIsNone(trilha)

    def test_buscar_trilha_arquivo_inexistente_retorna_none(self):
        trilha = cmd_certificado.buscar_trilha_por_nome("Java", Path("/nao/existe.json"))
        self.assertIsNone(trilha)

    # --- gerar_certificado ---
    def test_gerar_certificado_campos_obrigatorios(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java Developer", self.json_path)
        for chave in ["nome_aluno", "nome_trilha", "tecnologia", "nivel", "modulos", "xp_total", "data_emissao", "codigo"]:
            self.assertIn(chave, dados)

    def test_gerar_certificado_nome_preservado(self):
        dados = cmd_certificado.gerar_certificado("Maria Souza", "Python", self.json_path)
        self.assertEqual(dados["nome_aluno"], "Maria Souza")

    def test_gerar_certificado_trilha_nao_encontrada_usa_nome_dado(self):
        dados = cmd_certificado.gerar_certificado("Pedro", "TrilhaFicticia", self.json_path)
        self.assertEqual(dados["nome_trilha"], "TrilhaFicticia")
        self.assertEqual(dados["tecnologia"], "N/A")

    def test_gerar_certificado_data_formato_brasileiro(self):
        import re
        dados = cmd_certificado.gerar_certificado("Ana", "Java", self.json_path)
        self.assertRegex(dados["data_emissao"], r"\d{2}/\d{2}/\d{4}")

    # --- formatar_certificado ---
    def test_formatar_certificado_contém_nome_maiusculo(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java", self.json_path)
        texto = cmd_certificado.formatar_certificado(dados)
        self.assertIn("JOÃO SILVA", texto)

    def test_formatar_certificado_contém_nome_trilha(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java", self.json_path)
        texto = cmd_certificado.formatar_certificado(dados)
        self.assertIn("Formação Java Developer", texto)

    def test_formatar_certificado_contém_codigo(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java", self.json_path)
        texto = cmd_certificado.formatar_certificado(dados)
        self.assertIn("DIO-", texto)

    def test_formatar_certificado_contém_data(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java", self.json_path)
        texto = cmd_certificado.formatar_certificado(dados)
        self.assertIn(dados["data_emissao"], texto)

    # --- salvar_certificado ---
    def test_salvar_certificado_cria_arquivo(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java", self.json_path)
        conteudo = cmd_certificado.formatar_certificado(dados)
        caminho = cmd_certificado.salvar_certificado(conteudo, "João Silva", "Java Developer", self.tmpdir)
        self.assertTrue(caminho.exists())

    def test_salvar_certificado_conteudo_correto(self):
        dados = cmd_certificado.gerar_certificado("João Silva", "Java", self.json_path)
        conteudo = cmd_certificado.formatar_certificado(dados)
        caminho = cmd_certificado.salvar_certificado(conteudo, "João Silva", "Java", self.tmpdir)
        lido = caminho.read_text(encoding="utf-8")
        self.assertEqual(lido, conteudo)

    # --- executar ---
    def test_executar_retorna_conteudo_e_caminho(self):
        conteudo, caminho = cmd_certificado.executar(
            "João Silva", "Java Developer",
            caminho_dados=self.json_path,
            destino=self.tmpdir
        )
        self.assertIsInstance(conteudo, str)
        self.assertIsNotNone(caminho)
        self.assertTrue(Path(caminho).exists())

    def test_executar_nome_vazio_retorna_erro(self):
        resultado, caminho = cmd_certificado.executar("", "Java", self.json_path, self.tmpdir)
        self.assertIn("❌", resultado)
        self.assertIsNone(caminho)

    def test_executar_trilha_vazia_retorna_erro(self):
        resultado, caminho = cmd_certificado.executar("João", "", self.json_path, self.tmpdir)
        self.assertIn("❌", resultado)
        self.assertIsNone(caminho)


# ===========================================================================
# RUNNER — executa os testes e grava resultados em TXT
# ===========================================================================
if __name__ == "__main__":
    import io

    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    total = suite.countTestCases()

    buffer = io.StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    resultado = runner.run(suite)

    saida = buffer.getvalue()
    aprovados = total - len(resultado.failures) - len(resultado.errors)
    cobertura = round((aprovados / total) * 100, 1) if total > 0 else 0

    relatorio = f"""
{'='*70}
RELATÓRIO DE TESTES — Deal Explorer Slash Commands
{'='*70}
Data/Hora : {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
Arquivo   : tests/test_commands.py
{'='*70}

{saida}

{'='*70}
RESUMO
{'='*70}
Total de testes  : {total}
Aprovados        : {aprovados}
Falhas           : {len(resultado.failures)}
Erros            : {len(resultado.errors)}
Taxa de aprovação: {cobertura}%
Meta mínima      : 70%
Status           : {'✅ META ATINGIDA' if cobertura >= 70 else '❌ ABAIXO DA META'}
{'='*70}
""".strip()

    print(relatorio)

    # Salva o relatório
    out_path = Path(__file__).parent / "resultado_testes.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print(f"\n📄 Relatório salvo em: {out_path}")
    sys.exit(0 if cobertura >= 70 else 1)
