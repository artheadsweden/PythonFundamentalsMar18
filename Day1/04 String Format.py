def title(name):
    return name.title()


def main():
    name = "sara"
    age = 45

    print("Hi there", name, "! You are", age, "years old.", sep="")

    print("Hi there {0}! You are {1} years old.".format(name, age))

    # From Python 3.6
    print(f"Hi there {title(name)}! You are {age} years old.")


if __name__ == '__main__':
    main()
