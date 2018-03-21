from functools import reduce

def func(a, b):
    return a if a > b else b

def func2(a, b):
    return a + b

def main():
    numbers = [1, 2, 3, 4]
    result = reduce(func2, numbers)
    print(result)

    result = reduce(lambda a, b: a if a > b else b, numbers)
    print(result)
if __name__ == '__main__':
    main()