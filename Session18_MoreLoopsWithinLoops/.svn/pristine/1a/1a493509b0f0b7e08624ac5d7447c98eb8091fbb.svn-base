"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  October 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    test_draw_upside_down_wall()


def test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    
    width = rectangle.get_width()
    height = rectangle.get_height()
    
    start_corner = rectangle.corner_1
    end_corner = rectangle.corner_2
    
    for i in range(n):
        rect = rectangle.clone()
        rect.corner_1.x = start_corner.x - (width/2)*i
        rect.corner_2.x = end_corner.x - (width/2)*i
        rect.corner_1.y = start_corner.y - (height)*i
        rect.corner_2.y = end_corner.y - (height)*i
        
        for j in range(i+1):
            rect = rect.clone()
            rect.attach_to(window)
            rect.corner_1.x = rect.corner_1.x + width
            rect.corner_2.x = rect.corner_2.x + width
            
    window.render()
        

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
