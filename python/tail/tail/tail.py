# Program to optimize reading of last n lines from a file.
import sys

from tail import file_read
from tail import stack
'''
Usage:
    python tail.py filename number_of_lines_to_read
'''


class line():
    def __init__(self):
        '''
        Initializes:
            1)File handle
            2)Number of lines to be read
            3)Stack
        '''
        self.lines_to_read = int(sys.argv[2])
        self.fileread = file_read.MyFile()
        self.mystack = stack.MyStack()

    def push_lines_to_stack(self):
        '''Pushes all the lines in file to the stack.'''
        fhandle = self.fileread.open_file(sys.argv[1])
        linecount = self.fileread.get_line_count(sys.argv[1])
        tempfile = file_read.MyFile()
        handle = tempfile.open_file(name="output.txt", mode="a")
        for lines in fhandle:
            if linecount <= self.lines_to_read:
                # self.mystack.push(lines)
                handle.write(lines)
            else:
                linecount -= 1
        print("Check output.txt for the output!")

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
    test.push_lines_to_stack()
    # test.pop_required_lines()


if __name__ == '__main__':
    main()
