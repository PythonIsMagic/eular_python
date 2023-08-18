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


def test_getprimefactors_neg1_returnsNone():
    assert eular_003.get_prime_factors(-1) is None


def test_getprimefactors_0_returnsNone():
    assert eular_003.get_prime_factors(0) is None


def test_getprimefactors_1_returnsNone():
    assert eular_003.get_prime_factors(1) is None


def test_getprimefactors_2_returns2():
    assert eular_003.get_prime_factors(2) == {2}


def test_getprimefactors_3_returns3():
    assert eular_003.get_prime_factors(3) == {3}


def test_getprimefactors_4_returns2():
    assert eular_003.get_prime_factors(4) == {2}


def test_getprimefactors_5_returns5():
    assert eular_003.get_prime_factors(5) == {5}


def test_getprimefactors_6_returns2_3():
    assert eular_003.get_prime_factors(6) == {2, 3}


def test_getprimefactors_7_returns7():
    assert eular_003.get_prime_factors(7) == {7}


def test_getprimefactors_10_returns2_5():
    assert eular_003.get_prime_factors(10) == {2, 5}


def test_getprimefactors_12_returns2_3():
    assert eular_003.get_prime_factors(12) == {2, 3}


def test_getprimefactors_24_returns2_3():
    assert eular_003.get_prime_factors(24) == {2, 3}
