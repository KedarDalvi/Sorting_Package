# REPORT - Sorting_Package
## Contents
- Implementations: BubbleSort, SelectionSort, MergeSort, QuickSort
- Interface: SortBase (abstract base class)
- How to run:
  - Examples:
    - python3 main.py --input input.txt --algorithm bubble --order asc > output.txt
- Tests:
  - pytest (see junit.xml and coverage.xml in reports/)
- Complexity notes:
  - Bubble: O(n^2) time, O(1) extra space
  - Selection: O(n^2) time, O(1) extra space
  - Merge: O(n log n) time, O(n) extra space
  - Quick: average O(n log n), worst O(n^2), O(log n) stack (expected)
