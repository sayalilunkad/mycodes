'''
Implementation of stack in Python using tuple
Stack functions:
    push(): Add element to the top of the tuple
    pop(): Remove element from the top of tuple and print it
'''
# Note: Tuples are immutable.
class MyStack(object):
    def __init__(self):
        # define the tuple
        self.mystack = ()

    def isEmpty(self):
        # Returns 0 if stack is empty
        if self.mystack:
            return 1
        else:
            return 0

    def push(self, val):
        # tup1+=tup2
        val1 = (val,)
        self.mystack+=val1

    def pop(self):
        if self.isEmpty() == 1:
            i = len(self.mystack) - 1
            newstack = self.mystack[:i]
            print "Element poped: %d" % self.mystack[i]
            self.reinit()
            self.mystack = newstack
        else:
            print("Cannot pop: Empty Stack")

    def reinit(self):
        del self.mystack
        self.mystack = ()

if __name__ == "__main__":
    s = MyStack()
    s.push(2)
    s.push(1)
    s.push(3)
    print s.mystack
    s.pop()
    print s.mystack
