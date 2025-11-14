from .base import Sorter

class MergeSort(Sorter):
    def sort(self, data):
        self.validate(data)
        arr = data[:]  # copy
        n = len(arr)
        if n <= 1:
            return arr

        # bottom-up iterative merge sort
        width = 1
        while width < n:
            left = 0
            while left < n:
                mid = min(left + width, n)
                right = min(left + 2 * width, n)
                # merge arr[left:mid] and arr[mid:right]
                l, r = left, mid
                merged = []
                while l < mid and r < right:
                    if self.ascending:
                        if arr[l] <= arr[r]:
                            merged.append(arr[l]); l += 1
                        else:
                            merged.append(arr[r]); r += 1
                    else:
                        if arr[l] >= arr[r]:
                            merged.append(arr[l]); l += 1
                        else:
                            merged.append(arr[r]); r += 1
                while l < mid:
                    merged.append(arr[l]); l += 1
                while r < right:
                    merged.append(arr[r]); r += 1
                # place merged back
                arr[left:left+len(merged)] = merged
                left += 2 * width
            width *= 2
        return arr
