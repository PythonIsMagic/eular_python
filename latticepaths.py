def next_path(path, grid_len):
    while len(path) > 0:
        x, y = path.pop()  # Pop back one step
        if len(path) == 0:
            return False, []
        _x, _y = path[-1]

        if _x == grid_len or _y == grid_len:  # Wall. Only 1 choice available.
            pass
        elif y == _y + 1:
            pass
        else:
            path.append((_x, _y + 1))
            return True, path
    else:
        return False, []


def get_routes(x, y, grid_size, remembered={}):
    # Finds all the routes from a given point (x, y) in a grid.
    if (x, y) not in remembered:
        remembered[x, y] = 0
    routes, path = 0, []
    iterating = True

    while iterating:
        path.append((x, y))
        if x < grid_size:
            x += 1
        elif y < grid_size:
            y += 1
        else:
            routes += 1
            iterating, path = next_path(path, grid_size)
            if iterating:
                x, y = path.pop()

        if (x, y) in remembered:
            routes += remembered[x, y]
            path.append((x, y))

            iterating, path = next_path(path, grid_size)
            if iterating:
                x, y = path.pop()

    return routes


def find_all_routes(grid_size, remembered):
    # The lattice array is really grid_size + 1

    # Start constructing the counts from the last space
    for i in range(grid_size, -1, -1):
        for j in range(grid_size, -1, -1):
            # Remember the count of paths from the current (i, j) position
            if (i, j) not in remembered:
                remembered[i, j] = get_routes(i, j, grid_size, remembered)

    routes = get_routes(0, 0, grid_size, remembered)

    return routes
