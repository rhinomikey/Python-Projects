"""
PRACTICE Test 1, problem 3.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.  September 2015.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3a()
    test_problem3b()


def test_problem3a():
    """ Tests the   problem3a   function. """
    # ------------------------------------------------------------------
    # TODO: 2. Implement this TEST function.
    #   It TESTS the  problem3a  function defined below.
    #   Include at least **   3   ** tests, of which
    ####################################################################
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    ####################################################################
    #
    ####################################################################
    # CAUTION: Be sure to test the  ** RETURNED VALUE ** from
    #      problem3a, in ADDITION to testing that it DRAWS correctly.
    ####################################################################
    #
    # HINT: Consider using the same test cases as suggested by
    #       the pictures in    problem3a_picture.pdf  in this project.
    #         -- The pictures ALSO give you correct RETURNED VALUES
    #            to use in your tests.
    # ------------------------------------------------------------------


def problem3a(window, point, n):
    """
    See   problem3a_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    Draws a sequence of  n  rg.Lines on the given rg.RoseWindow,
    as follows:
      -- There are the given number (n) of rg.Lines.
      -- Each rg.Line is vertical and has length 50.
            (All units are pixels.)
      -- The top of the first (leftmost) rg.Line
            is at the given rg.Point.
      -- Each successive rg.Line is 20 pixels to the right
            and 10 pixels down from the previous rg.Line.
      -- The first rg.Line has thickness 1.
      -- Each successive rg.Line has thickness 2 greater than
         the zg.Line to its left, but no greater than 13.
           (So once a rg.Line has thickness 13,
           it and all the rg.Lines to its right have thickness 13.)

    Returns the sum of the thicknesses of the rg.Line's.

    Preconditions:
        :type window: rg.RoseWindow
        :type point: rg.Point
        :type n: int   and n is positive.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------


def test_problem3b():
    """ Tests the   problem3b   function. """
    # Test 1 is ALREADY DONE (here).
    expected = 158
    answer = problem3b(4, rg.Point(100, 50))
    print('Expected and actual are:', expected, answer)

    # Test 2 is ALREADY DONE (here).
    expected = 539
    answer = problem3b(7, rg.Point(30, 30))
    print('Expected and actual are:', expected, answer)


def problem3b(m, point1):
    """
    See   problem3b_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    -- Constructs and displays an rg.RoseWindow
         that is 400 wide by 650 tall.

    -- Draws, on the rg.RoseWindow,  m  SETS of lines, where:
        -- Each SET of lines is drawn by a call to ** problem3a **.
        -- The first set has 3 lines that start at point1
             (the given point).
        -- The second set has 5 lines that start 60 pixels
             directly below point1.
        -- The third set has 7 lines that start 120 pixels
             directly below point1.
        -- The fourth set has 9 lines that start 180 pixels
             directly below point1.
        -- etc until  m  SETS of lines are drawn (where m is given)

       Each set of lines should have widths (thicknesses) per problem3a.

    -- Waits for the user to click the mouse (and displays an appropriate
         message prompting the user to do so), then closes the window.

    -- Returns the sum of the thicknesses of ALL of the lines drawn
         (over all  m  sets of lines).

    Preconditions:
        :type m: int   and is positive
        :type point1: rg.Point
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ####################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   problem3a   function that you implemented above.
    ####################################################################
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
