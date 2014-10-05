# Test case for run_stack.py
from nose.tools import *
import stack.run_stack as stack


def test_loop():
    loop = stack.Interactive_Stuff()
    loop.looper()
