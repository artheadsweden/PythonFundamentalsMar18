import math
import math as m
from math import sqrt
from math import sqrt as squareroot
# from math import * - Don't use this form

def sqrt(x):
    return "hi"

def main():
    print(math.sqrt(9)) # Uses import math
    print(sqrt(25))     # Uses from math import sqrt
    print(squareroot(25)) # Uses from math import sqrt as squareroot


if __name__ == '__main__':
    main()