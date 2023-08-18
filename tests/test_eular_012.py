from ..src import eular_012


def test_fromprime():
    """ Compares divisors and divisors_bruteforce. """
    TRIES = 100
    failures = 0

    for i in range(1, TRIES):
        bf = eular_012.divisors_bruteforce(i)
        fp = eular_012.divisors(i)

        if bf != fp:
            print('Test failed on {}!'.format(i))
            print('bruteforce: {}'.format(sorted(bf)))
            print('fromprime:  {}'.format(sorted(fp)))
            failures += 1
        else:
            print('{} - Check.'.format(i))

    if failures > 0:
        print('{} out of {} tests failed.'.format(failures, TRIES - 1))
    else:
        print('All tests passed! (up to {})'.format(TRIES))


def test_trianglenum_call1_returns1():
    gen = eular_012.triangles()
    result = next(gen)
    assert result == 1


def test_trianglenum_call2_returns3():
    gen = eular_012.triangles()
    next(gen)
    result = next(gen)
    assert result == 3


def test_trianglenum_call3_returns6():
    gen = eular_012.triangles()
    next(gen)
    next(gen)
    result = next(gen)
    assert result == 6
