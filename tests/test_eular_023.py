from ..src import eular_023


def test_abundantsupto_12_returns12():
    result = eular_023.abundants_upto(12)
    assert result == [12]
