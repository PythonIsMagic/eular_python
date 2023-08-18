from ..src import eular_003

def test_maxprimefactor_0_returnNone():
    assert eular_003.max_prime_factor(0) is None


def test_maxprimefactor_1_returnNone():
    assert eular_003.max_prime_factor(1) is None


def test_maxprimefactor_2_return2():
    assert eular_003.max_prime_factor(2) == 2


def test_maxprimefactor_3_return3():
    assert eular_003.max_prime_factor(3) == 3


def test_maxprimefactor_4_return2():
    assert eular_003.max_prime_factor(4) == 2


def test_maxprimefactor_10_return5():
    assert eular_003.max_prime_factor(10) == 5


def test_maxprimefactor_100_return5():
    assert eular_003.max_prime_factor(100) == 5


def test_maxprimefactor_1000_return5():
    assert eular_003.max_prime_factor(1000) == 5