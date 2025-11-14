import pytest
from src.factory import SorterFactory
from src.base import INT32_MIN, INT32_MAX

algorithms = ["bubble", "selection", "merge", "quick"]

@pytest.mark.parametrize("algo", algorithms)
def test_basic_sorted_asc(algo):
    sorter = SorterFactory.get_sorter(algo, ascending=True)
    data = [5, 1, 3, 2, 9, 0, -1]
    out = sorter.sort(data)
    assert out == sorted(data)

@pytest.mark.parametrize("algo", algorithms)
def test_basic_sorted_desc(algo):
    sorter = SorterFactory.get_sorter(algo, ascending=False)
    data = [5, 1, 3, 2, 9, 0, -1]
    out = sorter.sort(data)
    assert out == sorted(data, reverse=True)

@pytest.mark.parametrize("algo", algorithms)
def test_empty_and_single(algo):
    sorter = SorterFactory.get_sorter(algo, ascending=True)
    assert sorter.sort([]) == []
    assert sorter.sort([1]) == [1]

@pytest.mark.parametrize("algo", algorithms)
def test_duplicates(algo):
    sorter = SorterFactory.get_sorter(algo, ascending=True)
    data = [2,2,2,1,1,3,3,2]
    out = sorter.sort(data)
    assert out == sorted(data)

@pytest.mark.parametrize("algo", algorithms)
def test_invalid_type_in_list(algo):
    sorter = SorterFactory.get_sorter(algo, ascending=True)
    with pytest.raises(TypeError):
        sorter.sort([1, 2, "x"])  # string present

@pytest.mark.parametrize("algo", algorithms)
def test_out_of_range_int(algo):
    sorter = SorterFactory.get_sorter(algo, ascending=True)
    v = INT32_MAX + 1
    with pytest.raises(ValueError):
        sorter.sort([1, v, 3])
