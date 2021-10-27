from dataclasses import dataclass
import re
from typing import List


@dataclass
class StringCalculator:
    def add(self, numbers: str):
        numbers_to_sum: List[int] = []
        if numbers == "":
            return 0
        elif "//" == numbers[:2]:
            char_index = numbers.index("\n")
            delimiters = [delimiter[:-1] for delimiter in numbers[3: char_index].split("[")]
            numbers_to_sum = [int(n) for n in  re.split(r"|".join(delimiters), numbers[char_index+1:])]
        elif ',' in numbers:
            numbers_to_sum = [int(n) for n in re.split(r",|\n", numbers)]
        else:
            numbers_to_sum.append(int(numbers))
        self.verify_negatives_existence(numbers_to_sum)
        return sum([n for n in numbers_to_sum if n <= 1000])

    def verify_negatives_existence(self, numbers_to_sum: List[int]):
        negatives: List[int] = [ x for x in numbers_to_sum if x < 0]
        if len(negatives) != 0:
            raise Exception("negatives not allowed: " + ', '.join(negatives))