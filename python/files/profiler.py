# Used for profiling file_read.py

import file_read


@profile
def my_func():
    fname = file_read.MyFile()
    fname.get_memory_useage()

if __name__ == '__main__':
    my_func()
