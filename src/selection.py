from .base import Sorter

class SelectionSort(Sorter):
    def sort(self, data):
        self.validate(data)
        arr = data[:]  # copy
        n = len(arr)
        if n <= 1:
            return arr
        for i in range(n):
            target_idx = i
            for j in range(i+1, n):
                if self.ascending:
                    if arr[j] < arr[target_idx]:
                        target_idx = j
                else:
                    if arr[j] > arr[target_idx]:
                        target_idx = j
            if target_idx != i:
                arr[i], arr[target_idx] = arr[target_idx], arr[i]
        return arr
