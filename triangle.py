# Generator
def triangle_num():
    x = 1
    tri = 1
    while True:
        yield tri
        x += 1
        tri += x
