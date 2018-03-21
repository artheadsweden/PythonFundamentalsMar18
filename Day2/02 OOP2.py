class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay

    def __str__(self):
        return f"{self.firstname} {self.lastname} earns {self.pay}"

    def give_rasie(self):
        self.pay *= self.raise_amt


class Developer(Employee):
    raise_amt = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + f" and loves {self.prog_lang}"

class Boss(Employee):
    pass

def main():
    emp1 = Employee("Anna", "Jones", 55000)
    emp2 = Employee("John", "Smith", 47000)

    dev1 = Developer("Sara", "Andersen", 55000, 'Python')
    print(dev1)
    dev1.give_rasie()
    print(dev1)

    boss1 = Boss("Peter", "Moore", 60000)
    print(boss1)
    boss1.give_rasie()
    print(boss1)

    if isinstance(boss1, Boss):
        print("boss1 is a Boss")
    else:
        print("boss1 is not a Boss")

    if isinstance(dev1, Boss):
        print("dev1 is a Boss")
    else:
        print("dev1 is not a Boss")


if __name__ == '__main__':
    main()