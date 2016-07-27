def print_list(alist):
    pl(alist, len(alist) - 1)

def pl(alist, index):
    # Base case: At index 0
    if index == 0:
        print(index)
    else:
        print(index)
        pl(alist, index - 1)


def print_list_selection(alist, index, factors):
    # Base case: At index 0
    if factors == 0:
        print(alist[index + factors])
    else:
        print(alist[index + factors])
        print_list(alist, index, factors - 1)
