# Q3 — Sorting_Package: Design & Test Report

## 1. Project overview
This repository implements a small Python sorting package that exposes four sorting algorithms (Bubble, Selection, Merge, Quick) through a common interface. It includes:
- `src/` — source modules (`base.py`, `bubble.py`, `selection.py`, `merge.py`, `quick.py`, `factory.py`).
- `test/` — pytest-based correctness tests.
- `reports/` — this file and any future logs/benchmarks.
- `main.py` — CLI-style entrypoint that reads an input file and writes the sorted list to stdout (so the output can be redirected via terminal).

Constraints enforced:
- Only integer inputs allowed.
- Each element must be in signed 32-bit range: [-2^31, 2^31 - 1].
- Maximum list length = 200,000.
- Sorting returns a **new** list; original input is not mutated.

## 2. High-level design & rationale
### 2.1 Interface
A simple abstract base class (`Sorter` in `src/base.py`) establishes:
- `ascending` flag on construction.
- `validate(data)` method to perform all input checks (type, size, range).
- `sort(data)` abstract method implemented by concrete classes.

Rationale: keeping validation in the base class avoids duplicate checks and centralizes constraint handling and error semantics.

### 2.2 Implementations
- **BubbleSort (src/bubble.py)**  
  Classic bubble sort with early-exit optimization (breaks when a pass has no swaps). Complexity: O(n²). Kept for correctness and teaching; explicitly unacceptable for large inputs but included per assignment.

- **SelectionSort (src/selection.py)**  
  Straightforward selection sort swapping the selected extreme into place for each index. Complexity: O(n²). Included for completeness.

- **MergeSort (src/merge.py)**  
  Iterative bottom-up merge sort (non-recursive). Complexity: O(n log n) deterministic worst-case. Implemented iteratively to avoid recursion depth problems for large `n` and to be robust up to the allowed 200k elements.

- **QuickSort (src/quick.py)**  
  Iterative quicksort using randomized pivot selection and an explicit stack. Average-case O(n log n), worst-case O(n²) — randomized pivot reduces pathological worst-case risk. Implemented iteratively to avoid recursion limits.

Rationale: `merge` and `quick` are the two appropriate algorithms for the allowed scale. `merge` delivers guaranteed worst-case performance; `quick` often performs faster in practice. `bubble` and `selection` are included only for completeness/education.

### 2.3 Factory
`SorterFactory` (`src/factory.py`) maps algorithm names (`"bubble"`, `"selection"`, `"merge"`, `"quick"`) to classes and constructs them with the `ascending` flag. This isolates the selection logic from consumers and keeps `main.py` tiny.

### 2.4 main.py behavior
`main.py` reads a simple input file format (algorithm, order, size, elements) and prints a space-separated sorted list to stdout. This design makes it easy to redirect output to files (required by the assignment).

## 3. Input validation & error handling
Centralized validation checks:
- `data` must be a `list`.
- Each element must be `int`.
- Each element must be between `-2**31` and `2**31-1`.
- List size ≤ 200000.

Exceptions raised:
- `TypeError` for wrong types (non-list input, non-int elements).
- `ValueError` for out-of-range integers or size > 200k.
- `TypeError` for invalid algorithm name types (handled in factory).

Rationale: explicit, deterministic exceptions make tests reliable and behavior predictable.

## 4. Test design and how test cases were chosen
All tests are in `test/test_sorting.py` and use `pytest`. Tests were chosen to cover:
1. **Correctness on typical inputs**  
   - `test_basic_sorted_asc` and `test_basic_sorted_desc` use a small mixed list to compare implementation result against Python's `sorted()` (trusted oracle).
   - Rationale: basic functional correctness for both sort orders.

2. **Edge cases**  
   - `test_empty_and_single` validates empty list and single element behavior (trivial base cases).

3. **Duplicates handling**  
   - `test_duplicates` uses duplicated values to ensure stable ordering where relevant and to ensure duplicates are preserved correctly.

4. **Invalid inputs**  
   - `test_invalid_type_in_list` ensures `TypeError` is raised for non-integer elements.
   - `test_out_of_range_int` ensures `ValueError` is raised for integers outside INT32 bounds.

5. **Cross-algorithm parameterization**  
   - Every test runs across all four algorithm names via `pytest.mark.parametrize`, ensuring parity of behavior across implementations.

Why these tests are sufficient for the assignment:
- The assignment expects correctness, type/range enforcement, and a uniform interface. These tests verify all these requirements.
- Performance tests (timings) are not required by the assignment; if needed they can be added to `reports/` as a follow-up.

## 5. How to run (reproducible steps)
**From project root (the directory that contains `src/`, `test/`, `main.py`):**

1. Run tests:
```bash
# ensure virtualenv is active and pytest is installed
pip install pytest
pytest -q
```

## 5. How to run using terminal
python3 main.py example_input.txt > output.txt
cat output.txt

