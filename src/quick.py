import random
from .base import Sorter

class QuickSort(Sorter):
    def sort(self, data):
        self.validate(data)
        arr = data[:]  # copy
        n = len(arr)
        if n <= 1:
            return arr

        # iterative quicksort with randomized pivot
        stack = [(0, n - 1)]
        comp = (lambda a, b: a < b) if self.ascending else (lambda a, b: a > b)

        while stack:
            low, high = stack.pop()
            if low >= high:
                continue

            pivot_idx = random.randint(low, high)
            pivot = arr[pivot_idx]
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
            store = low
            for i in range(low, high):
                if comp(arr[i], pivot) or (arr[i] == pivot and self.ascending):
                    arr[store], arr[i] = arr[i], arr[store]
                    store += 1
            arr[store], arr[high] = arr[high], arr[store]

            # push smaller range first to limit stack size
            if (store - 1 - low) > (high - (store + 1)):
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
