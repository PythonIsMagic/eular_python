from ..src import eular_002


def test_fibonaccis_call1_return1():
    f = eular_002.fibonaccis()
    assert next(f) == 1


def test_fibonaccis_call2_return1():
    f = eular_002.fibonaccis()
    next(f)
    assert next(f) == 1


def test_fibonaccis_call3_return2():
    f = eular_002.fibonaccis()
    next(f)
    next(f)
    assert next(f) == 2


def test_fibonaccis_call4_return3():
    f = eular_002.fibonaccis()
    next(f)
    next(f)
    next(f)
    assert next(f) == 3
