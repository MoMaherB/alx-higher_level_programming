#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError:
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        sys.stderr.write("Exception: list index out of range\n")
