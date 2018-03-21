def func(a):
    return a % 2 == 0


def main():
    numbers = [1, 2, 3, 4]
    result = list(filter(func, numbers))
    print(result)

    result = list(filter(lambda a: a % 2 == 0, numbers))
    print(result)

    result = [n for n in numbers if n % 2 == 0]
    print(result)

if __name__ == '__main__':
    main()