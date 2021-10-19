"""
This module shows how to ITERATE (i.e. loop) through a SEQUENCE:
  -- list
  -- string
  -- tuple

It shows two ways to do so:
  -- using RANGE
  -- using just IN (no RANGE)

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  September 2015.
"""

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_color_changes()
    test_sum_all()
    test_sum_all_without_range()


def test_color_changes():
    """ Tests the   color_changes   function. """
    print('--------------------------------------------------')
    print('Testing the   color_changes   function:')
    print('See the two graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # Test 1: Flashes red, white, blue -- 5 times.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400, 180, 'Red, white and blue!',
                           canvas_color='dark gray')

    circle = rg.Circle(rg.Point(150, 100), 40)
    circle.attach_to(window.initial_canvas)

    number_of_cycles = 5
    window.continue_on_mouse_click('Click anywhere in here to start')

    for _ in range(number_of_cycles):
        color_changes(window, circle, ['red', 'white', 'blue'])

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Test 2: Flashes through a bunch of colors,
    # forwards in rectangle, then backwards in an ellipse.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(450, 250, 'Colors!', canvas_color='yellow')

    rect_width = 100
    rect_height = 40
    rect_center = rg.Point(125, 100)
    rectangle = rg.Rectangle(rg.Point(rect_center.x - (rect_width / 2),
                                      rect_center.y - (rect_height / 2)),
                             rg.Point(rect_center.x + (rect_width / 2),
                                      rect_center.y + (rect_height / 2)))

    oval_width = 70
    oval_height = 160
    oval_center = rg.Point(300, 100)
    ellipse = rg.Ellipse(rg.Point(oval_center.x - (oval_width / 2),
                                  oval_center.y - (oval_height / 2)),
                         rg.Point(oval_center.x + (oval_width / 2),
                                  oval_center.y + (oval_height / 2)))

    rectangle.attach_to(window)
    ellipse.attach_to(window)

    colors = ['red', 'white', 'blue', 'chartreuse', 'chocolate',
              'DodgerBlue', 'LightPink', 'maroon', 'orchid', 'plum',
              'SteelBlue', 'violet']
    window.render()
    window.continue_on_mouse_click('Click anywhere in here to start')

    # This function call iterates through the colors, drawing rectangles.
    color_changes(window, rectangle, colors)

    # The  reverse  method reverses its list IN PLACE
    # (i.e., it "mutates" its list -- more on that in future sessions).
    colors.reverse()

    window.continue_on_mouse_click()

    # This function call iterates through the colors, drawing ellipses.
    color_changes(window, ellipse, colors)

    window.close_on_mouse_click()


def color_changes(window, graphics_object, colors):
    """
    Attaches the given rosegraphics graphics object
    (circle, square, ellipse, etc -- anything that has a fill color)
    to the given rg.RoseWindow's initial canvas.  Then:
      -- Iterates through the given sequence of colors, using those
           colors to set the given graphics object's fill color.
      -- At each iteration, renders the window with a brief pause
           after doing so, to create a "flashing" display.

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg._ShapeWithOutline
      :type colors: (list, tuple)
    where the colors are a sequence of RoseGraphics colors.
    """
    # ------------------------------------------------------------------
    # EXAMPLE 1.  Iterates through a sequence of colors.
    # ------------------------------------------------------------------
    graphics_object.attach_to(window.initial_canvas)

    for k in range(len(colors)):
        graphics_object.fill_color = colors[k]
        window.render(0.25)


def test_sum_all():
    """ Tests the   sum_all   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_all   function:')
    print('--------------------------------------------------')

    total1 = sum_all([8, 13, 7, 5])
    print('Returned, expected:', total1, 33)

    total2 = sum_all([8, -8, 13, 7, 5, -13, -20])
    print('Returned, expected:', total2, -8)

    total3 = sum_all([])
    print('Returned, expected:', total3, 0)


def sum_all(sequence):
    """
    Returns the sum of all the items in the given sequence of numbers.
    Precondition: The argument is a sequence of numbers.
    """
    # ------------------------------------------------------------------
    # EXAMPLE 2.  Iterates through a sequence of numbers, summing them.
    # ------------------------------------------------------------------
    total = 0
    for k in range(len(sequence)):
        total = total + sequence[k]

    return total


def test_sum_all_without_range():
    """ Tests the   test_sum_all_without_range   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_all_without_range   function:')
    print('--------------------------------------------------')

    total1 = sum_all_without_range([8, 13, 7, 5])
    print('Returned, expected:', total1, 33)

    total2 = sum_all_without_range([8, -8, 13, 7, 5, -13, -20])
    print('Returned, expected:', total2, -8)

    total3 = sum_all_without_range([])
    print('Returned, expected:', total3, 0)


def sum_all_without_range(sequence):
    """
    Returns the sum of all the items in the given sequence of numbers.
    Precondition: The argument is a sequence of numbers.
    """
    # ------------------------------------------------------------------
    # EXAMPLE 3.  Iterates through a sequence of numbers, summing them.
    #   Same as Example 2, but uses the "no range" form.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # This shows how you can iterate through a sequence WITHOUT using
    # a range expression, IF you do not need the index variable.
    # You can ALWAYS use the form above that uses RANGE;
    # this form is just "syntactic sugar."  Use this form if you like,
    # but be aware of its limitation, and don't confuse the two forms!
    # ------------------------------------------------------------------
    total = 0
    for number in sequence:
        total = total + number

    return total

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
