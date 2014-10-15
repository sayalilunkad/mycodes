# Program which uses 20KB memory to read 1GB text.

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
        return filesize

    def get_line_count(self):
        '''Gets line count of file.'''

        count = 0
        f = self.open_file()
        for lines in f:
            count += 1
        return(count)

    def read_file(self):
        '''Reads the file.'''
        f = self.open_file()
        for lines in f:
            buff = lines
            return buff
