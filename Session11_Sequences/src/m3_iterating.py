"""
This module lets you practice the ITERATE-THROUGH-A-SEQUENCE pattern
in its most classic form:
  -- Iterate all the way through the sequence, from beginning to end.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_count_negative()
    test_count_short_ones()
    test_draw_circles()


def test_count_negative():
    """ Tests the   count_negative   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  count_negative  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests beyond those we wrote.
    #
    # Use the same 4-step process as for previous TEST functions:
    #   Step 1: Read the green doc-string (below) that provides the
    #     specification of the function you are to test.
    #     Understand what that function SHOULD return.
    #
    #   Step 2:  Pick a test case:  numbers that you could send as
    #     actual arguments to the function.
    #
    #   Step 3: Figure out (by hand, or by trusting a test case that
    #     your instructor provided) the CORRECT (EXPECTED) answer
    #     for your test case.
    #
    #   Step 4: Write code that prints both the EXPECTED answer
    #     and the ACTUAL answer returned when you call the function.
    #     Follow the same form as in the test case we provided below.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_negative   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 1
    actual = count_negative([8, 13, 7, -5])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2:
    expected = 0
    actual = count_negative([])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 3:
    expected = 0
    actual = count_negative([3, 2.5, 3])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 4:
    expected = 4
    actual = count_negative([-500, -500, -500, -0.0000001])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Add your 2 ADDITIONAL tests here:
    
    expected = 2
    actual = count_negative([-29, 1, 60, -0.000000000000000000001])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)
    
    expected = 0
    actual = count_negative([9, 2, 4, 3])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)


def count_negative(seq):
    """
    What comes in:  An sequence of numbers.
    What goes out:  Returns the number of items in the given sequence
      that are negative.
    Side effects:   None.
    Examples:
      count_negative([8, 13, 7, -5])  returns  1
      count_negative([])  returns  0
      count_negative([3, 2.5, 3])  returns  0
      count_negative([-500, -500, -500, -0.0000001])  returns  4
    Type hints:
      :type seq: [float]
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    
    count =0
    for i in range(len(seq)):
        if seq[i] < 0:
            count+=1
    return count

def test_count_short_ones():
    """ Tests the   count_short_ones   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  count_short_ones  function defined below.
    #   Include at least ** 2 ** ADDITIONAL tests beyond those we wrote.
    #
    # Use the same 4-step process as for previous TEST functions.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_short_ones   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 5
    seq = [[3, 5],
           [3, 9, 0, 4],
           [5],
           [5],
           [],
           [9, 8, 7],
           [5, 6]]
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2:
    expected = 3
    seq = ['all', 'we', 'need', 'is', 'peace', '', 'short', '123']
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 3:
    expected = 6
    seq = ['abc', 'a', '', 'foo', 'de', 'dd', 'x', 'foo', 'argh', 'a']
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 4:
    expected = 0
    seq = []
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 5:
    expected = 1
    seq = [[]]
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 6:
    expected = 4
    seq = [[], [], [], []]
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 7:
    expected = 0
    seq = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Add your 2 ADDITIONAL test(s) here:

    expected = 2
    seq = [[1], [1, 1, 1,6,9,0], [], [5000,8000,629404]]
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)
    
    expected = 3
    seq = [[0,0,0,0,0], [], ['', 1], ['', '']]
    actual = count_short_ones(seq)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

def count_short_ones(seq_of_lists):
    """
    What comes in:  An sequence of sequences.
    What goes out:  Returns the number of sub-sequences in the given
      sequence whose length is less than 3.
    Side effects:   None.

    Examples:
    If the argument is:
        [ [3, 5],  [3, 9, 0, 4],  [5],  [5],  [],  [9, 8, 7],  [5, 6] ]
    then this function returns 5, since 5 of the 7 lists in the
    above sequence have length less than 3.

    If the argument is:
        ['all', 'we', 'need', 'is', 'peace', '', 'short', '123'],
    then this function returns 3, since 'we' and 'is' and ''
    all have length less than 3.

    Type hints:
      :type seq_of_lists: [[]]
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
        
    count=0
    for i in range(len(seq_of_lists)):
        if len(seq_of_lists[i]) < 3:
            count+=1 
    return count

def test_draw_circles():
    """ Tests the   draw_circles   function. """
    # ------------------------------------------------------------------
    # We have supplied two tests for you, on a single window.
    # No additional tests are required, although you are welcome to
    # supply more tests if you choose.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_circles   function:')
    print('See the window that pops up.')
    print('--------------------------------------------------')

    window = rg.RoseWindow(450, 350, 'Points to Circles')

    points1 = [rg.Point(200, 100),
               rg.Point(100, 130),
               rg.Point(150, 200)]

    points2 = [rg.Point(50, 50),
               rg.Point(250, 250)]

    points3 = []
    for k in range(40):
        points3.append(rg.Point((10 * k) + 10, 10))

    draw_circles(window, points1, 15, 'red')  # Test 1: 3 red circles
    message = 'You should see 3 SMALL RED circles.\n'
    message += 'Click to continue'
    window.continue_on_mouse_click(message)

    draw_circles(window, points2, 40, 'blue')  # Test 2: 2 blue circles
    message = 'Now you should see 3 small red circles\n'
    message += '** AND **  2 BIG BLUE ones.  Click to continue.'
    window.continue_on_mouse_click(message)

    draw_circles(window, points3, 4, 'purple')  # Test 3: 99 purple dots
    message = 'Now you should see 3 small red and 2 big blue\n'
    message += '** AND **  40 TEENY PURPLE circles.  Click to exit.'
    window.continue_on_mouse_click(message, close_it=True)


def draw_circles(window, points, radius, color):
    """
    What comes in:
      -- An rg.RoseWindow
      -- A sequence of rg.Points
      -- A positive number
      -- A string that can be used as a RoseGraphics color
    What goes out: Nothing (i.e., None).

    Side effects:
    For each point in the given sequence of rg.Points,
    constructs and draws an rg.Circle centered at that point,
    with the given radius and fill color, on the given rg.RoseWindow.
    Renders but does NOT close the given rg.RoseWindow.

    Type hints:
      :type window: rg.RoseWindow
      :type points: [rg.Point]
      :type radius: float
      :type color: str
    """
    # ------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------
    
    for i in range(len(points)):
        circle = rg.Circle(points[i],radius)
        circle.fill_color = color
        
        circle.attach_to(window)
        
    window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
