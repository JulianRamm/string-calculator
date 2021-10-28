from dataclasses import dataclass
from exceptions import NegativesNotAllowed
import re


@dataclass
class StringCalculator:

    def add(self, numbers: str):
        numbers_to_sum = []
        if numbers == "":
            return 0
        elif "//" in numbers[:2]:
            char_index = numbers.index("\n")
            delimiters = [delimiter[:-1] for delimiter in numbers[3: char_index].split("[")]
            # print(len(delimiters))
            print(delimiters)
            if "" in delimiters:
                delimiters = list(numbers[2:char_index])
                print(delimiters)
            numbers_delimiters = numbers[char_index+1:]  
            for delimiter in delimiters:
                numbers_delimiters = "_".join(numbers_delimiters.split(delimiter))
            print(numbers_delimiters)
            lista = numbers_delimiters.split("_")
            # en caso de que se pase mas de un mismo char "**" elimine los matchs vacios
            while "" in lista:
                lista.remove("")
            print(lista)
            numbers_to_sum = [int(n) for n in lista]
            # numbers_to_sum = [int(n) for n in numbers[char_index+1:].split(re.search(r"\/\/\[?([^\]]+)\]?\n.*", numbers).group(1))] 
        elif ',' in numbers:
            numbers_to_sum = [int(n) for n in re.split(r",|\n", numbers)]
        else:
            numbers_to_sum.append(int(numbers))
        self._check_for_negative_numbers(numbers_to_sum)
        return sum([x for x in numbers_to_sum if x <=1000])

    def _check_for_negative_numbers(self, numbers):
        negative_numbers = [x for x in numbers if x < 0]
        if len(negative_numbers) > 0:
            raise NegativesNotAllowed(f"Negatives numbers not allowed: {','.join(str(a) for a in negative_numbers)}")

