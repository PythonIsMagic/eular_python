from ..src import eular_023


def test_abundantsupto_12_returns12():
    assert eular_023.abundants_upto(12) == [12]
