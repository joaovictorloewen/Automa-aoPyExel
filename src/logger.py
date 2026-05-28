import logging

from config import PASTA_LOGS

logging.basicConfig(
    filename=PASTA_LOGS / "automacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()