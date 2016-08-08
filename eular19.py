"""
Eular problem 19:
* Jan, 1,  1900 was a Monday.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
  divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31
Dec 2000)?
"""

months = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }


def get_days(month, year=None):
    """
    Returns the number of days in the month. The year defaults to None, but if the month is
    February, the year will be needed to calculate the days.
    """
    if month == 2:
        if year is None:
            raise ValueError('getdays(month, year) requires a year when taking 2 as the month.')
        elif is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return months[month]


def is_leap_year(year):
    """
    Returns True if the passed year is a leap-year, False otherwise.
    """
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    for m, d in months.items():
        print('Month {} -> {} days'.format(m, d))
