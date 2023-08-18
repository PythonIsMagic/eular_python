from ..src import eular_004

def test_ispalindrome_emptyString_returnFalse():
    assert eular_004.is_palindrome('') is False


def test_ispalindrome_1_returnTrue():
    assert eular_004.is_palindrome(1)


def test_ispalindrome_10_returnFalse():
    assert eular_004.is_palindrome(10) is False


def test_ispalindrome_11_returnTrue():
    assert eular_004.is_palindrome(11)


def test_ispalindrome_101_returnTrue():
    assert eular_004.is_palindrome(101)


def test_ispalindrome_110_returnFalse():
    assert eular_004.is_palindrome(110) is False


def test_largestpalindrome_2digit_returns9009():
    assert eular_004.largest_palindrome(10, 100) == 9009
