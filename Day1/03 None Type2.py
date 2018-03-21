
def default_val(x = 10):
    print(x)

def list_adder(name, the_list=[]):
    the_list.append(name)
    return the_list

def list_adder2(name, the_list=None):
    if the_list is None:
        the_list = []
    the_list.append(name)
    return the_list

def main():
    my_list = list_adder2("Sue")
    print(my_list)
    my_list = list_adder2("Peter", my_list)
    print(my_list)

    default_val()
    default_val(99)




if __name__ == '__main__':
    main()