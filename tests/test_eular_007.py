import pytest

from ..src import eular_007


@pytest.fixture(params=[eular_007.isprime_ver1,
                        eular_007.isprime_ver2])
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
    g = eular_007.primes()
    assert next(g) == 2


def test_primes_2next_return3():
    g = eular_007.primes()
    next(g)
    assert next(g) == 3


def test_primes_3next_return5():
    g = eular_007.primes()
    next(g)
    next(g)
    assert next(g) == 5
