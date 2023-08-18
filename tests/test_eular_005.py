import pytest

from ..src import eular_005


def test_divbyallupto_1_raiseException():
    with pytest.raises(ValueError):
        eular_005.div_by_all_upto(1)


def test_divbyallupto_2_raisesException():
    with pytest.raises(ValueError):
        eular_005.div_by_all_upto(1)


def test_divbyallupto_15_raisesException():
    with pytest.raises(ValueError):
        eular_005.div_by_all_upto(15)


def test_divbyallupto_10_returns2520():
    assert eular_005.div_by_all_upto(10) == 2520
