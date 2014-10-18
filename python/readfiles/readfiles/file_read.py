# Program which uses 20KB memory to read 1GB text.

import os


class MyFile():
    def get_file(self, name):
        '''Gets a file name.'''
        self.fname = name
        return self.fname

    def open_file(self, name):
        '''Opens file.'''

        fhandle = open(name, 'r')
        return fhandle

    def get_file_size(self, name):
        '''Gets size of file.'''

        filesize = os.path.getsize(name)
        return filesize

    def get_line_count(self, name):
        '''Gets line count of file.'''

        count = 0
        f = self.open_file(name)
        for lines in f:
            count += 1
        return(count)

    def read_file(self, name):
        '''Reads the file.'''
        buff = ""
        f = self.open_file(name)
        for lines in f:
            buff += lines
            return buff
