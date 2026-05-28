from logger import logger

from excel import (
    carregar_planilha,
    limpar_dados,
    gerar_indicadores,
    exportar_dashboard
)

from relatorio import (
    gerar_relatorio,
    formatar_excel
)

from email_service import enviar_email

def main():

    try:

        logger.info("=== INICIANDO AUTOMAÇÃO ===")

        df = carregar_planilha()

        df = limpar_dados(df)

        (
            faturamento_total,
            ranking_vendedores,
            produtos_mais_vendidos
        ) = gerar_indicadores(df)

        gerar_relatorio(
            df,
            faturamento_total,
            ranking_vendedores,
            produtos_mais_vendidos
        )

        formatar_excel()

        exportar_dashboard(df)

        #enviar_email()

        logger.info("=== AUTOMAÇÃO FINALIZADA ===")

        print("Automação concluída com sucesso!")

    except Exception as e:

        logger.error(f"Erro: {e}")

        print(f"Erro na automação: {e}")

if __name__ == "__main__":
    main()