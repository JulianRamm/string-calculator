import dataclasses
from abc import ABC, abstractmethod

from logger import Logger

class BasicLogger(Logger):
    
    def write(self, msg: str, exception: Exception):
        if not exception:
            print(msg)
        else:
            print(f"Message received {msg}, the exception thrown was: {exception}")
