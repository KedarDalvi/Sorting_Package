"""Bubble sort implementation."""

from typing import List
from .base import Sorter


class BubbleSort(Sorter):
    """Bubble sort implementation with early exit optimization."""

    def sort(self, data: List[int]) -> List[int]:
        """Return a new sorted list (ascending or descending)."""
        self.validate(data)
        arr = data[:]  # copy to avoid mutating input
        n = len(arr)
        if n <= 1:
            return arr

        comparator = (lambda a, b: a > b) if self.ascending else (lambda a, b: a < b)
        for _ in range(n):
            swapped = False
            for j in range(0, n - 1):
                if comparator(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
