import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")

    args = parser.parse_args()
    answer = args.x**args.y

    if args.quiet:
        print(answer)
    elif args.verbose:
        print(f"{args.x} to the power of {args.y} equals {answer}")
    else:
        print(f"{args.x}^{args.y} = {answer}")



if __name__ == '__main__':
    main()