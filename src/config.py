from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PASTA_ENTRADA = BASE_DIR / "entrada"
PASTA_SAIDA = BASE_DIR / "saida"
PASTA_LOGS = BASE_DIR / "logs"

ARQUIVO_VENDAS = PASTA_ENTRADA / "vendas.xlsx"
ARQUIVO_RELATORIO = PASTA_SAIDA / "relatorio_final.xlsx"
ARQUIVO_DASHBOARD = PASTA_SAIDA / "dashboard.csv"

EMAIL_REMETENTE = "seuemail@gmail.com"
SENHA_EMAIL = "suasenha"
EMAIL_DESTINO = "destino@gmail.com"

PASTA_ENTRADA.mkdir(exist_ok=True)
PASTA_SAIDA.mkdir(exist_ok=True)
PASTA_LOGS.mkdir(exist_ok=True)