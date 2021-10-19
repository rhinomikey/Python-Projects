"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Gupta.  March 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_draw_bar_chart()


def test_draw_bar_chart():
    """ Tests the   bar_chart   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_bar_chart   function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # The titles are generated using the string   format   method.
    # Ask an assistant to explain if you are curious about them.
    format_string = 'draw_bar_chart(height of 1st bar: {},'
    format_string = format_string + ' increment: {}, width: {}, n: {}'

    # Test 1:
    title = format_string.format(60, 40, 100, 4)
    draw_bar_chart(60, 40, 100, 4, title)

    # Test 2:
    title = format_string.format(100, 20, 50, 10)
    draw_bar_chart(100, 20, 50, 10, title)

    # Test 3:
    title = format_string.format(50, 100, 75, 5)
    draw_bar_chart(50, 100, 75, 5, title)


def draw_bar_chart(height_of_first_bar, height_increment, bar_width, number_of_bars, title):

    window = rg.RoseWindow(1000, 1000)

    rectangle = rg.Rectangle(rg.Point(10 + bar_width, 650 - height_of_first_bar),
                             rg.Point(10, 650 + height_of_first_bar))

    for i in range(1, number_of_bars + 1):
        rectangle1 = rg.Rectangle(rg.Point(rectangle.get_lower_right_corner().x + bar_width * i,
                                           rectangle.get_lower_right_corner().y),
                                  rg.Point(rectangle.get_upper_left_corner().x + bar_width * i,
                                           rectangle.get_upper_left_corner().y - height_increment * i))
        rectangle1.attach_to(window)

    rectangle.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    """
    See   draw_bar_chart.pdf   in this project for pictures that may
    help you better understand the following specification:

    What comes in: 4 integers, plus a string, where:
      -- height_of_first_bar:  is the height of the first (leftmost)
            bar of a bar chart.
      -- height_increment:  is the constant amount by which the heights
            of the bars increase as you move left-to-right.
            (For example, if the 1st bar has height 9 and
            height_increment is 3, then the 2nd bar has height 12,
            the 3rd has height 15, the 4th has height 15, and so forth.)
      -- bar_width:  is the width of each bar (all bars have same width)
      -- number_of_bars:  is the number of bars to draw.
      -- title:  is a title to use when constructing the RoseWindow,
                   like this:   rg.RoseWindow(width, height, title)
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. Constructs a rg.RoseWindow that has the given title.
           -- The window should be large enough to hold
                the entire bar chart, with a reasonable number of
                extra pixels on each side.
      2. Draws a bar chart on it.
           The bars are vertical.  All have the same (given) width.
           The leftmost bar has the given height.
           As you go left-to-right, the bar heights increase
           by the constant  height_increment  specified.
      3. Pauses after drawing, waiting for the user to click the mouse
           in the window, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e of Session 4,
    #             instead of directly using the loop variable.
    # Also: ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
