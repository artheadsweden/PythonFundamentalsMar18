class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MyClass2:
    def __init__(self, x, y):
        self._x = x
        self._y = y


class MyClass3:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


def main():
    m = MyClass(10,12)
    print(m.x)
    print(m.y)
    m.x += 10
    print(m.x)
    m.z = 22

    m2 = MyClass2(3, 5)
    print(m2._x)

    m3 = MyClass3(4, 9)
    print(m3._MyClass3__x)


if __name__ == '__main__':
    main()