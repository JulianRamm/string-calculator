from dataclasses import dataclass
from exceptions import NegativesNotAllowed
import re
import logger


class StringCalculator:
    
    def __init__(self, logger: logger.Logger) -> None:
        self.logger = logger

    def add(self, numbers: str):
        numbers_to_sum = []
        if numbers == "":
            return 0
        elif "//" in numbers[:2]:
            char_index = numbers.index("\n")
            delimiters = [delimiter[:-1] for delimiter in numbers[3: char_index].split("[")]
            if "" in delimiters:
                delimiters = list(numbers[2:char_index])
            numbers_delimiters = numbers[char_index+1:]  
            for delimiter in delimiters:
                numbers_delimiters = "_".join(numbers_delimiters.split(delimiter))
            lista = numbers_delimiters.split("_")
            while "" in lista:
                lista.remove("")
            numbers_to_sum = [int(n) for n in lista]
        elif ',' in numbers:
            numbers_to_sum = [int(n) for n in re.split(r",|\n", numbers)]
        else:
            numbers_to_sum.append(int(numbers))
        self._check_for_negative_numbers(numbers_to_sum)
        res = sum([x for x in numbers_to_sum if x <=1000])
        self.logger.write(str(res), None)
        return res

    def _check_for_negative_numbers(self, numbers):
        negative_numbers = [x for x in numbers if x < 0]
        if len(negative_numbers) > 0:
            exception = NegativesNotAllowed(f"Negatives numbers not allowed: {','.join(str(a) for a in negative_numbers)}")
            self.logger.write("Sum not allowed", exception)
            raise exception

