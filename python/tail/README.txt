Reads the last 20 lines from a 1GB text file and writes to another file.

Useage:
from tail import tail

Profiling:
python2.7 -m memory_profiler tail/tail.py sample.txt 20

Running nosetests:
nosetests -v -s

Running tox:
tox

