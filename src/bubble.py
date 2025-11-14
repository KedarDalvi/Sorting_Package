from .base import Sorter

class BubbleSort(Sorter):
    def sort(self, data):
        self.validate(data)
        arr = data[:]  # copy
        n = len(arr)
        if n <= 1:
            return arr
        comp = (lambda a, b: a > b) if self.ascending else (lambda a, b: a < b)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if comp(arr[j], arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
