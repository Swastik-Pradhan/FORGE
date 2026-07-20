import logging

from forge.utils.config import LOG_LEVEL, LOG_FILE

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename=LOG_FILE,
    filemode="a",
)

logger = logging.getLogger("forge")