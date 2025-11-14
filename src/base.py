"""Base sorter interface and validation utilities."""

from abc import ABC, abstractmethod
from typing import List

INT32_MIN: int = -2**31
INT32_MAX: int = 2**31 - 1
MAX_SIZE: int = 200_000


class Sorter(ABC):
    """Abstract base class for sorting algorithms."""

    def __init__(self, ascending: bool = True) -> None:
        """Initialize sorter with ascending flag."""
        self.ascending = ascending

    def validate(self, data: List[int]) -> bool:
        """Validate list: type, length and INT32 range for each element."""
        if not isinstance(data, list):
            raise TypeError("Input must be a list of integers.")
        size = len(data)
        if size > MAX_SIZE:
            raise ValueError(f"List size {size} exceeds maximum allowed {MAX_SIZE}.")
        for index, value in enumerate(data):
            if not isinstance(value, int):
                raise TypeError(
                    f"All elements must be integers. Found {type(value)} at index {index}."
                )
            if value < INT32_MIN or value > INT32_MAX:
                raise ValueError(
                    f"Element at index {index} = {value} out of INT32 range."
                )
        return True

    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """Return a new list sorted according to ascending flag."""
        raise NotImplementedError
