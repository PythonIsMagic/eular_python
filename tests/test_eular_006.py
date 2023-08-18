from ..src import eular_006


def test_sumofsquares_upto0_returns0():
    result = eular_006.sum_of_squares(0)
    assert result == 0


def test_sumofsquares_upto1_returns1():
    result = eular_006.sum_of_squares(1)

    assert result == 1


def test_sumofsquares_upto2_returns5():
    result = eular_006.sum_of_squares(2)
    assert result == 5


def test_squareofsum_upto1_returns0():
    result = eular_006.square_of_sum(0)
    assert result == 0


def test_squareofsum_upto1_returns1():
    result = eular_006.square_of_sum(1)
    assert result == 1


def test_squareofsum_upto2_returns9():
    result = eular_006.square_of_sum(2)
    assert result == 9
