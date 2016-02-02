#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""


class CustomerDivideException(Exception):
    """Raise Exception"""


def listDivide(numbers, divide=2):
    """return amount of numbers in numbers list divisible by divide.
    """
    counter = 0
    for number in numbers:
        if number % divide == 0:
            counter += 1
    return counter

def testListDivide():
    """Docstring"""
    test1 = listDivide([1, 2, 3, 4, 5])
    test2 = listDivide([2, 4, 6, 8, 10])
    test3 = listDivide([30, 54, 63, 98, 100], divide=10)
    test4 = listDivide([])
    test5 = listDivide([1, 2, 3, 4, 5], 1)

    tests = (test1, test2, test3, test4, test5)
    while test1 == int(2):
        while test2 == int(5):
            while test3 == int(2):
                while test4 == int(0):
                    while test5 == int(5):
                        return tests
    else:
        raise CustomerDivideException('Exception: a number is incorrect')

print testListDivide()
