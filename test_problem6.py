import problem6


def test_sumofsquares_upto0_returns0():
    assert problem6.sum_of_squares(0) == 0


def test_sumofsquares_upto1_returns1():
    assert problem6.sum_of_squares(1) == 1


def test_sumofsquares_upto2_returns5():
    assert problem6.sum_of_squares(2) == 5


def test_squareofsum_upto1_returns0():
    assert problem6.square_of_sum(0) == 0


def test_squareofsum_upto1_returns1():
    assert problem6.square_of_sum(1) == 1


def test_squareofsum_upto2_returns9():
    assert problem6.square_of_sum(2) == 9
