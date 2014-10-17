# Test cases for file functions

from nose.tools import *
import readfiles.file_read as readfile


def test_get_file():
    filename = readfile.MyFile()
    assert filename.get_file() == "/home/sayali/sample.txt"


def test_open_file():
    filename = readfile.MyFile()
    assert filename.open_file()


def test_file_size():
    filename = readfile.MyFile()
    print("%d") % (filename.get_file_size())


def test_line_count():
    filename = readfile.MyFile()
    print("%d") % (filename.get_line_count())


def test_file_read():
    pass
