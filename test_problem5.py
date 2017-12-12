import problem5
import pytest


def test_divbyallupto_1_raiseException():
    with pytest.raises(ValueError):
        problem5.div_by_all_upto(1)


def test_divbyallupto_2_raisesException():
    with pytest.raises(ValueError):
        problem5.div_by_all_upto(1)


def test_divbyallupto_15_raisesException():
    with pytest.raises(ValueError):
        problem5.div_by_all_upto(15)


def test_divbyallupto_10_returns2520():
    assert problem5.div_by_all_upto(10) == 2520
