"""
  " Functions related to or using recursion.
  """


def print_list(alist):
    """ Prints a list recursively. """
    pl(alist, 0)


def pl(alist, index):
    if index < len(alist) - 1:
        print(alist[index])
        pl(alist, index + 1)
    else:
        # Base case: index is at the end
        print(alist[index])


def print_selection(alist, index, factors):
    # Base case: At index 0
    if factors == 0:
        print(alist[index])
    else:
        print(alist[index])
        print_selection(alist, index + 1, factors - 1)


def multiply(alist, index, factors, product=1):
    # Base case: At index 0
    if index < 0 or index >= len(alist):
        # Out of bounds, just return 0?
        raise ValueError('index is out of bounds!')
        #  return 0
    elif factors == 1:
        return alist[index]
    else:
        return alist[index] * multiply(alist, index + 1, factors - 1, product)


# This wasn't successful.
def recursive_try():
    pass
    #  print('Eular 9: Recursive solution')
    #  result = recursive_solution()
    #  if result is None:
        #  print('No solution was found')
        #  exit()
    #  else:
        #  a2, b2, c2 = result

    #  a = math.sqrt(a2)
    #  b = math.sqrt(b2)
    #  c = math.sqrt(c2)
