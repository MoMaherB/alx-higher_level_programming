#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    list_of_args = sys.argv
    sum = 0
    for i in range(1, len(list_of_args)):
        sum += int(list_of_args[i])
    print(sum)
