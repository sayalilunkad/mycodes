# Program which uses 20KB memory to read 1GB text.

import sys
import os


class MyFile():
    def get_file(self):
        '''Gets a file name.'''
        self.fname = "/home/sayali/sample.txt"
        return self.fname

    def open_file(self):
        '''Opens file.'''

        f = self.get_file()
        fhandle = open(f, 'r')
        return fhandle

    def get_file_size(self):
        '''Gets size of file.'''

        f = self.get_file()
        filesize = os.path.getsize(f)
        print("Size of file in bytes: %d") % (filesize)
        return filesize

    def get_line_count(self):
        '''Gets line count of file.'''

        count = 0
        f = self.open_file()
        for lines in f:
            count += 1
        print("Total lines: %d") % (count)

    def get_memory_useage(self):
        '''Shows memory used to read file.'''

        f = self.open_file()
        # memory = 0
        for lines in f:
            pass
        #    memory += sys.getsizeof(lines)
        # print("Memory in bytes: %d") % (memory)

'''
    if __name__ == '__main__':
    myfile = MyFile()
    # myfile.get_file_size()
    # myfile.get_line_count()
    myfile.get_memory_useage()
'''
