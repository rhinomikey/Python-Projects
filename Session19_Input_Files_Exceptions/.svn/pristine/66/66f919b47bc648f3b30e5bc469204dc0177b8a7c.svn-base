"""
This module demonstrates lets you practice INPUT from the CONSOLE.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()


def test_problem1():
    """ Tests the   problem1   function. """
    problem1()


def problem1():
    """
    What comes in: Nothing.
    What goes out: Nothing (i.e. None)
    Side effects:
      Prompts the user for and inputs:
        -- A positive floating point number
        -- A positive integer
        -- A string
      in that order (via three separate inputs).
      Then prints, in this order, all on separate lines:
        -- The square root of the floating point number,
           repeated the input integer number of times
        -- The string, repeated the input integer number of times.
      No input validation is required.  Nothing else should be printed.

    Example:
    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    
    fnum = float(input('Please input a decimal number: '))
    inum = int(input('Please input a whole number: '))
    rstr = str(input('Please input a word or a fragment of a sentence: '))
    
    for i in range(inum):
        print(math.sqrt(fnum))
    for i in range(inum):
        print(rstr)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
