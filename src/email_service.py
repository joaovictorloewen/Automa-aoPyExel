import smtplib

from email.message import EmailMessage

from logger import logger

from config import (
    EMAIL_REMETENTE,
    SENHA_EMAIL,
    EMAIL_DESTINO,
    ARQUIVO_RELATORIO
)

def enviar_email():

    logger.info("Enviando email")

    msg = EmailMessage()

    msg["Subject"] = "Relatório Automático"
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINO

    msg.set_content(
        "Segue o relatório automático em anexo."
    )

    with open(ARQUIVO_RELATORIO, "rb") as f:

        arquivo = f.read()

        msg.add_attachment(
            arquivo,
            maintype="application",
            subtype="octet-stream",
            filename="relatorio_final.xlsx"
        )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            EMAIL_REMETENTE,
            SENHA_EMAIL
        )

        smtp.send_message(msg)

    logger.info("Email enviado")