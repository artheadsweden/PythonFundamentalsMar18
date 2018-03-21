class A:
    def __init__(self):
        print('A.__init__')
        self.x = 10

class B(A):
    def __init__(self):
        print('B.__init__')
        super().__init__()
        self.x += 2

class C(A):
    def __init__(self):
        print('C.__init__')
        super().__init__()
        self.x += 4

class D(C, B):
    def __init__(self):
        print('D.__init__')
        super().__init__()


def main():
    d = D()
    print(d.x)

    print(D.__mro__)


if __name__ == '__main__':
    main()