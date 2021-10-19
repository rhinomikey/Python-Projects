"""
Test 1, problem 3.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Gupta.  March 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()


def test_problem3():
    """ Tests the  problem3   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 and 2 of problem3:    '
    title += '6 green lines, then 3 blue lines'
    window = rg.RoseWindow(500, 300, title)

    problem3(150, 230, 6, 'green', window)
    window.continue_on_mouse_click()

    problem3(450, 120, 3, 'blue', window)
    window.close_on_mouse_click()

    # A third test on another window.
    title = 'Test 3 of problem3:    15 red lines'
    window = rg.RoseWindow(400, 500, title)

    problem3(300, 450, 15, 'red', window)
    window.close_on_mouse_click()


def problem3(x1, y1, n, color, window):
    """
    See    problem3_pictures.pdf     for pictures that may help you
    better understand the following specification:

    What comes in:
      -- Two positive integers x1, y1.
      -- A positive integer n.
      -- A string that is a color (e.g. 'red' or 'green' or ...)
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. Draws a rg.Point at (x1, y1).
      2. Draws a rg.Point at (x1, 30).
      3. Draws  n  rg.Lines on the given rg.RoseWindow such that:
           -- All  n  rg.Lines have the given color.
           -- All  n  rg.Lines have (0, 0)
                [the upper-left corner of the window]
                as their leftmost endpoint.
           -- The topmost    rg.Line goes from (0, 0) to (x1, 30),
                and has thickness n.
           -- The bottommost rg.Line goes from (0, 0) to (x1, y1),
                and has thickness 1.
           -- The  n  rg.Lines are equally spaced between the topmost
                and the bottommost, and decrease evenly in thickness
                from top to bottom.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type x1:      int
      :type y1:      int
      :type n:       int
      :type color:   str
      :type window:  rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------

    # I think that this is mostly right but missing something but I'm not sure.

    point = rg.Point(0, 0)
    point1 = rg.Point(x1, y1)
    point2 = rg.Point(x1, y1)

    point.outline_thickness = 5
    point1.outline_thickness = 5
    point.fill_color = 'black'
    point1.fill_color = 'black'

    point.attach_to(window)
    point1.attach_to(window)

    line1 = rg.Line(rg.Point(0, 0), rg.Point(x1, 30))
    line1.attach_to(window)

    line1.thickness = n
    line1.color = color

    for i in range(n - 1):
        line = rg.Line(point, point2)
        point2.y = point2.y - 50

        line.thickness = (n / n) + i

        line.color = color

        line.attach_to(window)

    point3 = rg.Point(x1, 30)
    point3.outline_thickness = 5
    point3.fill_color = 'black'

    point3.attach_to(window)

    window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
