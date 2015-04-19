#!/usr/bin/python2.7
# -*- coding: utf8 -*-

# Write a function called bisect that takes a sorted list and a target
# value and returns the index of the value in the list, if it’s there,
# or None if it’s not

import unittest


def bisect(lst, target_value, index=0):
    list_len = len(lst)
    len_mid = list_len/2
    index = index + len_mid
    if list_len == 1:
        if lst[len_mid] != target_value:
            return 0
    if lst[len_mid] == target_value:
        return 1, index
    else:
        if target_value < lst[len_mid]:
            lst = lst[:len_mid]
            return bisect(lst, target_value, 0)
        elif target_value > lst[len_mid]:
            lst = lst[len_mid:]
            return bisect(lst, target_value, index)


class TestBisect(unittest.TestCase):
    def test_num_is_present(self):
        random_list = [77, 68, 72, 82, 19, 78, 28, 95, 18, 97]
        random_list.sort()
        val, index = bisect(random_list, 95)
        self.assertEquals(val, 1)

    def test_num_is_not_present(self):
        random_list = [77, 68, 72, 82, 19, 78, 28, 95, 18, 97]
        random_list.sort()
        self.assertEqual(bisect(random_list, 30), 0)

    def test_num_present_returns_index(self):
        random_list = [77, 68, 72, 82, 19, 78, 28, 95, 18, 97]
        random_list.sort()
        val, index = bisect(random_list, 18)
        self.assertEqual(index, 0)

if __name__ == '__main__':
    unittest.main()
