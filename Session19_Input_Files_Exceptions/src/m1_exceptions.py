"""
This project demonstrates EXCEPTIONS
and TRY/EXCEPT for catching and handling them.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# DONE: 2.
#   1. READ example1, then run it.  [Change  main  to do so.]
#      Then answer these questions (RIGHT HERE IN THIS DOCUMENT):
#      a. When example1 runs, does it print "DONE running example1"?

#            No.

#         Briefly explain why or why not.
#           Your explanation:The program caught an exception and decided to exit the program.
#      b. Does it print a stack trace?  No.
#         Briefly explain why or why not.
#            Your explanation:The exception was caught.
#
#   2. READ example2, then run it.  [Change  main  to do so.]
#      Then answer these questions (right here in this document):
#      a. When example2 runs, does it print "DONE running example2"?

#            Yes

#         Briefly explain why or why not.
#           Your explanation:The error in the program is caught and ignored.
#      b. Does it print a stack trace?  No.
#         Briefly explain why or why not.
#            Your explanation:The exception was caught and ignored.
#
#   3a. READ example3a, then run it.  [Change  main  to do so.]
#      Then answer these questions (right here in this document):
#      a. When example3a runs, does it print "DONE running example3a"?
#            
#             No.

#         Briefly explain why or why not.
#           Your explanation: There is an error in the program and it cannot continue to run.
#      b. Does it print a stack trace?  Yes.
#         Briefly explain why or why not.
#            Your explanation:There is an error so program cannot continue to run.
#
#   3b. READ example3b, then run it. [Change  main  to do so.]
#      Then answer these questions (right here in this document):
#      a. When example3b runs, does it print "DONE running example3b"?
#            
#                 No.

#         Briefly explain why or why not.
#           Your explanation: It doesn't have the exception checker to check if there was a division by zero.
#      b. Does it print a stack trace?  Yes.
#         Briefly explain why or why not.
#            Your explanation: There is an error in the program.
#
#   After you have PUT YOUR ANSWERS IN THIS FILE as described above,
#   change the above TODO to DONE.
########################################################################
import time
import sys


def main():
    """ Calls the other functions in this module to demo EXCEPTIONS. """
    example1()
#     example2()
#     example3a()
#     example3b()


########################################################################
# The following EXAMPLE functions are the SAME in that:
#   Each computes slopes, letting "rise" be 100 and "run" varying:
#     -50, -40, -30, ... 40, 50.
#   So a loop that goes 11 times.
#
#   After computing each slope, the function calls a method  foo(slope)
#   that simulates doing something real with the slopes. (It actually
#   just prints the slope.)
#
#   When run is 0, a divide-by-zero exception occurs.
#
# The following EXAMPLE functions DIFFER in that:
#   example1: catches the exception and exits the program
#             after printing a message.
#   example2: same as #1, but continues the program
#             from where it left off (i.e, next time through the loop).
#   example3a: does NOT catch the exception, thus letting the CALLER
#             catch and handle it (or the caller's caller, or ...).
#   example3b: same as #3a, but catches exception then re-raises it.
########################################################################

def foo(slope):
    """ Could do anything with the slope. This just prints it. """
    print(slope)
    time.sleep(0.5)  # Short pause so we can see the run step by step


########################################################################
# Example 1:  CATCH the Exception, print a message,
#             then EXIT the program.
########################################################################
def example1():
    print('Running example1: CATCH the Exception,')
    print('                  print a message, then EXIT the program.')

    rise = 100
    for run in range(-50, 51, 10):  # Do 100/-50, then 100/-40, then ...
        try:
            slope = rise / run
            foo(slope)
        except ArithmeticError:  # Catches divide by zero AND others
            print('   CAUGHT AN EXCEPTION!')
            print('   Oops! Probably a divide by zero.')
            print('   I will EXIT THE PROGRAM now.')
            sys.exit()

    print('DONE running example1.')
    print()


########################################################################
# Example 2:  CATCH the Exception, print a message,
#             then CONTINUE the program from where it left off.
########################################################################
def example2():
    print('Running example2:')
    print('        CATCH the Exception,')
    print('        print a message,')
    print('        then CONTINUE the program from where it left off.')

    rise = 100
    for run in range(-50, 51, 10):  # Do 100/-50, then 100/-40, then ...
        try:
            slope = rise / run
            foo(slope)
        except ArithmeticError:  # Catches divide by zero AND others
            print('   CAUGHT AN EXCEPTION!')
            print('   Oops! Probably a divide by zero.')
            print('   I will CONTINUE the program from where I')
            print('   left off (i.e., the next time thru the loop.)')

    print('DONE running example2.')
    print()


########################################################################
# Example 3a:  Do NOT CATCH the Exception.
#    Let the Caller (or Caller's Caller...) catch and handle
#    the Exception.  In Example3a, NOBODY catches the Exception.
########################################################################
def example3a():
    print('Running example3a:')
    print('        Do NOT CATCH the Exception.')
    print('        Let the Caller (or Caller\'s Caller...)')
    print('        catch and handle the Exception.')
    print('        In this example, NOBODY will catch the Exception.')

    do_example3()

    print('DONE running example3a.')
    print()


def do_example3():
    rise = 100
    for run in range(-50, 51, 10):  # Do 100/-50, then 100/-40, then ...
        slope = rise / run
        foo(slope)


########################################################################
# Example 3b:  Do NOT CATCH the Exception.
#    Let the Caller (or Caller's Caller...) catch and handle
#    the Exception.  In Example3b, the CALLER catches and handles it.
# The caller chooses to re-RAISE the Exception in this example.
########################################################################
def example3b():
    print('Running example3b:')
    print('        Do NOT CATCH the Exception.')
    print('        Let the Caller (or Caller\'s Caller...)')
    print('        catch and handle the Exception.')
    print('        In this example, the CALLER catches and handles it.')
    print('        The caller chooses to re-RAISE the Exception')
    print('        in this example.')

    try:
        do_example3()
    except Exception:
        print('   The CALLER caught an EXCEPTION!')
        print('   This example catches ANY exception generated.')
        print('   Then it re-RAISEs the Exception,')
        print('   thus passing it along to the Caller,')
        print('   or the Caller\'s Caller, or ...')

        raise

    print('DONE running example3b.')
    print()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
