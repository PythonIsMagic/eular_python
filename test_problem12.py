import problem12


def test_trianglenum_call1_returns1():
    gen = problem12.triangles()
    assert next(gen) == 1


def test_trianglenum_call2_returns3():
    gen = problem12.triangles()
    next(gen)
    assert next(gen) == 3


def test_trianglenum_call3_returns6():
    gen = problem12.triangles()
    next(gen)
    next(gen)
    assert next(gen) == 6
