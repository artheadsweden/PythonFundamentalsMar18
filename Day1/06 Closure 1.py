def outer(name):
    def inner(age):
        return f"Hi {name}. I see you are {age} years old"
    return inner

def main():
    f = outer("Anna")
    result = f(15)
    print(result)
    result = f(16)
    print(result)

    f2 = outer("Peter")
    result = f2(34)
    print(result)
    result = f2(35)
    print(result)

    result = f(17)
    print(result)


if __name__ == '__main__':
    main()