import logger

class loggerClass(logger.Logger):

    def __init__(self) -> None:
        super().__init__()
        self.call_count = 0

    def write(self, msg: str, exception: Exception):
        self.call_count += 1
