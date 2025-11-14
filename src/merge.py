"""Iterative bottom-up MergeSort implementation."""

from typing import List
from .base import Sorter


class MergeSort(Sorter):
    """Iterative merge sort to avoid recursion depth issues."""

    def sort(self, data: List[int]) -> List[int]:
        """Return a new sorted list (ascending or descending)."""
        self.validate(data)
        arr = data[:]
        n = len(arr)
        if n <= 1:
            return arr

        width = 1
        while width < n:
            left = 0
            while left < n:
                mid = min(left + width, n)
                right = min(left + 2 * width, n)
                left_idx, right_idx = left, mid
                merged: List[int] = []
                while left_idx < mid and right_idx < right:
                    if self.ascending:
                        if arr[left_idx] <= arr[right_idx]:
                            merged.append(arr[left_idx])
                            left_idx += 1
                        else:
                            merged.append(arr[right_idx])
                            right_idx += 1
                    else:
                        if arr[left_idx] >= arr[right_idx]:
                            merged.append(arr[left_idx])
                            left_idx += 1
                        else:
                            merged.append(arr[right_idx])
                            right_idx += 1
                while left_idx < mid:
                    merged.append(arr[left_idx])
                    left_idx += 1
                while right_idx < right:
                    merged.append(arr[right_idx])
                    right_idx += 1
                arr[left:left + len(merged)] = merged
                left += 2 * width
            width *= 2
        return arr
