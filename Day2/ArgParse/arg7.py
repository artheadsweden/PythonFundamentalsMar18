import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("square", type=int, help="The number to be squared")
    parser.add_argument("-v", "--verbose", action="count",default=0, help="Increase output verbosity")

    args = parser.parse_args()
    answer = args.square**2
    if args.verbose >= 2:
        print(f"The square of {args.square} equals {answer}")
    elif args.verbose == 1:
        print(f"{args.square}^2 = {answer}")
    else:
        print(answer)


if __name__ == '__main__':
    main()