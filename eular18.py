#!/usr/bin/env python3
from __future__ import print_function
import eular11


def find_max_path(tree):
    # Start all paths at 0(or IOW, the absolute left side of the tree.)
    path = [0 for x in range(len(tree))]
    total_paths = 0
    maxsum = 0
    iterating = True

    while iterating:
        # Checking for the best sum
        pathsum = get_sum(path, tree)
        if pathsum > maxsum:
            maxsum = pathsum

        # Move path ahead
        iterating = move_path(path, len(tree) - 1)
        total_paths += 1
    print('max = {}'.format(maxsum))
    print('total of {} paths found!'.format(total_paths))


def get_sum(path, tree):
    pathsum = 0
    for i, row in enumerate(tree):
        pathsum += row[path[i]]
        print('{} '.format(row[path[i]]), end='')
    print('\n')
    return pathsum


def move_path(path, row):
    # Base case: If the row is 0, we can't move that one since its the top.
    # Should mean iteration is over.
    if row == 0:
        return False
    elif path[row] == path[row - 1]:
        path[row] += 1

        # Make sure all sub rows match! To avoid skips
        for x in range(row + 1, len(path)):
            path[x] = path[row]

        return True
    else:

        return move_path(path, row - 1)
    pass


if __name__ == "__main__":
    tree = eular11.read_matrix('number_tree.txt')
    #  tree = eular11.read_matrix('small_tree.txt')
    print(eular11.print_matrix(tree))
    print()
    find_max_path(tree)
