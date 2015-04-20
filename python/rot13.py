#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import unittest

#String Manupilation

# ROT13 is a weak form of encryption that involves “rotating” each letter in a
# word by 13 places. To rotate a letter means to shift it through the alphabet,
# wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and
# ’Z’ shifted by 1 is ’A’. Write a function called rotate_word that takes a
# string and an integer as parameters, and that returns a new string that
# contains the letters from the original string “rotated” by the given amount.
# For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is
# “cubed”.You might want to use the built-in functions ord, which converts a
# character to a numeric code,and chr, which converts numeric codes to
# character


def rotate_word(word, rotateby=7):
    new_word = ''
    for i in word:
            temp = ord(i)
            temp += rotateby
            if temp < 97:
                diff = 97 - temp
                temp = 123 - diff
            elif temp > 122:
                diff = temp - 122
                temp = 96 + diff
            tmp = chr(temp)
            new_word += str(tmp)
    return new_word

class TestRotateWord(unittest.TestCase):
    def test_positive_rotate1(self):
        self.assertEquals(rotate_word('cheer'), 'jolly')

    def test_negative_rotate(self):
        self.assertEquals(rotate_word('melon', -10), 'cubed')

    def test_positive_rotate2(self):
        self.assertEquals(rotate_word('z', 2), 'b')

if __name__ == '__main__':
    unittest.main()
