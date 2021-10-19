"""
Test 3, problem 1.

Authors: David Mutchler, Dave Fisher, their colleagues
              and Nathan Gupta.  May 2016.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()


def test_problem1():
    """ Tests the    problem1    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    problem1()


def problem1():
    """
    Prompts the user for and inputs:
      -- A string
      -- A floating point number
      -- Another string
    in that order (via three separate inputs).

    Then prints, in this order, all on separate lines:
      -- The SECOND of the two strings
      -- The cosine of the floating point number
      -- The FIRST of the two strings FOLLOWED by the SECOND of the
           two strings (all on one line, with one space in between them).

    No input validation is required.  Nothing else should be printed.

    Here is a sample run, where the user input is to the right
    of the colons:
        Enter a string: I went skiing!
        Enter a floating point number: 3.0
        Enter another string: Mickey Mouse
        Mickey Mouse
        -0.9899924966004454
        I went skiing! Mickey Mouse
    """
    # -----------------------------------------------------------------
    # DONE: Implement and test this function.
    #       The testing code is already written for you (above).
    # -----------------------------------------------------------------
    
    string1 = input('Please enter a string: ')
    fnum = input('Please input a decimal number: ')
    string2 = input('Please enter another string: ')
    
    print(string2)
    print(math.cos(float(fnum)))
    print(string1,'',string2)



# ----------------------------------------------------------------------
# Calls main to start the ball rolling.
#   More precisely, calls main only if this module is running at the
#   top level (as opposed to being imported by another module).
#   This structure helps us automate tests of this module.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
