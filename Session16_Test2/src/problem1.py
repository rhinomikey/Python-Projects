"""
Test 2, problem 1.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Gupta.  April 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st
import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1a()
    test_problem1b()


def is_perfect(n):
    """
    What comes in: A positive integer
    What goes out:
      Returns True if the given integer is PERFECT.
      Returns False if the given integer is NOT PERFECT.
    Side effects: None.
    Type hints:
      :type n: int
    """
    # Definition:  A number is PERFECT if it equals
    # the sum of its proper divisors.  For example,
    # 6, 28, 496 and 8128 are the four smallest PERFECT numbers.

    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_perfect  function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------
    if n <= 2:
        return False

    total = 1
    for k in range(2, int(math.sqrt(n) + 0.001) + 1):
        if n % k == 0:
            total = total + k
            total = total + (n // k)

    return total == n


# ----------------------------------------------------------------------
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
#           See details in the  test  code below.
# ----------------------------------------------------------------------


def test_problem1a():
    """ Tests the    problem1a    function. """
    tests = [st.SimpleTestCase(problem1a,
                               [[rg.Point(28, 6),
                                 rg.Point(5, 13),
                                 rg.Point(24, 6),
                                 rg.Point(5, 6),
                                 rg.Point(28, 6),
                                 rg.Point(6, 5),
                                 ]],
                               rg.Point(28, 6)),
             st.SimpleTestCase(problem1a,
                               [[rg.Point(44, 6),
                                 rg.Point(5, 13),
                                 rg.Point(24, 6),
                                 rg.Point(5, 6),
                                 rg.Point(28, 6),
                                 rg.Point(6, 5),
                                 ]],
                               rg.Point(28, 6)),
             st.SimpleTestCase(problem1a,
                               [[rg.Point(24, 6),
                                 rg.Point(5, 13),
                                 rg.Point(24, 6),
                                 rg.Point(5, 6),
                                 rg.Point(496, 28),
                                 rg.Point(6, 5),
                                 ]],
                               rg.Point(496, 28)),
             st.SimpleTestCase(problem1a,
                               [[rg.Point(20, 6),
                                 rg.Point(5, 13),
                                 rg.Point(24, 6),
                                 rg.Point(5, 6),
                                 rg.Point(22, 6),
                                 rg.Point(493, 24),
                                 ]],
                               'BAD'),
             st.SimpleTestCase(problem1a,
                               [[]],
                               'BAD'),
             st.SimpleTestCase(problem1a,
                               [[rg.Point(23, 6),
                                 rg.Point(5, 13),
                                 rg.Point(496, 6),
                                 rg.Point(5, 6),
                                 rg.Point(20, 6),
                                 rg.Point(6, 5),
                                 ]],
                               rg.Point(496, 6)),

             ]

    st.SimpleTestCase.run_tests('problem1a', tests)


def problem1a(points):
    """
    What comes in:  A sequence of rg.Points.
    What goes out:
      Returns the first (leftmost) rg.Point in the given sequence
      whose x-coordinate and y-coordinate are both PERFECT.
      Returns the string "BAD" if there are no such rg.Points
      in the given sequence.
        -- Use the   is_perfect   function above for judging
             whether or not a number is PERFECT.
    Side effects: None.
    Examples: See the test cases.  Ask if you don't understand them.
    Type hints:
      :type sequence: [rg.Point]
    """
    ####################################################################
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################

    if len(points) == 0:
        return 'BAD'
    for i in range(len(points)):
        if is_perfect(points[i].x) == True and is_perfect(points[i].y) == True:
            return points[i]
    return 'BAD'


def test_problem1b():
    """ Tests the    problem1b    function. """
    tests = [st.SimpleTestCase(problem1b,
                               [2],
                               6),
             st.SimpleTestCase(problem1b,
                               [5],
                               6),
             st.SimpleTestCase(problem1b,
                               [6],
                               28),
             st.SimpleTestCase(problem1b,
                               [7],
                               28),
             st.SimpleTestCase(problem1b,
                               [27],
                               28),
             st.SimpleTestCase(problem1b,
                               [28],
                               496),
             st.SimpleTestCase(problem1b,
                               [500],
                               8128),
             st.SimpleTestCase(problem1b,
                               [1000],
                               8128),
             st.SimpleTestCase(problem1b,
                               [8127],
                               8128),
             ]

    st.SimpleTestCase.run_tests('problem1b', tests)


def problem1b(start):
    """
    What comes in: A positive integer.
    What goes out:
      Returns the smallest PERFECT integer that is strictly bigger
      than the given integer.
      -- Use the   is_perfect   function above for judging
             whether or not a number is PERFECT.
    Side effects: None.
    Examples: See the test cases.  Ask if you don't understand them.
    Type hints:
      :type: start: int
    """
    ####################################################################
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################

    while True:
        start += 1
        if is_perfect(start) == True:
            return start


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
