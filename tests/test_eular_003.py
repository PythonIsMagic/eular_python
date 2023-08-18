
from ..src import eular_003


def test_max_prime_factor_negative_number():
    result = eular_003.max_prime_factor(-12)
    assert result is None


def test_maxprimefactor_0_returnNone():
    result = eular_003.max_prime_factor(0)
    assert result is None


def test_max_prime_factor_one():
    result = eular_003.max_prime_factor(1)
    assert result is None


def test_max_prime_factor_prime_number():
    result = eular_003.max_prime_factor(17)
    assert result == 17


def test_max_prime_factor_large_prime():
    result = eular_003.max_prime_factor(9973)
    assert result == 9973


def test_max_prime_factor_very_large_prime():
    result = eular_003.max_prime_factor(10000019)
    assert result == 10000019


def test_max_prime_factor_composite_number():
    result = eular_003.max_prime_factor(56)
    assert result == 7


def test_max_prime_factor_large_composite():
    result = eular_003.max_prime_factor(123456)
    assert result == 643


def test_max_prime_factor_very_large_composite():
    result = eular_003.max_prime_factor(999999990)
    assert result == 137
