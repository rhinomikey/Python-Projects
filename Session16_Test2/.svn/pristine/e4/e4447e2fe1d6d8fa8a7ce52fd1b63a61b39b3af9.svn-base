
import rosegraphics as rg
import random
import time
import sys
import inspect
import problem2 as p2

PRINT_SUCCESSES = False
WIDTH = 600
HEIGHT = 500
WINDOW = None
rg._ShapeWithText.defaults['font_size'] = 11  # So messages fit
DO_DRAW = False
random.seed(42)


def evaluate_test(expected, actual, test_title=None, flush_time=0.05):
    """
    Prints the (optional) test_title,
    then prints the expected and actual results for the test.
    If the test FAILED, also prints a failure message in red.
    """
    # If expected is a NUMBER, then actual must also be a number,
    # and their values, rounded to 12 decimal places, must be the same.
    # both in type and in value.  If expected is NOT a number,
    # then actual must match in in both type and value.
    if is_a_number(expected):
        passes_test = (is_a_number(actual) and
                       round(actual, 12) == round(expected, 12))
    else:
        passes_test = (type(actual) is type(expected) and
                       actual == expected)

    global PRINT_SUCCESS
    if PRINT_SUCCESSES or not passes_test:
        print()
        if test_title:
            print(test_title)
        print('Expected:', expected)
        print('Actual:  ', actual, flush=True)
        time.sleep(flush_time)

    if not passes_test:
        print_failure(flush_time=flush_time)


def is_a_number(x):
    """ Returns True if x is an int or a float. """
    return (type(x) is int) or (type(x) is float)


def print_failure(message='  *** FAILED the above test. ***',
                  flush_time=0.05):
    """ Prints a message onto stderr, hence in RED. """
    print(message,
          file=sys.stderr, flush=True)
    time.sleep(flush_time)


def is_implemented(animated_circle_method, expected_lines=2):
    """ True if the given Animated_Circle method is not yet implemenented. """
    # There is probably a better way to do this...
#     method = getattr(p1.Animated_Circle, animated_circle_method)
#     source = inspect.getsource(method)
#     doc_string = method.__doc__
#     expected = source.replace(doc_string, '')
#     lines_left = expected.splitlines()
#
#     return len(lines_left) > expected_lines
    return True


def start_test(what_to_test):
    print()
    print('-----------------------------------------------------------')
    print('Testing the   {}_   method:'.format(what_to_test))
    print('-----------------------------------------------------------')
    return is_implemented(what_to_test)


def throw(stick, number_of_shifts=10, max_x=600, max_y=500,
          time_to_sleep=0.1):
    """
    What comes in: a Stick.
    What goes out: Nothing (i.e., None).
    Side effects:
        This method moves this Stick in unpredictable ways,
        as if blown about by a shifting wind,
        before magically stopping "in mid-air".

        Also, this method:
          -- Displays the final position of this Stick on the console.
          -- Displays an animation of this Stick moving, in a RoseWindow
               that is constructed elsewhere in this module.
    """
    for _ in range(number_of_shifts):
        new_start = rg.Point(random.randrange(max_x * stick.wind_speed),
                             random.randrange(max_y * stick.wind_speed))
        new_end = rg.Point(random.randrange(max_x * stick.wind_speed),
                           random.randrange(max_y * stick.wind_speed))
        stick.line.start = new_start
        stick.line.end = new_end
        global DO_DRAW
        if DO_DRAW:
            draw(stick)
            time.sleep(time_to_sleep)


def start_drawing(title=None):
    global WINDOW, DO_DRAW
    WINDOW = rg.RoseWindow(WIDTH, HEIGHT, title)
    DO_DRAW = True


def end_drawing(message=None):
    global WINDOW, DO_DRAW
    WINDOW.close_on_mouse_click()
    DO_DRAW = False


def draw(stick, message=None):
    """
    Type hints:
      :type stick: Stick
      :type message: str
    """
    stick.line.attach_to(WINDOW)
    WINDOW.render()


def test_slope():
    """ Tests the   slope   method. """
    if not start_test('slope'):
        return


def test_change_wind_speed():
    """ Tests the   change_wind_speed   method. """
    if not start_test('change_wind_speed'):
        return


def test_throw_n_times():
    """ Tests the   throw_n_times   method. """
    if not start_test('throw_n_times'):
        return


def test_get_number_of_throws():
    """ Tests the   get_number_of_throws   method. """
    if not start_test('get_number_of_throws'):
        return


def test_new_stick():
    """ Tests the   new_stick   method. """
    if not start_test('new_stick'):
        return


def test_midpoint_closest_to_point():
    """ Tests the   midpoint_closest_to_point   method. """
    if not start_test('midpoint_closest_to_point'):
        return
