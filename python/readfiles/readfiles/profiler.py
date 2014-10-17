# Used for profiling file_read.py
'''
Usage:
    python -m memory_profiler profiler.py
'''
import readfiles.file_read as file_read


@profile
def my_func():
    fname = file_read.MyFile()
    fname.read_file()

if __name__ == '__main__':
    my_func()
