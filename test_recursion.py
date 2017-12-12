"""
  " Tests for the recursion module.
  """
import pytest
import recursion


def test_multiply_2factors_returns2():
    n = [1, 2, 3, 4, 5]
    assert recursion.multiply(n, 0, 2) == 2


def test_multiply_3factors_returns6():
    n = [1, 2, 3, 4, 5]
    assert recursion.multiply(n, 0, 3) == 6


def test_multiply_3factors_index1_returns24():
    n = [1, 2, 3, 4, 5]
    assert recursion.multiply(n, 1, 3) == 24


def test_multiply_indexoutofbounds_raiseException():
    n = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        recursion.multiply(n, 10, 3)


def test_multiply_3factors_size3_returns24():
    n = [2, 3, 4]
    assert recursion.multiply(n, 0, 3) == 24


def test_multiply_13factors_size14_index0_returns157689344584365834240():
    n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
    expected = 157689344584365834240
    assert recursion.multiply(n, 0, 13) == expected


def test_multiply_13factors_size14_index1_returns211895056785241589760():
    n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
    expected = 211895056785241589760
    assert recursion.multiply(n, 1, 13) == expected
