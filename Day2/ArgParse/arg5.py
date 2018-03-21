import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("square", type=int, help="The number to be squared")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print(f"The square of {args.square} equals {answer}")
    else:
        print(answer)


if __name__ == '__main__':
    main()