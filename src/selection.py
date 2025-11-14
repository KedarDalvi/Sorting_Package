"""Selection sort implementation."""

from typing import List
from .base import Sorter


class SelectionSort(Sorter):
    """Selection sort implementation."""

    def sort(self, data: List[int]) -> List[int]:
        """Return a new sorted list (ascending or descending)."""
        self.validate(data)
        arr = data[:]
        n = len(arr)
        if n <= 1:
            return arr

        for i in range(n):
            target_idx = i
            for j in range(i + 1, n):
                if self.ascending:
                    if arr[j] < arr[target_idx]:
                        target_idx = j
                else:
                    if arr[j] > arr[target_idx]:
                        target_idx = j
            if target_idx != i:
                arr[i], arr[target_idx] = arr[target_idx], arr[i]
        return arr
