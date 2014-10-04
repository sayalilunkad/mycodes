# Implements stack in python using tuples.
# Note: Tuples are immutable.


class MyStack(object):
    '''Implementation of stack in Python using tuple
    Stack functions:
        push(): Add element to the top of the tuple
        pop(): Remove element from the top of tuple and print it
    '''

    def __init__(self):
        '''Initializes the variable for stack.

        self.mystack is a tuple which represents the stack.
        '''
        self.mystack = ()

    def isEmpty(self):
        '''Checks if stack is empty.

        returns 1 if stack has 1 or more elements.
        returns 0 if stack has no elements.
        '''
        if self.mystack:
            return 1
        else:
            return 0

    def push(self, val):
        '''Pushes element to the top of stack

        val1: tuple with new elements to be added
        Adds the new values to self.mystack using
        tup1 = tup2 + tup3 property of tuples
        '''
        val1 = (val,)
        self.mystack += val1

    def pop(self):
        '''Deletes the top of stack element and prints it

        Steps:
            if stack is not empty:
                copies all but top of stack element to new stack
                prints top of stack element
                reinitializes self.mystack
                copies newstack to self.mystack
            else:
                Prints error message
        '''
        if self.isEmpty() == 1:
            i = len(self.mystack) - 1
            newstack = self.mystack[:i]
            print("Element poped: %d") % (self.mystack[i])
            self.reinit()
            self.mystack = newstack
        else:
            print("Cannot pop: Empty Stack")

    def reinit(self):
        '''Reinitializes the stack variable

        Deletes the existing stack tuple
        Reinitializes the stack tuple
        '''
        del self.mystack
        self.mystack = ()


# Nosetests
def test_can_create_a_stack():
    stack = MyStack()
    assert stack


def test_to_check_pop_on_empty_stack():
    stack = MyStack()
    stack.pop()


def test_to_push_to_stack():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert (1, 2, 3) == stack.mystack


def test_to_pop_element_from_stack():
    stack = MyStack()
    stack.push(5)
    stack.push(7)
    stack.push(9)
    stack.pop()
