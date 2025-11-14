from abc import ABC, abstractmethod
from typing import List

INT32_MIN = -2**31
INT32_MAX = 2**31 - 1
MAX_SIZE = 200_000

class Sorter(ABC):
    def __init__(self, ascending: bool = True):
        self.ascending = ascending

    def validate(self, data: List[int]):
        if not isinstance(data, list):
            raise TypeError("Input must be a list of integers.")
        n = len(data)
        if n > MAX_SIZE:
            raise ValueError(f"List size {n} exceeds maximum allowed {MAX_SIZE}.")
        for i, v in enumerate(data):
            if not isinstance(v, int):
                raise TypeError(f"All elements must be integers. Found {type(v)} at index {i}.")
            if v < INT32_MIN or v > INT32_MAX:
                raise ValueError(f"Element at index {i} = {v} out of INT32 range.")
        return True

    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """Return a new list sorted according to ascending flag."""
        pass
