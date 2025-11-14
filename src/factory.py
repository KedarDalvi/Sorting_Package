"""Factory to get sorter instances by name."""

from typing import Type
from .bubble import BubbleSort
from .selection import SelectionSort
from .merge import MergeSort
from .quick import QuickSort

ALGO_MAP = {
    "bubble": BubbleSort,
    "selection": SelectionSort,
    "merge": MergeSort,
    "quick": QuickSort,
}

class SorterFactory:
    """Factory class to return sorter instances based on algorithm name."""

    @staticmethod
    def get_sorter(name: str, ascending: bool = True):
        """Return a Sorter instance by algorithm name."""
        if not isinstance(name, str):
            raise TypeError("Algorithm name must be a string.")
        key = name.strip().lower()
        if key not in ALGO_MAP:
            valid = ", ".join(sorted(ALGO_MAP.keys()))
            raise ValueError(f"Unknown algorithm '{name}'. Valid: {valid}")
        sorter_cls: Type = ALGO_MAP[key]
        return sorter_cls(ascending=ascending)
