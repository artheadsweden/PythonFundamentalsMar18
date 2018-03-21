class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"Point with x = {self._x} and y = {self._y}"

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self._x + other._x, self._y + other._y)
        raise TypeError("Second operand needs to be of type Point")

    def printit(self):
        print(self._x, self._y)

def main():
    p1 = Point(10, 45)
    p2 = Point(2, 5)

    p1.printit()
    p2.printit()

    #p3 = p1.add(p2)
    p3 = p1 + p2
    #p4 = p1 + 14

    print(p3)

    print(repr(p1))
    print(str(p1))


if __name__ == '__main__':
    main()