#!/usr/bin/python2.7
# -*- coding: utf8 -*-

# Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once. It should not modify
# the original list.

import unittest
import random

def has_duplicate(input_list):
    len_input_list = len(input_list)
    set_input_list = set(input_list)
    len_set = len(set_input_list)
    if len_set < len_input_list:
        return True
    else:
        return False


class TestDuplicate(unittest.TestCase):
    def test_duplicate_present(self):
        my_list = [2, 3, 1, 1, 4, 5]
        self.assertTrue(has_duplicate(my_list))

    def test_no_duplicate(self):
        my_list = [2, 3, 4, 6, 8, 9]
        self.assertFalse(has_duplicate(my_list))

    def test_birthday_paradox(self):
        i = 1
        counter = 0
        trials = 1000
        while i<=trials:
            birth_days = [random.randint(1,31) for num in range(1,40)]
            birth_months = [random.randint(1,12) for num in range(1,40)]
            birth_date = zip(birth_days, birth_months)
            if has_duplicate(birth_date)==True:
                counter +=1
            i +=1

        probability = (float(counter)/float(trials))
        print "The probability of two people sharing their birthdays: %f" % probability
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
