"""
Test 2, problem 2.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Gupta.  April 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math
import random
import problem2t_tests

########################################################################
# IMPORTANT:
#   Your instructor will explain the "big picture" of this exercise.
########################################################################


def main():
    """
    Calls the   TEST   functions in this module, but ONLY if
    the method to be tested has at least a partial implementation.
    That is, a  TEST   function will not be called
    until you begin work on the code that it is testing.
    """
    if problem2t_tests.is_implemented('slope'):
        test_slope()
    if problem2t_tests.is_implemented('change_wind_speed'):
        test_change_wind_speed()
    if problem2t_tests.is_implemented('throw_n_times'):
        test_throw_n_times()
    if problem2t_tests.is_implemented('get_number_of_throws'):
        test_get_number_of_throws()
    if problem2t_tests.is_implemented('new_stick'):
        test_new_stick()
    if problem2t_tests.is_implemented('midpoint_closest_to_point'):
        test_midpoint_closest_to_point()


########################################################################
# The   STICK  class is here.  TESTS for it are further down.
########################################################################


class Stick(object):
    """
    Represents a magic "Stick" that can GROW and be THROWN.
    When it is THROWN, it moves in unpredictable ways, as if blown
    about by a shifting wind, before magically stopping in mid-air.
    """

    def __init__(self, line, wind_speed):
        """
        What comes in:
          -- self
          -- An rg.Line
          -- A positive number that describes how strong the "wind" is.
               -- Stronger (bigger) winds cause wilder movement
                  when the Stick is thrown.
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Stores the given rg.Line and wind_speed
               in instance variables named, respectively:
                    line     wind_speed
          -- [Eventually] Sets additional instance variables
                          as needed for other methods.
        Example:
        Type hints:
            :type line: rg.Line
            :type initial_spin_rate: int
        """
        ################################################################
        # DONE: 2.
        #   READ the green doc-string (specification) above.  If you
        #   do not understand it, ASK YOUR INSTRUCTOR to explain it.
        #
        #     Note: Recall that an rg.Line has:
        #       -- instance variables   start   and   end   for
        #            its two endpoints.
        #       -- a method  get_midpoint()  that returns the midpoint
        #            of the rg.Line.
        #
        #   Do NOT change this method at this time!  You will need
        #   to AUGMENT this method later for some of the other methods.
        #
        #   Mark this TODO as DONE when you feel like you understand
        #   this method.
        ################################################################
        self.line = line
        self.wind_speed = wind_speed
        self.count = 0

    def __repr__(self):
        """
        What comes in:
          -- self
        What goes out:
          Returns a string that represents this Stick.
          The string has the form of the following example:
              STICK: (100, 150) to (180, 30), wind_speed = 30.8
          where:
            -- the first pair of numbers indicates the current position
                 (x and y coordinates) of one end of this Stick
            -- the second pair of numbers indicates the current position
                 (x and y coordinates) of the other end of this Stick
            -- the last number is the current wind_speed
        Side effects: None.
        """
        # --------------------------------------------------------------
        # We have already implemented this  __repr__  function for you.
        # Do NOT modify it.
        # --------------------------------------------------------------

        f_string = 'STICK: ({}, {}) to ({}, {}), wind_speed = {}'
        return f_string.format(self.line.start.x, self.line.start.y,
                               self.line.end.x, self.line.end.y,
                               self.wind_speed)

    def throw(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects:
          This method moves this Stick in unpredictable ways,
          as if blown about by a shifting wind,
          before magically stopping "in mid-air".

          Also, this method:
            -- Displays the final position of this Stick on the console.
            -- Displays an animation of this Stick moving,
                 in a RoseWindow that WE construct and manage.
        """
        problem2t_tests.throw(self)

    def slope(self):
        """
        What comes in:
          -- self
        What goes out:
          Returns the slope of this Stick's line.
          If this Stick's line is vertical (i.e., has "infinite" slope),
          returns   math.inf
        Side effects: None.
        Example:
        Type hints:
            :rtype float
        """
        ################################################################
        # DONE: 3.
        #   First, READ the green doc-string (specification) above.
        #     -- ASK QUESTIONS if you do not understand it.
        #   Then, implement and test this method.
        #   We supplied tests (later in this module).
        ################################################################

        if self.line.start.x == self.line.end.x:
            return math.inf
        else:
            return((self.line.end.y - self.line.start.y) / (self.line.end.x - self.line.start.x))

    def change_window_speed(self, new_wind_speed):
        """
        What comes in:
          -- self
          -- A number
        What goes out: Nothing (i.e., None).
        Side effects:
          Changes this Stick's wind_speed to the given new_wind_speed.
        Example:
        Type hints:
            :type new_wind_speed: float
        """
        ################################################################
        # DONE: 4.
        #   First, READ the green doc-string (specification) above.
        #     -- ASK QUESTIONS if you do not understand it.
        #   Then, implement and test this method.
        #   We supplied tests (later in this module).
        ################################################################

        self.wind_speed = new_wind_speed

    def throw_n_times(self, n):
        """
        What comes in:
          -- self
          -- a positive integer
        What goes out: Nothing (i.e. None).
        Side effects:
          -- Calls the   throw   method THAT WE WROTE FOR YOU (above)
             the given number of times.
        Example:
        Type hints:
            :type n: int
        """
        ################################################################
        # DONE: 5.
        #   First, READ the green doc-string (specification) above.
        #     -- ASK QUESTIONS if you do not understand it.
        #   Then, implement and test this method.
        #   We supplied tests (later in this module).
        ################################################################

        for i in range(n):
            self.count += 1
            self.throw()

    def get_number_of_throws(self):
        """
        What comes in:
          -- self
        What goes out: Returns the number of times that this Stick
          has been thrown.
            -- Note that a Stick is thrown ONLY by the  thrown_n_times
               method, which throws the Stick MULTIPLE times.
        Side effects: None.
        Example:
        Type hints:
            :rtype int
        """
        ################################################################
        # DONE: 6.
        #   First, READ the green doc-string (specification) above.
        #     -- ASK QUESTIONS if you do not understand it.
        #   Then, implement and test this method.
        #   We supplied tests (later in this module).
        ################################################################

        return self.count

    def new_stick(self, other_stick):
        """
        What comes in:
          -- self
          -- Another Stick
        What goes out: A new Stick for which:
          -- The new Stick's line is midway between this Stick's line
               and the other_stick's line.  (See  problem2.pdf
               for a picture that explains what "midway" means here.)
          -- The new Stick's wind_speed is the smaller of the two
               Stick's wind_speeds.
        Side effects: None.
        Example:
        Type hints:
            :type other_stick: Stick
        """
        ################################################################
        # DONE: 7.
        #   First, READ the green doc-string (specification) above.
        #     -- ASK QUESTIONS if you do not understand it.
        #   Then, implement and test this method.
        #   We supplied tests (later in this module).
        ################################################################

        mid_start_x = (other_stick.line.start.x + self.line.start.x) / 2
        mid_start_y = (other_stick.line.start.y + self.line.start.y) / 2
        mid_start = rg.Point(mid_start_x, mid_start_y)
        mid_end_x = (other_stick.line.end.x + self.line.end.x) / 2
        mid_end_y = (other_stick.line.end.y + self.line.end.y) / 2
        mid_end = rg.Point(mid_end_x, mid_end_y)
        new_stick = Stick(rg.Line(mid_start, mid_end), 0)
        return new_stick

    def midpoint_closest_to_point(self, P):
        """
        What comes in:
          -- self
          -- an rg.Point P
        What goes out: Returns a LIST [X, Y],
          where X and Y are determined as follows:

          Consider the Stick.  Its line has a midpoint M that
          starts out as one value (call it M1).  Each time that the
          Stick is thrown, it ends up stopped "in mid-air".  At each
          stopped time, its line has a midpoint. Lets call
          those midpoints at the stopping times M2, M3, M4, etc.

          Of all those midpoints, one of them is closest to the given
          point P.  (You can break ties however you wish.)
          Lets call that midpoint (the one closest to P)   M_closest.

          This method returns the LIST [X, Y] where X and Y
          are the x and y coordinates of M_closest.
        Side effects: None.
        Examples:
        Type hints:
            :type point: rg.Point
        """
        ################################################################
        # TODO: 8.
        #   First, READ the green doc-string (specification) above.
        #     -- ASK QUESTIONS if you do not understand it.
        #   Then, implement and test this method.
        #   We supplied tests (later in this module).
        ################################################################
        #
        # IMPORTANT: You may find the   distance   function helpful.
        # It is defined immediately below this method.
        # Note that it is a FUNCTION, not a METHOD.
        #
        ################################################################

        # Not right but completely unsure how find the point.

        midpoints = []
        line2 = Stick(rg.Line(self.line.get_midpoint(), P), 0)
        dist = distance(line2.line.start, line2.line.end)
        if len(midpoints) == 0:
            return line2.line.start
        for i in range(self.count - 1):
            midpoints.append(self.line.get_midpoint())
            return midpoints[0]


def distance(point1, point2):
    """
    What comes in: Two rg.Point objects
    What goes out: The distance between those two rg.Point objects.
    Side effects: None.
    Type hints:
      :type point1: rg.Point
      :type point2: rg.Point
    """
    # The usual distance formula:
    delta_x = point1.x - point2.x
    delta_y = point1.y - point2.y
    return math.sqrt((delta_x ** 2) + (delta_y ** 2))

    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  distance  function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


########################################################################
# The TEST functions for the  Stick  class begin here.
########################################################################
def test_slope():
    """ Tests the   slope   method. """
    problem2t_tests.test_slope()  # This runs OUR tests.

    line = rg.Line(rg.Point(100, 70), rg.Point(300, 120))
    stick1 = Stick(line, 1)

    line = rg.Line(rg.Point(100, 70), rg.Point(100, 120))
    stick2 = Stick(line, 1)

    print('\nTest 1:')
    print('Expected:', 0.25)
    print('Actual:  ', stick1.slope())

    print('\nTest 2:')
    print('Expected:', math.inf)
    print('Actual:  ', stick2.slope())


def test_change_wind_speed():
    """ Tests the   change_wind_speed   method. """
    problem2t_tests.test_change_wind_speed()  # This runs OUR tests.

    line = rg.Line(rg.Point(100, 70), rg.Point(300, 120))
    stick1 = Stick(line, 3)

    line = rg.Line(rg.Point(100, 70), rg.Point(100, 120))
    stick2 = Stick(line, 1)

    print('\nTest 1:')
    stick1.change_window_speed(1.5)
    print('Expected:', 1.5)
    print('Actual:  ', stick1.wind_speed)

    print('\nTest 2:')
    stick2.change_window_speed(0.75)
    print('Expected:', 0.75)
    print('Actual:  ', stick2.wind_speed)


def test_throw_n_times():
    """ Tests the   throw_n_times   method. """
    problem2t_tests.test_throw_n_times()  # This runs OUR tests.
    random.seed(42)  # Lets us control the randomness

    line = rg.Line(rg.Point(100, 70), rg.Point(300, 120))
    stick1 = Stick(line, 3)

    print('\nTest 1:')

    stick1.throw_n_times(13)
    print('Expected:', 'Point(1642, 1371) Point(1769, 508)')
    print('Actual:  ', stick1.line.start, stick1.line.end)

    print('\nTest 1, continued:')
    stick1.line.start = rg.Point(40, 50)
    stick1.line.end = rg.Point(80, 20)
    stick1.wind_speed = 0.5

    stick1.throw_n_times(random.randrange(10, 100))
    print('Expected:', 'Point(277, 74) Point(153, 217)')
    print('Actual:  ', stick1.line.start, stick1.line.end)


def test_get_number_of_throws():
    """ Tests the   get_number_of_throws   method. """
    problem2t_tests.test_get_number_of_throws()  # This runs OUR tests.

    line = rg.Line(rg.Point(100, 70), rg.Point(300, 120))
    stick1 = Stick(line, 3)

    line = rg.Line(rg.Point(100, 70), rg.Point(100, 120))
    stick2 = Stick(line, 1)

    print('\nTest 1:')
    print('Expected:', 0)
    print('Actual:  ', stick1.get_number_of_throws())

    stick1.throw_n_times(13)
    print('\nTest 1, continued:')
    print('Expected:', 13)
    print('Actual:  ', stick1.get_number_of_throws())

    print('\nTest 2:')
    print('Expected:', 0)
    print('Actual:  ', stick2.get_number_of_throws())

    print('\nTest 1, resumed:')
    for k in range(100):
        stick1.change_window_speed(42 + k)
        stick1.throw_n_times(k + 42)
        s = stick1.slope()
        if not s or s == math.inf:
            s = 100
        stick1.change_window_speed(42 + s)

    print('Expected:', 13 + (42 + 141) * 50)
    print('Actual:  ', stick1.get_number_of_throws())

    print('\nTest 2, resumed')
    print('Expected:', 0)
    print('Actual:  ', stick2.get_number_of_throws())


def test_new_stick():
    """ Tests the   new_stick   method. """
    problem2t_tests.test_new_stick()  # This runs OUR tests.

    line = rg.Line(rg.Point(100, 70), rg.Point(300, 120))
    stick1 = Stick(line, 3)

    line = rg.Line(rg.Point(150, 10), rg.Point(200, 120))
    stick2 = Stick(line, 5)

    print('\nTest 1:')
    new1 = stick1.new_stick(stick2)
    new2 = stick2.new_stick(stick1)

    if new1 is None or new2 is None:
        print('FAILED tests.  You must RETURN a value.')
        return

    print('Expected:',
          rg.Point(125, 40), rg.Point(250, 120),
          rg.Point(125, 40), rg.Point(250, 120),
          3, 3)
    print('Actual:  ',
          new1.line.start, new1.line.end,
          new2.line.start, new2.line.end,
          new1.wind_speed, new2.wind_speed)


def test_midpoint_closest_to_point():
    """ Tests the   midpoint_closest_to_point   method. """
    problem2t_tests.test_midpoint_closest_to_point()  # Runs OUR tests.
    random.seed(42)  # Lets us control the randomness

    print('\nTest 1:')
    line = rg.Line(rg.Point(100, 70), rg.Point(300, 120))
    stick1 = Stick(line, 1)

    print('Expected:', [200.0, 95.0])
    print('Actual:  ', stick1.midpoint_closest_to_point(rg.Point(100,
                                                                 50)))

    print('\nTest 1, continued:')
    print('Expected:', [200.0, 95.0])
    print('Actual:  ', stick1.midpoint_closest_to_point(rg.Point(-9999,
                                                                 99999)))

    print('\nTest 2:')
    line = rg.Line(rg.Point(110, 200), rg.Point(150, 40))
    stick2 = Stick(line, 0.5)

    print('Expected:', [130.0, 120.0])
    print('Actual:  ', stick2.midpoint_closest_to_point(rg.Point(0,
                                                                 0)))
    print('\nTest 2, continued:')
    stick2.throw_n_times(100)
    print('Expected:', [51.0, 30.0])
    print('Actual:  ', stick2.midpoint_closest_to_point(rg.Point(0,
                                                                 0)))

    print('\nTest 2, continued:')
    print('Expected:', [159.0, 232.0])
    print('Actual:  ', stick2.midpoint_closest_to_point(rg.Point(200,
                                                                 300)))
    print('\nTest 2, continued:')
    stick2.throw_n_times(50)
    print('Expected:', [41.0, 13.0])
    print('Actual:  ', stick2.midpoint_closest_to_point(rg.Point(0,
                                                                 0)))

    print('\nTest 1, resumed:')
    stick1.throw_n_times(100)
    print('Expected:', [69.5, 52.0])
    print('Actual:  ', stick1.midpoint_closest_to_point(rg.Point(100,
                                                                 50)))

    print('\nTest 1, continued:')
    stick1.wind_speed = 3
    stick1.throw_n_times(100)
    print('Expected:', [946.0, 999.0])
    print('Actual:  ', stick1.midpoint_closest_to_point(rg.Point(1000,
                                                                 1000)))

    print('\nTest 1, continued:')
    print('Expected:', [69.5, 52.0])
    print('Actual:  ', stick1.midpoint_closest_to_point(rg.Point(0,
                                                                 0)))

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
