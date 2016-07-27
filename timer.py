#!/usr/bin/env python3

from __future__ import print_function

import primes
import sys
import time

# Selects the time func for Unix and time.clock for Windows.
timer = time.clock if sys.platform[:3] == 'win' else time.time


def basic_timer(func, *args):
    """ Basic timer:
    * Many disadvantages:
    * No keyword args  for tested func
    * Hardcoded reps. Only total time. Doesn't verify func worked.
    * Charges the cost of range() to the time
    * Uses time.clock (Best for Windows)
    """
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start  # Total time elapsed in seconds.


def total(reps, func, *pargs, **kargs):
    """
    Returns the total time for the specified repetitions of a test function.
    * The repetitions can vary.
    * Any number of positional and keywords args can be passed.
    * Returns total time for all calls and function's final return value so we can verify
    *   function's operation success.
    Returns (total time, last result)
    """
    # Hoisted the range call out of the timing loop.
    # In 3.x, range is an iterable so it doesn't make a difference.
    repslist = list(range(reps))

    start = timer()
    for i in repslist:
        return_val = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, return_val)


def bestof(reps, func, *pargs, **kargs):
    """
    Measures the quickest time among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32  # Set best time very high - 136 years
    for i in range(reps):
        start = timer()
        return_val = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, return_val)


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
        Returns (best of reps1 runs of (total of reps2 runs of func))
    """

    # Note: This is called the above total() function and passing all the rest to that.
    return bestof(reps1, total, reps2, func, *pargs, **kargs)


def basic_test(func, *pargs, **kargs):
    if len(kargs) > 0:
        print('Basic total time test for: {}({}{})'.format(str(func), str(pargs), str(kargs)))
    else:
        print('Testing: {}{}'.format(str(func), str(pargs)))

    print('Basic Timer - Running 1000 reps each set')
    print('')
    for t, i in enumerate(range(10)):
        total_time = basic_timer(func, *pargs, **kargs)  # Testing 2 to the 1000th power
        print('Set #{}: {} seconds'.format(i, total_time))


def enhanced_tests(func, *pargs, **kargs):
    print('\==================================================')
    reps = 1000
    if len(kargs) > 0:
        print('Enhanced tests for: {}({}{})'.format(str(func), str(pargs), str(kargs)))
    else:
        print('Testing: {}{}'.format(str(func), str(pargs)))

    print('Total Times - Running {} reps each set'.format(reps))
    print('')
    for t, i in enumerate(range(5)):
        total_time = total(1000, func, *pargs, **kargs)[0]
        print('Set #{}: {} seconds'.format(i, total_time))

    print('')
    besttime = bestof(reps, func, *pargs, **kargs)[0]
    print('best run time in {} reps: {} seconds'.format(reps, besttime))
    print('')
    print(bestoftotal(50, reps, func, *pargs, **kargs))
    print('best total time run for 50 runs of {} reps'.format(reps))


def compare_funcs(reps, func1, func2):
    """
    Takes two tuples of function calls and compares the speeds.
    """
    print('####################################')
    print('Comparing 2 functions!')
    total_time1 = total(reps, *func1)[0] / reps
    total_time2 = total(reps, *func2)[0] / reps

    print(func1)
    print('Total time: {} seconds'.format(total_time1))
    print('')
    print(func2)
    print('Total time: {} seconds'.format(total_time2))
    print('')

    if total_time1 < total_time2:
        print('{} had the faster total time: '.format(func1), end='')
    else:
        print('{} had the faster total time: '.format(func2), end='')
    besttime = max(total_time1, total_time2)
    print('{} seconds.'.format(besttime))

    diff = abs(total_time1 - total_time2)
    percent = (diff / besttime) * 100
    print('Faster by {}%'.format(percent))

if __name__ == "__main__":
    #  basic_test(pow, 2, 1000)
    #  enhanced_tests(pow, 2, 1000)
    #  enhanced_tests(str.upper, 'spam')

    #  test1 = (str.upper, 'spam')
    #  test2 = (str.upper, 'spamspaspaspammm')
    #  compare_funcs(test1, test2)

    # Test the isprime functions: One that checks all numbers, and one that skips evens.
    #  test_num = 809789132779
    #  prime1 = (primes.isprime_checkall, test_num)
    #  prime2 = (primes.isprime_2step, test_num)
    #  compare_funcs(10000, prime1, prime2)

    # Test prime number generation: brute checking all ints vs sieve of Eratosthenese
    #  upto = 100
    #  prime1 = (primes.generate_primes, upto)
    #  prime2 = (primes.sieve_rm_method, upto)
    #  compare_funcs(10000, prime1, prime2)

    # Test prime sieves: One using remove method, other marking numbers and removing at end.
    #  upto = 100
    #  prime2 = (primes.sieve_rm_method, upto)
    #  prime1 = (primes.sieve_markers, upto)
    #  compare_funcs(10000, prime1, prime2)

    # Test prime generation: sieve_markers vs generate_primes
    upto = 1000
    prime2 = (primes.generate_primes, upto)
    prime1 = (primes.sieve_markers, upto)
    compare_funcs(10000, prime1, prime2)
