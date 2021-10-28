from abc import ABC, abstractmethod


class Logger(ABC):

    @abstractmethod
    def write(self, msg: str, exception: Exception):
        pass