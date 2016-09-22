import factors


# Generator
def triangle_num():
    x = 1
    tri = 1
    while True:
        yield tri
        x += 1
        tri += x


if __name__ == "__main__":
    for t in triangle_num():
        f = factors.divisors(t)

        if len(f) > 500:
            print('{} is the first triangle number to have over 500 divisors.'.format(t))
            break
