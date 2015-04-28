#!/usr/bin/pythoin2.7
# -*- coding: utf8 -*-

# This exercise is a cautionary tale about one of the most common, and
# difficult to find, errors in Python.
# Write a definition for a class named Kangaroo with the following methods:
# 1. An init method that initializes an attribute named pouch_contents to an
# empty list.append
# 2. A method named put_in_pouch that takes an object of any
# type and adds it to pouch_contents.
# 3. A str method that returns a string representation of the Kangaroo object
# and the con-tents of the pouch.
# Test your code by creating two Kangaroo objects, assigning them to variables
# named kanga and roo, and then adding roo to the contents of kanga’s pouch

class Kangaroo(object):
    def __init__(self):
        self.pouch_content = []

    def put_in_pouch(self, obj):
        self.pouch_content.append(obj)

    def string(self):
        print object.__str__(self)
        for x in self.pouch_content:
            s = object.__str__(x)
            print s

if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(1)
    kanga.put_in_pouch('kanga')
    kanga.put_in_pouch(roo)
    kanga.string()
