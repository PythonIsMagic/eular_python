#!/usr/bin/env python3
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
    month = 1
    day = 1
    year = 1900
    weekday = 0
    sundays = 0

    while year < 2001:
        print('{}/{}/{} weekday: {}'.format(month, day, year, weekday))
        input()
        # Check for Sunday on the first of the month.
        if weekday == 6 and day == 1:
            sundays += 1
            print('Sunday on the first of the month!')

        # advance day
        day += 1
        weekday = (weekday + 1) % 7

        # Advance month
        if day > get_days(month, year):
            day = 1
            month += 1

        # Advance Year
        if month > 12:
            year += 1
            month = 1
            #  input()

    print('There were {} Sundays counted.'.format(sundays))
