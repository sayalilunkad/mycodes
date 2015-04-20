#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import re
import sys
import unittest

# Write a function called sed that takes as arguments a pattern string, a
# replacement string, and two file names; it should read the first file and
# write the contents into the second file(creating it if necessary) If the
# pattern string appears anywhere in the file, it should be replaced with the
# replacement string. If an error occurs while opening, reading, writing or
# closing files, your program should catch the exception, print an error
# message, and exit.


def sed(pattern, replace, file1, file2):
    try:
        fname1 = open(file1, 'r')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit(0)
    try:
        fname2 = open(file2, 'w+')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit(0)
    for line in fname1:
        line = re.sub(r''+re.escape(pattern), replace, line)
        fname2.write(line)
    try:
        fname2.close()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit(0)
    try:
        fname1.close()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        sys.exit(0)

class TestSed(unittest.TestCase):
    def test_sed(self):
        file_test = open('/tmp/original.txt', 'w')
        string = "Unittest is a testing module to write test cases in python."
        file_test.write(string)
        file_test.close()
        sed('test', 'error', '/tmp/original.txt', '/tmp/test.txt')

if __name__ == '__main__':
    unittest.main()
