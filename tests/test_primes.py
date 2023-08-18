import pytest

import eular_python.src
from ..src import primes


def test_getprimefactors_neg1_returnsNone():
    result = primes.get_prime_factors(-1)
    assert result is None


def test_getprimefactors_0_returnsNone():
    result = primes.get_prime_factors(0)
    assert result is None


def test_getprimefactors_1_returnsNone():
    result = primes.get_prime_factors(1)
    assert result is None


def test_getprimefactors_2_returns2():
    result = primes.get_prime_factors(2)
    assert result == {2}


def test_getprimefactors_3_returns3():
    result = primes.get_prime_factors(3)
    assert result == {3}


def test_getprimefactors_4_returns2():
    result = primes.get_prime_factors(4)
    assert result == {2}


def test_getprimefactors_5_returns5():
    result = primes.get_prime_factors(5)
    assert result == {5}


def test_getprimefactors_6_returns2_3():
    result = primes.get_prime_factors(6)
    assert result == {2, 3}


def test_getprimefactors_7_returns7():
    result = primes.get_prime_factors(7)
    assert result == {7}


def test_getprimefactors_10_returns2_5():
    result = primes.get_prime_factors(10)
    assert result == {2, 5}


def test_getprimefactors_12_returns2_3():
    result = primes.get_prime_factors(12)
    assert result == {2, 3}


def test_getprimefactors_24_returns2_3():
    result = primes.get_prime_factors(24)
    assert result == {2, 3}


@pytest.fixture(params=[eular_python.src.primes.isprime_ver1,
                        eular_python.src.primes.isprime_ver2])
def isprime(request):
    return request.param


def test_isprime_0_returnFalse(isprime):
    result = isprime(0)
    assert result is False


def test_isprime_1_returnFalse(isprime):
    result = isprime(1)
    assert result is False


def test_isprime_2_returnTrue(isprime):
    result = isprime(2)
    assert result


def test_isprime_3_returnTrue(isprime):
    result = isprime(3)
    assert result


def test_primes_1next_return2():
    g = eular_python.src.primes.primes()
    result = next(g)
    assert result == 2


def test_primes_2next_return3():
    g = eular_python.src.primes.primes()
    next(g)
    result = next(g)
    assert result == 3


def test_primes_3next_return5():
    g = eular_python.src.primes.primes()
    next(g)
    next(g)
    result = next(g)
    assert result == 5
