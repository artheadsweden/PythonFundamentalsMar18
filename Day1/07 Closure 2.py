def func_fact(p):
    def inner(b):
        return b**p
    return inner

def main():
    square = func_fact(2)
    print(square(2))
    print(square(3))

    cube = func_fact(3)
    print(cube(2))
    print(cube(3))


if __name__ == '__main__':
    main()