def print_list(alist):
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
