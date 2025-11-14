"""Iterative QuickSort implementation with randomized pivot."""

import random
from typing import List
from .base import Sorter


class QuickSort(Sorter):
    """Iterative quicksort using randomized pivot selection."""

    def sort(self, data: List[int]) -> List[int]:
        """Return a new sorted list (ascending or descending)."""
        self.validate(data)
        arr = data[:]
        n = len(arr)
        if n <= 1:
            return arr

        stack = [(0, n - 1)]
        comparator = (lambda a, b: a < b) if self.ascending else (lambda a, b: a > b)

        while stack:
            low, high = stack.pop()
            if low >= high:
                continue

            pivot_idx = random.randint(low, high)
            pivot_value = arr[pivot_idx]
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
            store = low
            for index in range(low, high):
                if comparator(arr[index], pivot_value) or (
                    arr[index] == pivot_value and self.ascending
                ):
                    arr[store], arr[index] = arr[index], arr[store]
                    store += 1
            arr[store], arr[high] = arr[high], arr[store]

            left_size = store - 1 - low
            right_size = high - (store + 1)
            if left_size > right_size:
                if low < store - 1:
                    stack.append((low, store - 1))
                if store + 1 < high:
                    stack.append((store + 1, high))
            else:
                if store + 1 < high:
                    stack.append((store + 1, high))
                if low < store - 1:
                    stack.append((low, store - 1))
        return arr
