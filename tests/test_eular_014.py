import pytest

from ..src import eular_014


def test_collatzseq_1_returns1():
    expected = [1]
    assert eular_014.collatz_seq(1) == expected


def test_collatzseq_2_returns2_1():
    expected = [2, 1]
    assert eular_014.collatz_seq(2) == expected


def test_collatzseq_3_returns3_10_5_16_8_4_2_1():
    expected = [3, 10, 5, 16, 8, 4, 2, 1]
    assert eular_014.collatz_seq(3) == expected


def test_collatzseq_4_returns4_2_1():
    expected = [4, 2, 1]
    assert eular_014.collatz_seq(4) == expected


def test_collatzseq_5_returns5_16_8_4_2_1():
    expected = [5, 16, 8, 4, 2, 1]
    assert eular_014.collatz_seq(5) == expected


def test_nextcollatz_neg1_raiseException():
    with pytest.raises(ValueError):
        eular_014.next_collatz(-1)


def test_nextcollatz_0_raiseException():
    with pytest.raises(ValueError):
        eular_014.next_collatz(0)


def test_nextcollatz_1_raiseException():
    with pytest.raises(ValueError):
        eular_014.next_collatz(1)


def test_nextcollatz_2_returns1():
    expected = 1
    assert eular_014.next_collatz(2) == expected


def test_nextcollatz_3_returns10():
    expected = 10
    assert eular_014.next_collatz(3) == expected


def test_nextcollatz_4_returns2():
    expected = 2
    assert eular_014.next_collatz(4) == expected


def test_nextcollatz_5_returns16():
    expected = 16
    assert eular_014.next_collatz(5) == expected
