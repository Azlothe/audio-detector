import logging
from enum import Enum

LEVEL = logging.DEBUG

class Color(Enum):
    WHITE = "\033[97m"
    YELLOW = "\033[93m"
    ORANGE = "\033[38;5;214m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    def __str__(self):
        return self.value
