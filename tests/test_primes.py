import pytest

import eular_python.src
from ..src import primes


def test_getprimefactors_neg1_returnsNone():
    assert primes.get_prime_factors(-1) is None


def test_getprimefactors_0_returnsNone():
    assert primes.get_prime_factors(0) is None


def test_getprimefactors_1_returnsNone():
    assert primes.get_prime_factors(1) is None


def test_getprimefactors_2_returns2():
    assert primes.get_prime_factors(2) == {2}


def test_getprimefactors_3_returns3():
    assert primes.get_prime_factors(3) == {3}


def test_getprimefactors_4_returns2():
    assert primes.get_prime_factors(4) == {2}


def test_getprimefactors_5_returns5():
    assert primes.get_prime_factors(5) == {5}


def test_getprimefactors_6_returns2_3():
    assert primes.get_prime_factors(6) == {2, 3}


def test_getprimefactors_7_returns7():
    assert primes.get_prime_factors(7) == {7}


def test_getprimefactors_10_returns2_5():
    assert primes.get_prime_factors(10) == {2, 5}


def test_getprimefactors_12_returns2_3():
    assert primes.get_prime_factors(12) == {2, 3}


def test_getprimefactors_24_returns2_3():
    assert primes.get_prime_factors(24) == {2, 3}


@pytest.fixture(params=[eular_python.src.primes.isprime_ver1,
                        eular_python.src.primes.isprime_ver2])
def isprime(request):
    return request.param


def test_isprime_0_returnFalse(isprime):
    assert isprime(0) is False


def test_isprime_1_returnFalse(isprime):
    assert isprime(1) is False


def test_isprime_2_returnTrue(isprime):
    assert isprime(2)


def test_isprime_3_returnTrue(isprime):
    assert isprime(3)


def test_primes_1next_return2():
    g = eular_python.src.primes.primes()
    assert next(g) == 2


def test_primes_2next_return3():
    g = eular_python.src.primes.primes()
    next(g)
    assert next(g) == 3


def test_primes_3next_return5():
    g = eular_python.src.primes.primes()
    next(g)
    next(g)
    assert next(g) == 5
