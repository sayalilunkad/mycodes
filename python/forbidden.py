#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import unittest

# Write a function named avoids that takes a word and a string of forbidden
# letters,and that returns True if the word doesn’t use any of the forbidden
# letters.
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don’t contain any of them.
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?

def forbidden(word, *forbidden):
    for letter in word:
        for arg in forbidden:
            if letter == arg:
                return False
                break
    else:
        print word
        return True

class TestForbidden(unittest.TestCase):
    def test_forbidden_true(self):
        self.assertTrue(forbidden('string', 'u', 'v', 'w', 'x'))

    def test_forbidden_not_true(self):
        self.assertFalse(forbidden('string', 'p', 'i'))

    def test_forbidden_multiple_words(self):
        fname = open('/tmp/wordlist.txt', 'r')
        word_list = fname.read().splitlines()
        for i in word_list:
            forbidden(i, 'y', 'x', 'l')

if __name__ == '__main__':
    unittest.main()
