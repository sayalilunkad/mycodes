# Test cases for stack.py

from nose.tools import *
import stack.stack as stack


def test_can_create_a_stack_instance():
    stack_instance = stack.MyStack()
    assert stack_instance


def test_to_check_pop_on_empty_stack_instance():
    stack_instance = stack.MyStack()
    stack_instance.pop()


def test_to_push_to_stack_instance():
    stack_instance = stack.MyStack()
    stack_instance.push(1)
    stack_instance.push(2)
    stack_instance.push(3)
    assert (1, 2, 3) == stack_instance.mystack


def test_to_pop_element_from_stack_instance():
    stack_instance = stack.MyStack()
    stack_instance.push(5)
    stack_instance.push(7)
    stack_instance.push(9)
    stack_instance.pop()
