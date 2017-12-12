import problem2


def test_fibonaccis_call1_return1():
    f = problem2.fibonaccis()
    assert next(f) == 1


def test_fibonaccis_call2_return1():
    f = problem2.fibonaccis()
    next(f)
    assert next(f) == 1


def test_fibonaccis_call3_return2():
    f = problem2.fibonaccis()
    next(f)
    next(f)
    assert next(f) == 2


def test_fibonaccis_call4_return3():
    f = problem2.fibonaccis()
    next(f)
    next(f)
    next(f)
    assert next(f) == 3
