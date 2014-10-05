# Program to add user interactivity for using the stack implementation
# created in the other program Stack.py

import pprint
import sys
import unittest

import stack


class Interactive_Stuff(object):
    '''This class will run kind of on infinite loop till the user wants to exit
    this class will allow the user to interactively use the stack
    implementation in an interactive way!

    Wishlist: Use Multithreading module in python to run different instances of
    this program in infinite loop but only after doing the initial step of
    running it blindly using while or for loop (while is better)

    Also port the menu to ncurses library for much better menu implementation
    after implementing the multithreading part.
    '''

    def __init__(self):
        pass

    class init_stack(object):
        '''Initializes new stack.'''

        def __init__(self):
            pass

        def return_stack(self):
            '''Initializes and returns new stack.'''
            self.s = stack.MyStack()
            return self.s

    def input(self, msg):
        '''Responsible for taking input from the user!'''

        try:
            # Return given datatype
            return input(msg + ': ')
        except Exception:
            # Return string in case of error
            return raw_input(msg + ': ')

    def cprint(self, msg):
        '''Print messages in pretty format!'''

        pretty_print = pprint.PrettyPrinter(indent=4)
        pretty_print.pprint(msg)

    def exit(self, msg, exit_status=0):
        '''Exit the program!'''

        self.cprint(msg)

        try:
            if exit_status is not 0:
                exit_status = 1

        except Exception:
            # If there is an exception in the exit_status then assume that it
            exit_status = 1

        finally:
            sys.exit(exit_status)

    def new_stack(self):
        '''Create and return a new stack object.'''
        new = self.init_stack()
        return new.return_stack()

    def looper(self):
        '''Run the program menu in continous loop.'''
        choice = 0
        nstack = self.new_stack()
        while choice <= 4:
            self.menu()
            choice = input("Enter your choice:")
            if choice == 1:
                # Push to stack
                val = input("Enter element to push:")
                nstack.push(val)
            elif choice == 2:
                # Pop from stack
                nstack.pop()
            elif choice == 3:
                # Check stack status
                empty = nstack.isEmpty()
                if empty == 0:
                    self.cprint("Empty stack!!")
                else:
                    self.cprint("Not Empty")
            elif choice == 4:
                # Print stack elements
                self.cprint("Elements of the stack")
                nstack.print_stack()
            elif choice == 5:
                # Exit
                self.exit('Bye')

    def menu(self):
        '''Print the menu and wait for the option that the use chooses.'''
        print("""
                        ***MENU***
                1. Push Element to stack
                2. Pop Element from stack
                3. Check if stack is empty
                4. Print stack elements
                5 .Exit""")


class testing(unittest.TestCase):

    def test_stack(self):
        start = Interactive_Stuff()
        start.looper()

if __name__ == "__main__":
    unittest.main()
