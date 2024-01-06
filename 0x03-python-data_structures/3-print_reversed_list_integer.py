#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        for i in range(len(my_list) - 1, - 1, -1):
            print("{:d}".format(my_list[i]))
