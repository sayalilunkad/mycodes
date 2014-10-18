# Test cases for file functions

from nose.tools import *
import readfiles.file_read as readfile


def test_get_file():
    filename = readfile.MyFile()
    assert filename.get_file(name="sample.txt") == "sample.txt"


def test_open_file():
    filename = readfile.MyFile()
    assert filename.open_file(name="sample.txt")


def test_file_size():
    filename = readfile.MyFile()
    print("%d") % (filename.get_file_size(name="sample.txt"))


def test_line_count():
    filename = readfile.MyFile()
    print("%d") % (filename.get_line_count(name="sample.txt"))


def test_file_read():
    filename = readfile.MyFile()
    filename.read_file(name="sample.txt")
