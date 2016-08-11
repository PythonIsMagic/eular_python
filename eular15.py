#!/usr/bin/env python3
# coding=utf-8

"""
Eular15

*Lattice paths*

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

#  while path[0] == (0, 0):


def next_path(path, grid_len):
    while len(path) > 0:
        lastx, lasty = path.pop()  # Pop back one step
        if len(path) == 0:
            return False, []
        x, y = path[-1]

        if x == grid_len or y == grid_len:  # Wall. Only 1 choice available.
            pass
        elif lasty == y + 1:
            pass
        else:
            path.append((x, y + 1))
            return True, path
    else:
        return False, []


if __name__ == "__main__":
    grid_len = 10
    x, y = 0, 0
    routes, path = [], []
    iterating = True

    while iterating:
        path.append((x, y))
        if x < grid_len:
            x += 1
        elif y < grid_len:
            y += 1
        else:
            routes.append(path[:])  # We have reached the end node
            iterating, path = next_path(path, grid_len)
            if iterating:
                x, y = path.pop()

    print('{} routes found!'.format(len(routes)))

    #  for r in routes:
        #  print(r)
