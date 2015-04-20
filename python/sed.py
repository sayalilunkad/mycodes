#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import re
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
    fname2 = open(file2, 'w+')
    for line in fname1:
        line = re.sub(r''+re.escape(pattern), replace, line)
        fname2.write(line)
    fname2.close()
    fname1.close()

if __name__ == '__main__':
    sed('test', 'error', '/tmp/original.txt', '/tmp/test.txt')
