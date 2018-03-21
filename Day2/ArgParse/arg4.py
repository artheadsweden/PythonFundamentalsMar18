import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("square", type=int, help="The number to be squared")

    args = parser.parse_args()
    print(args.square**2)


if __name__ == '__main__':
    main()