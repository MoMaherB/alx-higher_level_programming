#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for hidden in dir(hidden_4):
        if hidden[0:2] != '__':
            print(hidden)
