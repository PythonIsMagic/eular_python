from ..src import eular_004


def test_ispalindrome_emptyString_returnFalse():
    result = eular_004.is_palindrome('')
    assert result is False


def test_ispalindrome_1_returnTrue():
    result = eular_004.is_palindrome(1)
    assert result is True


def test_ispalindrome_10_returnFalse():
    result = eular_004.is_palindrome(10)
    assert result is False


def test_ispalindrome_11_returnTrue():
    result = eular_004.is_palindrome(11)
    assert result is True


def test_ispalindrome_101_returnTrue():
    result = eular_004.is_palindrome(101)
    assert result is True


def test_ispalindrome_110_returnFalse():
    result = eular_004.is_palindrome(110)
    assert result is False


def test_largestpalindrome_2digit_returns9009():
    result = eular_004.largest_palindrome(10, 100)
    assert result == 9009
