#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""

class CustomerDivideException(Exception):
    """Error"""
    def init(self, message):
        self.message = 'There was an error'

def listDivide(numbers, divide=2):
    """return amount of numbers in numbers list divisible by divide.
    """
    counter = 0
    for number in numbers:
        if number % 2 == 0:
            counter += 1
    return counter


def testListDivide():
    test1 = listDivide([1,2,3,4,5])
    test2 = listDivide([2,4,6,8,10])
    test3 = listDivide([30, 54, 63,98, 100], 10)
    test4 = listDivide([])
    test5 = listDivide([1,2,3,4,5], 1)
    
    return test1, test2, test3, test4, test5
    
print listDivide([30, 54, 63, 98, 100], 10)

print testListDivide()
