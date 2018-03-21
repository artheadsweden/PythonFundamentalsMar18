class ArgumentValueError(ValueError):
    pass


def myfunc(x, y):
    if y == 0:
        raise ArgumentValueError("Parameter y can't be 0")
    z = x / y
    return z

def main():
    try:
        print(myfunc(10, 0))
    except ArgumentValueError as e:
        print("ArgumentValueError", e)
    except ValueError as e:
        print("ValueError", e)
    else:
        print("No error")
    finally:
        print("Will always go here")

    print("Done")


if __name__ == '__main__':
    main()