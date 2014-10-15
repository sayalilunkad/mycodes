# Program to optimize reading of last n lines from a file.
import sys

import stack
'''
Usage:
    python lines.py filename number_of_lines_to_read
'''


class line():
    def __init__(self):
        '''
        Initializes:
            1)File handle
            2)Number of lines to be read
            3)Stack
        '''
        self.fhandle = open(sys.argv[1], 'r')
        self.lines_to_read = int(sys.argv[2])
        self.mystack = stack.MyStack()

    def push_all_lines_to_stack(self):
        '''Pushes all the lines in file to the stack.'''
        for lines in self.fhandle:
            self.mystack.push(lines)

    def pop_required_lines(self):
        '''Pops required lines.'''
        temp_stack = stack.MyStack()
        loc = self.lines_to_read
        while loc != 0:
            temp_stack.push(self.mystack.pop())
            loc -= 1

        while self.lines_to_read != 0:
            sentence = temp_stack.pop()
            self.lines_to_read -= 1
            print(sentence)


@profile
def main():
    test = line()
    test.push_all_lines_to_stack()
    test.pop_required_lines()


if __name__ == '__main__':
    main()
