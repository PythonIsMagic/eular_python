import string

ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen',
         6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}


def num_to_list(n):
    return [int(x) for x in str(n)]


def get_digit(n, i):
    """
    Returns the i'th digit(from the right of the ones digit) of an integer n
    """
    modulus = pow(10, i + 1)
    power = pow(10, i)
    return (n % modulus) // power


def get_text(n):
    """
    Returns the test representation of an integer from 0-999
    """
    if n < 1 or n > 999:
        raise ValueError('n is out of bounds. Must be between 1 and 999 inclusive.')

    alpha = ''
    # Hundreds digit
    if n < 100:
        pass
    elif n % 100 == 0:
        alpha += ones[get_digit(n, 2)] + ' hundred'
    else:
        alpha += ones[get_digit(n, 2)] + ' hundred and '

    # Teens
    if get_digit(n, 1) == 1:
        alpha += teens[get_digit(n, 0)]
    # Factors of 10
    elif n % 10 == 0:
        alpha += tens[get_digit(n, 1)]
    # Ten+single, ie: "twenty-one"
    elif get_digit(n, 1) >= 2:
        alpha += tens[get_digit(n, 1)] + '-' + ones[get_digit(n, 0)]
    else:
        alpha += ones[get_digit(n, 0)]
    return alpha


def num_to_alpha(n):
    alpha = ''
    if n == 0:
        return 'zero'
    if n >= 1000000:
        millions = (n % 1000000000) // 1000000
        alpha += '{} million '.format(get_text(millions))

    if n >= 1000:
        thousands = (n % 1000000) // 1000
        alpha += '{} thousand '.format(get_text(thousands))

    hundreds = n % 1000
    if hundreds > 0:
        alpha += get_text(hundreds)

    return alpha.strip()


def letter_qty(s):
    _sum = 0
    for c in s:
        if c in string.ascii_letters:
            _sum += 1
    return _sum


def add_digits(n):
    digits = num_to_list(n)
    sum = 0
    for d in digits:
        sum += d
    return sum
