from myimport.mymodule import add
from myimport import mymodule
import myimport


def main():
    result = add(3,4)
    result2 = mymodule.add(2,3)
    result3 = myimport.mymodule.add(4,5)
    print(result)


if __name__ == '__main__':
    main()