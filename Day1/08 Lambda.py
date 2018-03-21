def my_func(x, y):
    return x + y

def main():
    f = lambda x, y:  x + y

    print(f(2,3))

    result =  (lambda x, y:  x + y)(3,4)
    print(result)

    ff = lambda p: lambda b: b**p
    square = ff(2)
    cube = ff(3)
    print(square(5))
    print(cube(5))

if __name__ == '__main__':
    main()