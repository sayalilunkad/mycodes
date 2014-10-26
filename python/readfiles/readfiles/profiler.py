# Used for profiling file_read.py
'''
Usage:
    python -m memory_profiler profiler.py
'''
from readfiles import file_read


@profile
def my_func():
    fname = file_read.MyFile('sample.txt')
    for lines in fname.read_file():
        # print lines
        pass

if __name__ == '__main__':
    my_func()
