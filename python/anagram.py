#!/usr/bin/python2.7
# -*- coding: utf8 -*-
import sys
# Tuples: Write a program that reads a word list from a file and prints all the
# sets of words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas','desalt','lasted','salted','slated','staled']
# ['retainers','ternaries']
# ['generating','greatening']
# ['resmelts','smelters','termless']
#
# Modify this program so that it prints the largest set of anagrams first,
# followed by the second largest set, and so on

def file_to_list():
    fname = open("/tmp/wordlist.txt", 'r')
    word_list = []
    while(True):
        line = fname.readline()
        if line == '':
            break
        else:
            line_len = len(line)
            word_list.append(line[:line_len-1])
    return word_list


def anagram(word_list):
    len_list = len(word_list)
    if len_list == 1:
        sys.exit(1)
    new_list = []
    i = 1
    while i < len(word_list):
        if (set(word_list[0]) == set(word_list[i])):
            new_list.append(word_list[i])
            del word_list[i]
            new_list.append(word_list[0])
        else:
            i = i + 1
    del word_list[0]
    if new_list != []:
        print new_list
    anagram(word_list)


if __name__ == '__main__':
    l = file_to_list()
    anagram(l)
