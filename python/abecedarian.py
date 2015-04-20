#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import unittest

# Write a function called is_abecedarian that returns True if the letters in
# a word appear in alphabetical order (double letters are ok)
# How many abecedarian words are there?


def is_abecedarian(word):
    len_word = len(word)
    i = 0
    while i+1 < len_word:
        if ord(word[i]) > ord(word[i+1]):
            return False
            break
        i += 1
    else:
        return True


class TestAbecedarian(unittest.TestCase):
    def test_is_abecerdarian(self):
        self.assertTrue(is_abecedarian('abcde'))

    def test_is_not_abecerdarian(self):
        self.assertFalse(is_abecedarian('abxde'))

if __name__ == '__main__':
    unittest.main()
