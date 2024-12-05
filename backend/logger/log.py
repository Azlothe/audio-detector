import logging
from .constants import Color, LEVEL


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        match record.levelno:
            case logging.DEBUG:
                record.msg = f"{Color.GREEN}{record.msg}{Color.RESET}"
            case logging.INFO:
                record.msg = f"{Color.WHITE}{record.msg}{Color.RESET}"
            case logging.WARNING:
                record.msg = f"{Color.YELLOW}{record.msg}{Color.RESET}"
            case logging.ERROR:
                record.msg = f"{Color.ORANGE}{record.msg}{Color.RESET}"
            case logging.CRITICAL:
                record.msg = f"{Color.RED}{record.msg}{Color.RESET}"
        return super().format(record)


logging.basicConfig(level=LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.handlers = []
logger.addHandler(handler)
