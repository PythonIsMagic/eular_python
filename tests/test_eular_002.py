import pytest
from ..src import eular_002


def test_sum_evens_empty_list():
    result = eular_002.sum_evens([])
    assert result == 0


def test_sum_evens_even_numbers():
    numlist = [2, 4, 6, 8, 10]
    result = eular_002.sum_evens(numlist)
    assert result == 30


def test_sum_evens_odd_numbers():
    numlist = [1, 3, 5, 7, 9]
    result = eular_002.sum_evens(numlist)
    assert result == 0


def test_sum_evens_mixed_numbers():
    numlist = [2, 3, 4, 5, 6]
    result = eular_002.sum_evens(numlist)
    assert result == 12


def test_sum_evens_negative_numbers():
    numlist = [-2, -4, -6, -8, -10]
    result = eular_002.sum_evens(numlist)
    assert result == -30


def test_sum_evens_large_list():
    numlist = list(range(0, 100000, 2))
    result = eular_002.sum_evens(numlist)
    assert result == 2499950000  # Sum of even numbers from 0 to 99998


def test_fibonaccis_call1_return1():
    f = eular_002.fibonaccis()
    result = next(f)
    assert result == 1


def test_fibonaccis_call2_return1():
    f = eular_002.fibonaccis()
    next(f)
    result = next(f)
    assert result == 1


def test_fibonaccis_call3_return2():
    f = eular_002.fibonaccis()
    next(f)
    next(f)
    result = next(f)
    assert result == 2


def test_fibonaccis_call4_return3():
    f = eular_002.fibonaccis()
    next(f)
    next(f)
    next(f)
    result = next(f)
    assert result == 3


def test_fibonacci_basic():
    gen = eular_002.fibonaccis()
    expected = [1, 1, 2, 3, 5, 8, 13, 21]  # First 8 Fibonacci numbers
    result = [next(gen) for _ in range(len(expected))]
    assert result == expected


def test_fibonacci_with_limit():
    gen = eular_002.fibonaccis(limit=10)  # Limit the sequence to numbers less than 10
    expected_sequence = [1, 1, 2, 3, 5, 8]  # Fibonacci numbers less than 10
    result = [next(gen) for _ in range(len(expected_sequence))]
    assert result == expected_sequence


@pytest.mark.skip()
def test_fibonacci_limit_reached():
    gen = eular_002.fibonaccis(limit=5)  # Limit the sequence to numbers less than 5
    for _ in range(5):  # Try to generate more numbers than the limit
        next(gen)
    with pytest.raises(StopIteration) as e_info:
        next(gen)
