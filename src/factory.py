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
    @staticmethod
    def get_sorter(name: str, ascending: bool = True):
        if not isinstance(name, str):
            raise TypeError("Algorithm name must be a string.")
        key = name.strip().lower()
        if key not in ALGO_MAP:
            raise ValueError(f"Unknown algorithm '{name}'. Valid: {', '.join(ALGO_MAP.keys())}")
        return ALGO_MAP[key](ascending=ascending)
