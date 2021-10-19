"""
Practice Test, problem 1a.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Gupta.  April 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import math
import random
import sys
import time
import practice_problem1_tests as p1_test
from test.test_colorsys import ColorsysTest

########################################################################
# IMPORTANT:
#   Your instructor will help you get started on this exercise.
########################################################################


def main():
    """
    Calls the   TEST   functions in this module, but ONLY if
    the method to be tested has at least a partial implementation.
    That is, a  TEST   function will not be called
    until you begin work on the code that it is testing.
    """
    if p1_test.is_implemented('__init__'):
        test_init()
    if p1_test.is_implemented('swell_or_shrink_once'):
        test_swell_or_shrink_once()
    if p1_test.is_implemented('swell_or_shrink_repeatedly'):
        test_swell_or_shrink_repeatedly()
    if p1_test.is_implemented('swallow'):
        test_swallow()
    if p1_test.is_implemented('change_color'):
        test_change_color()
    if p1_test.is_implemented('change_to_original_color'):
        test_change_to_original_color()
    if p1_test.is_implemented('swell_to_prime'):
        test_swell_to_prime()
    if p1_test.is_implemented('change_to_previous_color'):
        test_change_to_previous_color()


########################################################################
# The   Animated_Circle   class (and its methods) begins here.
########################################################################
class Animated_Circle(object):
    """ Represents an "animated" circle. """

    def __init__(self, x, y, radius, fill_color, colors):
        """
        What comes in:
          -- self
          -- Three integers: x, y and radius
          -- A string that represents a color in RoseGraphics
               e.g. 'magenta'
          -- A tuple of strings that represent colors in RoseGraphics
               e.g.   ('blue', 'gray', 'light green', 'yellow', 'black')
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Constructs an rg.Circle whose:
               -- center is an rg.Point at the given x and y
               -- radius is the given radius
               -- fill_color is the given fill_color
          -- Stores that rg.Circle in the instance variable:
                   circle
          -- Stores the given tuple of colors in the instance variable:
                   colors
          -- [Eventually] Sets additional instance variables
                          as needed for other methods.
        Example: See   test_init   below for an example.
        Type hints:
            :type x: int
            :type y: int
            :type radius: int
            :type colors: tuple[str]
        """
        ################################################################
        # DONE: 2.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_init   function (below).
        #   Third, implement and test this method.
        #
        # Each TEST function gives an EXAMPLE that helps you understand
        # the SPECIFICATION of the method.  That is why you read the
        # TEST function before implementing the method that it tests.
        ################################################################

        # --------------------------------------------------------------
        # Change the following "animation_factor" if the animations
        # go too fast or too slow for your tastes.  Setting it to N
        # makes the animations go N times SLOWER.
        # --------------------------------------------------------------
        self.animation_factor = 1  # Smaller => faster animations
        self.seconds_to_sleep = 0.5  # Default for each call to draw
        self.x = x
        self.y = y
        self.radius = radius
        self.colors = colors
        self.circle = rg.Circle(rg.Point(x, y), radius)
        self.circle.fill_color = fill_color
        self.color_fill = self.circle.fill_color
        self.color_before = self.circle.fill_color

    def __repr__(self):
        """
        What comes in:
          -- self
        What comes out:
          Returns a string that represents this Animated_Circle.
          The string has the form of the following example:
            ANIMATED_CIRCLE:
              Circle: center=(10, 23), radius=50, fill_color=None,
                      outline_color=black, outline_thickness=1.
              colors: ('blue', 'gray', 'light green', 'black')
        Side effects: None.
        """
        # --------------------------------------------------------------
        # We have already implemented this  __repr__  function for you.
        # Do NOT modify it.
        # --------------------------------------------------------------

        # Break the string for the circle into two lines:
        circle_string = repr(self.circle)
        circle_string = circle_string.replace(' outline_color',
                                              ('\n' +
                                               '          ' +
                                               'outline_color'))

        # Use lower-case C for 'circle' to match instance-variable name:
        circle_string = circle_string.replace('Circle', 'circle')

        s = 'ANIMATED CIRCLE:\n'
        s = s + '  ' + circle_string + '\n'
        s = s + '  ' + 'colors: ' + repr(self.colors)
        return s

    def draw(self, message=None):
        """
        What comes in:
          -- self
          -- an optional message
        What comes out:  Nothing (i.e., None)

        Side effects:
          This method draws and renders this Animated_Circle
          on an rg.RoseWindow.

          Then, if   message   is:
            None (the default):
                This method pauses for the default number of seconds
                (multiplied by self.animation_factor).
            Any number:
                This method pauses for the given number of seconds
                (multiplied by self.animation_factor).
                There is no pause if the number is 0.
            Anything else:
                This method prints the message on the rg.RoseWindow
                and waits for the user to click the mouse.
        """
        # --------------------------------------------------------------
        # We have already implemented this  draw  function for you.
        # Do NOT modify it.
        #
        # You can do this entire exercise knowing only that   draw
        #    "Draws this Animated_Circle on a window,
        #     pausing briefly after doing so."
        #
        # per the green doc_string (specification) above.
        # You do NOT need to know HOW   draw   does its work.
        #
        # But feel free to ask your instructor about it if you
        # are curious as to how   draw   works.
        # --------------------------------------------------------------
        p1_test.draw(self, message)

    def swell_or_shrink_once(self, amount_to_swell_or_shrink):
        """
        What comes in:
          -- self
          -- An integer that indicates how much this Animated_Circle's
               circle is to swell or shrink by, that is, how much
               this Animated_Circle's circle's radius is to change by.        
        What goes out: Nothing (i.e., None).

        Side effects:
        The following happens IN THE ORDER LISTED.
          1. The radius of this Animated_Circle's circle changes
               by adding the given  amount_to_swell_or_shrink  to it.

               So the circle:
                 -- swells if   amount_to_swell_or_shrink   is positive
                 -- shrinks if  amount_to_swell_or_shrink   is negative.

               Exception:  If the change would make the radius
                 LESS THAN 1, the radius should be set to 1.

          2. The outline_thickness of this Animated_Circle's circle
               is set to a random number chosen from [3, 15]
               (that is, between 3 and 15, inclusive).

          3. The fill color of this Animated_Circle's circle
               changes to a color chosen at random from this
               Animated_Circle's list of colors.

        Example: See   test_swell_or_shrink_once   below for examples.

        Type hints:
            :type amount_to_swell_or_shrink: int
        """

        self.circle.outline_thickness = random.randrange(3, 16)

        randnum = random.randrange(0, len(self.colors))

        if self.radius + amount_to_swell_or_shrink < 1:
            self.circle.radius = 1

        self.circle.radius = self.circle.radius + amount_to_swell_or_shrink

        self.circle.fill_color = self.colors[randnum]


        ################################################################
        # DONE: 3.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_swell_or_shrink_once   function
        #   (below).  Third, implement and test this method.
        ################################################################
        #
        # IMPORTANT  ** HINT ** Regarding randomness:
        #
        #   The following statement chooses a random number between
        #   3 and 15, inclusive:
        #       r = random.randrange(3, 16)
        #   Note the 16 --  randrange   is like   range   in that
        #   it does NOT include the ending number.
        #   Use the above to help set the outline_thickness.
        #
        #   To get a random COLOR, you need to get a random INDEX
        #   into the   self.colors   tuple.  So something like:
        #       r_index = random.randrange(0, ??)
        #
        #   where you figure out what ?? must be, and then
        #
        #       r_color = self.colors[r_index]
        #
        #   will give a randomly chosen color from self.colors.
        #
        #   Simply   ** ASK FOR HELP **
        #            if this does not make sense to you.
        ################################################################

    def swell_or_shrink_repeatedly(self,
                                   amount_to_swell_or_shrink,
                                   times_to_swell_or_shrink):
        """
        What comes in:
          -- self
          -- Two integers (see   Side effects  below for what they do)
        What goes out: Nothing (i.e., None).
        Side effects:
          Does the following 4 steps repeatedly:
            1. This Animated_Circle's circle swells/shrinks by the
               given amount_to_swell_or_shrink.
            2. This Animated_Circle is drawn (by its  draw   method).
            3. This Animated_Circle's circle swells/shrinks
               to UNDO the swell/shrink that it just did.
            4. This Animated_Circle is drawn (by its  draw   method).
          The argument  times_to_swell_or_shrink  says how many times
          to do the above 4 steps.
        Example:
          Suppose that the radius of this Animated_Circle's circle
          is currently 50.  Suppose further that:
            -- amount_to_swell_or_shrink is 10
            -- times_to_swell_or_shrink  is 3.
          Then this method would:
            -- Increase the circle's radius to 60.
               Draw the Animated_Circle (by using its   draw   method).
            -- Decrease the circle's radius back to 50.
               Draw the Animated_Circle again.
            -- Increase the circle's radius to 60.
               Draw the Animated_Circle again.
            -- Decrease the circle's radius back to 50.
               Draw the Animated_Circle again.
            -- Increase the circle's radius to 60.
               Draw the Animated_Circle again.
            -- Decrease the circle's radius back to 50.
               Draw the Animated_Circle again.
          So, 3 times it did an increase by 10 followed by a decrease
          by 10.  Since the  draw  method pauses briefly each time
          it is called, this creates an animation.

        Type hints:
            :type amount_to_swell: int
            :type times_to_swell:  int
        """
        ################################################################
        # DONE: 4.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the  test_swell_or_shrink_repeatedly  function
        #   (below).  Third, implement and test this method.
        #
        # *** IMPORTANT:  FULL CREDIT for this method if it
        #     CALLS   swell_or_shrink_once   CORRECTLY,
        #     even if   swell_or_shrink_once   is wrong.
        ################################################################

        for _ in range(times_to_swell_or_shrink):
            self.swell_or_shrink_once(amount_to_swell_or_shrink)
            self.draw()
            self.swell_or_shrink_once(-amount_to_swell_or_shrink)
            self.draw()

    def swallow(self, other_animated_circle):
        """
        What comes in:
          -- self
          -- Another Animated_Circle
        What goes out:
          -- A new Animated_Circle:
             -- whose circle is a new rg.Circle that:
                -- is centered at the point that is MIDWAY between
                     the center of this Animated_Circle's circle and
                     the center of the other Animated_Circle's circle.
                -- has radius that is the SUM of the radius of
                     this Animated_Circle's circle and the radius
                     of the other Animated_Circle's circle.
                -- has 'red' as the  fill color
             -- whose tuple of colors a new tuple
                  that is this Animated_Circle's tuple of colors
                  plus (that is, concatenated with)
                  the other Animated_Circle's tuple of colors.
        Side effects: None.
        Example: See   test_swallow   below for examples.
        Type hints:
            :type other_animated_circle: Animated_Circle
            :rtype Animated_Circle
        """
        # --------------------------------------------------------------
        # DONE: 5.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_swallow   function (below).
        #   Third, implement and test this method.
        # --------------------------------------------------------------

        other_circle = other_animated_circle
        colors = self.colors + other_circle.colors
        mid_x = (other_circle.circle.center.x + self.circle.center.x) / 2
        mid_y = (other_circle.circle.center.y + self.circle.center.y) / 2
        mid_circle = Animated_Circle(mid_x, mid_y, self.circle.radius + other_circle.radius, 'red', colors)
        return mid_circle



    def change_color(self, index_of_color):
        """
        What comes in:
          -- self
          -- An nonnegative integer that is less than the length
               of this Animated_Circle's tuple of colors.
        What goes out: Nothing (i.e., None).
        Side effects:
          -- The fill_color of this Animated_Circle's circle becomes
               the color in this Animated_Circle's tuple of colors
               whose index is the given index_of_color.
        Example:
          If this Animated_Circle's tuple of colors is:
             ('blue', 'gray', 'green', 'black')
          and if index_of_color is 2,
          then the fill_color of this Animated_Circle becomes 'green'.
        Type hints:
            :type index_of_color: int
        """
        # --------------------------------------------------------------
        # DONE: 6.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_change_color   function (below).
        #   Third, implement and test this method.
        # --------------------------------------------------------------

        self.color_before = self.circle.fill_color
        self.circle.fill_color = self.colors[index_of_color]

    def change_to_original_color(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects:
          -- The fill_color of this Animated_Circle's circle becomes
               the same color that it was when this Animated Circle
               was constructed.
        """
        # --------------------------------------------------------------
        # DONE: 7.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_change_to_original_color   function
        #   (below).  Third, implement and test this method.
        # --------------------------------------------------------------

        self.circle.fill_color = self.color_fill

    def swell_to_prime(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects:
          -- The radius of this Animated_Circle's circle increases
               until it equals the first prime number that is strictly
               bigger than the current radius
               of this Animated_Circle's circle.
        Examples:
          If this Animated_Circle's circle currently has radius 8,
          then this method would cause its radius to increase to 11.
          If this Animated_Circle's circle currently has radius 11,
          then this method would cause its radius to increase to 13.
          If this Animated_Circle's circle currently has radius 23,
          then this method would cause its radius to increase to 29.

        IMPORTANT: Use the  is_prime  method defined at the end
        of this module.
        """
        # --------------------------------------------------------------
        # DONE: 8.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_swell_to_prime   function (below).
        #   Third, implement and test this method.
        #
        #   *** IMPORTANT *** Use the   is_prime   method.
        #
        #   It is defined at the end of this module.
        # --------------------------------------------------------------

        while True:
            self.circle.radius += 1
            if is_prime(self.circle.radius) == True:
                break
        return self.circle

    def change_to_previous_color(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        Side effects:
          -- The fill_color of this Animated_Circle's circle becomes
               the same color that it was just BEFORE the most recent
               call to   change_color.
        Example:
          Suppose that the Animated_Circle's circle has fill_color
          'blue' at some point in time.  Suppose that
              change_color('green')
           was called on this Animated_Circle at that point in time,
           so that this Animated_Circle's circle now has fill_color
           that is 'green'.  Suppose further that other things
           then happen, none of which is change_color.  Then when
              change_to_previous_color
           is called on this Animated Circle, its circle should
           change its fill_color back to 'blue'.

           You do NOT have to deal with any scenarios other than the
           example just described (although the scenario in the example
           can occur multiple times).  In particular:
             -- You do not have to deal with what happens if
                  change_to_previous_color   is called twice in a row.
             -- You do not have to deal with what happens if
                  change_to_previous_color   is called before
                  change_color is called at all.  (But the program
                  should not crash in that case.)
        """
        # --------------------------------------------------------------
        # DONE: 9.
        #   First, READ the green doc-string (specification) above.
        #   Second, READ the   test_change_to_previous_color   function
        #   (below).  Third, implement and test this method.
        # --------------------------------------------------------------

        self.circle.fill_color = self.color_before


########################################################################
# The TEST functions for the  Animated_Circle  class begin here.
########################################################################

def test_init():
    """ Tests the   __init__   method of the Animated_Circle class. """
    p1_test.test_init()  # This runs OUR tests.

    # This is a VISUAL test.
    p1_test.start_drawing('Testing: the   __init__   method')

    # Construct two Animated_Circle objects:
    animated_circle1 = Animated_Circle(100, 150, 100, 'blue',
                                       ('red', 'blue', 'green'))
    animated_circle2 = Animated_Circle(300, 50, 30, 'yellow',
                                       ('green', 'gold'))

    # Print and draw them:
    print('After construction:')
    print(animated_circle1, '\n', animated_circle2, '\n', sep='')
    animated_circle1.draw(0.5)
    animated_circle2.draw("""
    A BLUE circle at (100, 150) with radius 100 and thickness 1,
    and a YELLOW circle at (250, 50) with radius 30 and thickness 1.""")

    # Change some of their characteristics, then print and redraw them:
    animated_circle1.circle.fill_color = animated_circle1.colors[2]
    animated_circle2.circle.outline_thickness = 10
    print('After changing characteristics:')
    print(animated_circle1, '\n', animated_circle2, sep='')
    animated_circle1.draw()
    animated_circle2.draw("""
    Now the leftmost (formerly BLUE) circle is GREEN
    and the YELLOW circle has a thicker outline.""")


def test_swell_or_shrink_once():
    """ Tests the   swell_or_shrink_once   method. """
    p1_test.test_swell_or_shrink_once()  # This runs OUR tests
    random.seed(42)  # Lets us determine the results of the randomness

    # This is a VISUAL test.
    # Construct 3 Animated_Circle objects, printing and drawing them.
    p1_test.start_drawing('Testing: the  swell_or_shrink_once   method')
    print('After construction:')
    animated_circle1 = Animated_Circle(200, 150, 30, 'blue',
                                       ('blue', 'yellow', 'green',
                                        'aqua', 'brown'))
    print(animated_circle1)
    animated_circle1.draw()

    animated_circle2 = Animated_Circle(400, 100, 50, 'red', ('green',))
    print(animated_circle2)
    animated_circle2.draw()

    animated_circle3 = Animated_Circle(300, 200, 10, 'green',
                                       ('yellow', 'blue'))
    print(animated_circle3)
    animated_circle3.draw("""
    A BLUE circle at (200, 150) with radius 30 and thickness 1,
    and a RED circle at (400, 100) with radius 50 and thickness 1,
    and a GREEN circle at (300, 200) with radius 10 and thickness 1.""")

    # For each of the three Animated_Circle objects,
    #   apply the   swell_or_shrink_once  method, then redraw/reprint.
    print('\nAfter the first set of    swell_or_shrink_once   calls:')
    animated_circle1.swell_or_shrink_once(100)
    print(animated_circle1)
    animated_circle1.draw()

    animated_circle2.swell_or_shrink_once(-30)
    print(animated_circle2)
    animated_circle1.draw()

    animated_circle3.swell_or_shrink_once(40)
    print(animated_circle3)
    animated_circle3.draw("""
    After the first swell_or_shrink, now:
    Left circle is bigger (radius 130), still BLUE but thickness 13,
    Right circle is smaller (radius 20), GREEN with thickness 3,
    Middle circle is bigger (radius 50), YELLOW with thickness 6.""")

#     # Apply the   swell_or_shrink_once  method to each a second time:
#     animated_circle1.swell_or_shrink_once(-80)
#     animated_circle2.swell_or_shrink_once(30)
#     animated_circle3.swell_or_shrink_once(50)
#
#     print('After the second swell_or_shrink_once:')
#     print(animated_circle1, '\n',
#           animated_circle2, '\n',
#           animated_circle3, '\n', sep='')
#     p1_test.start_drawing('After the second swell_or_shrink_once')
#     animated_circle1.draw()
#     animated_circle2.draw()
#     animated_circle3.draw("""
#     After the second swell_or_shrink:
#     The leftmost circle swelled to radius 130 and thickness 4,
#     and a RED circle at (400, 100) with radius 50 and thickness 1,
#     and a GREEN circle at (300, 200) with radius 10 and thickness 1.""")
#
#     animated_circle1.swell_or_shrink_once(-50)
#     animated_circle2.swell_or_shrink_once(100)
#     animated_circle3.swell_or_shrink_once(70)
#     print(animated_circle1)
#     animated_circle1.draw('Now GREEN, radius 80, thickness 10')


def test_swell_or_shrink_repeatedly():
    """ Tests the   swell_or_shrink_repeatedly   method. """
    p1_test.test_swell_or_shrink_once()  # This runs OUR tests
    random.seed(999)  # Lets us determine the results of the randomness

    # This is a VISUAL test.
    # Construct 1 Animated_Circle object, printing and drawing it.
    title = 'Testing: the  swell_or_shrink_repeatedly   method'
    p1_test.start_drawing(title)

    print('After construction:')
    animated_circle1 = Animated_Circle(200, 150, 30, 'blue',
                                       ('blue', 'yellow', 'green',
                                        'aqua', 'brown'))
    print(animated_circle1)
    animated_circle1.draw("""
    A BLUE circle at (200, 150) with radius 30 and thickness 1.""")

    # Apply the   swell_or_shrink_repeatedly   method.
    print('\nAfter the first   swell_or_shrink_repeatedly   call:')
    animated_circle1.animation_factor = 0.25  # faster animation

    animated_circle1.swell_or_shrink_repeatedly(50, 10)

    print(animated_circle1)
    animated_circle1.draw("""
    The circle should have swelled/shrunk by 50 10 times,
    changing color and thickness each time.
    It should end with the radius that it began (30),
    GREEN with thickness 10.""")


def test_swallow():
    """ Tests the   swallow   method. """
    p1_test.test_swallow()  # This runs OUR tests.

    # This is a VISUAL test.
    # Construct 2 Animated_Circle objects, printing and drawing them.
    title = 'Testing: the  swallow   method'
    p1_test.start_drawing(title)

    print('After construction:')
    animated_circle1 = Animated_Circle(200, 150, 50, 'blue',
                                       ('blue', 'yellow', 'green'))
    animated_circle1.draw()
    print(animated_circle1)
    animated_circle2 = Animated_Circle(250, 180, 30, 'green',
                                       ('yellow', 'magenta'))
    print(animated_circle2)
    animated_circle2.draw("""
    A BLUE circle at (200, 150) with radius 100,
    and a GREEN circle at (350, 200) with radius 70.""")

    # Apply the   swallow   method.  Then print/draw the resulting
    # circle, drawing the original circles on top of it.
    print('\nAfter the first   swallow   call:')

    animated_circle3 = animated_circle1.swallow(animated_circle2)
    print(animated_circle3)
    animated_circle3.draw("""
    The RED circle should be centered at (225, 165) with radius 80.
    It should completely cover the BLUE and GREEN circles.""")

    animated_circle4 = Animated_Circle(200, 150, 50, 'blue',
                                       ('blue', 'yellow', 'green'))
    animated_circle4.draw()
    animated_circle5 = Animated_Circle(250, 180, 30, 'green',
                                       ('yellow', 'magenta'))
    animated_circle5.draw("""
    Here are the BLUE and GREEN circles again, on TOP of the RED circle.
    The RED should appear to BARELY cover the BLUE
    but be MORE THAN NECESSARY to cover the GREEN.""")

    # Test that the swallowing (red) Animated_Circle
    # has a   colors   attribute that is the CONCATENATION
    # of the  colors   attributes of the swallowed Animated_Circles.
    if animated_circle3.colors != (animated_circle4.colors +
                                   animated_circle5.colors):
        message = """The   colors   instance variable
    of the swallowing Animated_Circle (the one RETURNED by
    the   swallow   method) is wrong.
    It should be the CONCATENATION of the   colors   instance
    variables of the two SWALLOWED Animated Circle objects.
    For example, if   animated_circle1.colors   is:
       (blue', 'yellow', 'green')
    and if   animated_circle2.colors   is:
       ('yellow', 'magenta')
    then   animated_circle1.swallow(animated_circle2)   should be:
       ('blue', 'yellow', 'green', 'yellow', 'magenta')
    and    animated_circle2.swallow(animated_circle1)   should be:
       ('yellow', 'magenta', 'blue', 'yellow', 'green')
    """
        time.sleep(0.5)
        print(message, file=sys.stderr)
        print('The   colors   instance  of   animated_circle1   is:',
              '\n   ', animated_circle1.colors, file=sys.stderr)
        print('The   colors   instance  of   animated_circle2   is:',
              '\n   ', animated_circle2.colors, file=sys.stderr)
        print('The   colors   instance  of the swallowing',
              file=sys.stderr)
        print('Animated_Circle (animated_circle3)   is:',
              '\n   ', animated_circle3.colors, file=sys.stderr)
        print('but should be:', file=sys.stderr)
        print("  ('blue', 'yellow', 'green', 'yellow', 'magenta')",
              file=sys.stderr)
        time.sleep(1)


def test_change_color():
    """ Tests the   change_color   method. """
    p1_test.test_change_color()  # This runs OUR tests.
    random.seed(77)  # Lets us determine the results of the randomness

    # This is a VISUAL test.
    # Construct 2 Animated_Circle objects, printing and drawing them.
    title = 'Testing: the  change_color   method'
    p1_test.start_drawing(title)

    print('After construction:')
    animated_circle1 = Animated_Circle(100, 100, 70, 'black',
                                       ('blue', 'yellow'))
    animated_circle1.draw()
    print(animated_circle1)
    animated_circle2 = Animated_Circle(350, 130, 50, 'purple',
                                       ('yellow', 'magenta', 'blue',
                                        'green', 'yellow', 'aqua'))
    print(animated_circle2)
    animated_circle2.draw("""
    A BLACK circle at (100, 100) with radius 70,
    and a PURPLE circle at (350, 130) with radius 50.""")

    # Apply the   change_color   method.  Then print/draw the results.
    print('\nAfter the first set of   change_color   calls:')

    animated_circle1.change_color(1)
    print(animated_circle1)
    animated_circle1.draw()

    animated_circle2.change_color(5)
    print(animated_circle2)
    animated_circle2.draw("""
    Same circles, but now YELLOW and AQUA.
    The next test will cycle the LEFT circle through:
      blue and yellow (repeating as needed)
    and the RIGHT circle through:
      yellow, magenta, blue, green, yellow, and aqua.""")

    # Another test:
    for k in range(6):
        animated_circle1.change_color(k % 2)
        animated_circle1.draw()

        animated_circle2.change_color(k)
        animated_circle2.draw()

    animated_circle1.draw("""
    Should have finished with YELLOW and AQUA.""")

    # This tests   change_color   and   swell_and_shrink_once
    # repeatedly.
    for k in range(20, 0, -1):
        animated_circle1.change_color(k % 2)
        animated_circle1.draw(0.05)
        animated_circle1.swell_or_shrink_once((-40 // k) * (k ** -1))
        animated_circle1.draw(0.05)

        animated_circle2.change_color(k % 6)
        animated_circle2.draw(0.05)
        animated_circle2.swell_or_shrink_once(50 // k)
        animated_circle1.draw(0.05)

    animated_circle1.draw("""
    Should have ended with two YELLOW circles:
    a TINY one on the LEFT and a HUGE one on the RIGHT.""")


def test_change_to_original_color():
    """ Tests the   change_to_original_color   method. """
    p1_test.test_change_to_original_color()  # This runs OUR tests.
    random.seed(123)  # Lets us determine the results of the randomness

    # This is a VISUAL test.
    # Construct 2 Animated_Circle objects, printing and drawing them.
    title = 'Testing: the  change_to_original_color   method'
    p1_test.start_drawing(title)

    print('After construction:')
    animated_circle1 = Animated_Circle(100, 100, 100, 'black',
                                       ('blue', 'green'))
    animated_circle1.draw()
    print(animated_circle1)
    animated_circle2 = Animated_Circle(280, 100, 100, 'purple',
                                       ('yellow', 'magenta', 'blue',
                                        'green', 'yellow', 'aqua'))
    print(animated_circle2)
    animated_circle2.draw("""
    A BLACK circle at (100, 100) with radius 100,
    and a PURPLE circle at (280, 100) with radius 100.
    You will next see a bunch of colors,
    ending with BLACK and PURPLE again.""")

    # Flash through many color changes.  Then apply the
    #   change_to_original_color   method and print/draw the results.
    print('\nAfter the first set of  change_to_original_color  calls:')
    for k in range(30):
        animated_circle1.change_color(k % 2)
        animated_circle1.draw(0.05)

        animated_circle2.change_color(k % 6)
        animated_circle2.draw(0.05)

    animated_circle1.change_to_original_color()
    print(animated_circle1)
    animated_circle1.draw()

    animated_circle2.change_to_original_color()
    print(animated_circle2)
    animated_circle2.draw("""
    Should end as it started: BLACK and PURPLE.""")


def test_swell_to_prime():
    """ Tests the   swell_to_prime   method. """
    p1_test.test_swell_to_prime()  # This runs OUR tests.

    # This is a VISUAL test.
    # Construct 2 Animated_Circle objects, printing and drawing them.
    title = 'Testing: the  swell_to_prime   method'
    p1_test.start_drawing(title)

    print('After construction:')
    animated_circle1 = Animated_Circle(50, 25, 20, 'black',
                                       ('blue', 'green'))
    animated_circle1.draw()
    print(animated_circle1)
    animated_circle2 = Animated_Circle(200, 100, 89, 'purple',
                                       ('yellow', 'magenta', 'blue',
                                        'green', 'yellow', 'aqua'))
    print(animated_circle2)
    animated_circle2.draw("""
    A BLACK circle at (50, 25) with radius 20,
    and a PURPLE circle at (200, 100) with radius 89.""")

    # Apply the   swell_to_prime   method and print/draw the results.
    print('\nAfter the first set of  swell_to_prime  calls:')

    animated_circle1.swell_to_prime()
    print(animated_circle1)
    animated_circle1.draw()

    animated_circle2.swell_to_prime()
    print(animated_circle2)
    animated_circle2.draw("""
    The LEFT circle should have grown from radius 20 to radius 23.
    The RIGHT circle should have grown from radius 89 to radius 97.
    Both should be 3 pixels from the top of the window.""")


def test_change_to_previous_color():
    """ Tests the   change_to_previous_color   method. """
    p1_test.test_change_to_previous_color()  # This runs OUR tests.
    random.seed(4242)  # Lets us determine the results of the randomness

    # This is a VISUAL test.
    # Construct 2 Animated_Circle objects, printing and drawing them.
    title = 'Testing: the  change_to_previous_color   method'
    p1_test.start_drawing(title)

    print('After construction:')
    animated_circle1 = Animated_Circle(100, 100, 20, 'violet',
                                       ('dark red', 'green', 'tomato',
                                        'blue', 'plum', 'seashell',
                                        'red', 'peach puff', 'coral',
                                        'chocolate', 'brown'))
    animated_circle1.draw()
    print(animated_circle1)
    animated_circle2 = Animated_Circle(200, 200, 50, 'orange',
                                       ('yellow', 'magenta', 'blue',
                                        'lavender', 'cyan', 'aqua',
                                        'black', 'salmon', 'hot pink',
                                        'forest green', 'spring green'))
    print(animated_circle2)
    animated_circle2.draw("""
    A VIOLET circle at (100, 100) with radius 20,
    and an ORANGE circle at (200, 200) with radius 50.
    Next the circles will flash through swelling/shrinking
    along with color and thickness changes.""")

    # Apply:
    #   -- swell_and_shrink_repeatedly() (so the colors change)
    #   -- change_color()
    #   -- swell_or_shrink_repeatedly() (so the colors change again)
    #   -- change_to_previous_color()
    # The latter should have changed the color back to
    # .
    print('\nAfter various color changes (but none via change_color):')

    animated_circle1.animation_factor = 0.1  # Faster animations
    animated_circle2.animation_factor = 0.1

    animated_circle1.swell_or_shrink_repeatedly(40, 16)
    animated_circle2.swell_or_shrink_repeatedly(-10, 12)
    animated_circle1.circle.fill_color = 'CHARTREUSE'
    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw("""
    A CHARTREUSE circle on the left
    and a BLACK circle on the right.
    The very next action will be a CHANGE_COLOR on the LEFT one.""")

    print('\nJust after the call to change_color:')

    animated_circle1.change_color(0)
    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw()
    animated_circle2.draw("""
    A DARK RED circle on the left
    and a BLACK circle on the right.
    Next, the circles will again flash through swelling/shrinking
    along with color and thickness changes.""")

    print('\nJust after various color changes:')

    animated_circle1.swell_or_shrink_repeatedly(80, 13)
    animated_circle2.swell_or_shrink_repeatedly(20, 11)
    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw()
    animated_circle2.draw("""
    A SEASHELL circle on the left
    and a FOREST GREEN circle on the right.
    The very next action will be a change_to_previous_color
    applied to the LEFT Animated_Circle.
    That should return the LEFT circle to CHARTREUSE.""")

    print('Just after animated_circle1.change_to_previous_color():')

    animated_circle2.draw(1)
    animated_circle1.change_to_previous_color()
    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw("""
    CHARTREUSE on the left, since that is what it was just BEFORE
    the most recent call to   change_color   on the LEFT.
    The RIGHT remains FOREST GREEN.
    Next will be a change_to_previous_color
    applied to the RIGHT Animated_Circle.
    That Animated_Circle has not yet had ANY calls to change_color
    so the RIGHT should become some arbitrary color
    (anything is OK, but the program should not crash).""")

    print('Just after animated_circle2.change_to_previous_color():')

    animated_circle1.draw(1)  # To force a pause

    animated_circle2.change_to_previous_color()
    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw("""
    The LEFT remains CHARTREUSE.
    The RIGHT should have changed to some arbitrary color
    (anything is OK, but the program should not crash).
    Next we do more color changes (but none via change_color).""")

    print('Just after more color changes (but none via change_color):')

    animated_circle1.swell_or_shrink_repeatedly(30, 11)
    animated_circle2.swell_or_shrink_repeatedly(50, 6)
    animated_circle1.circle.fill_color = 'AQUAMARINE'
    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw("""
    An AQUAMARINE circle on the left and a HOT PINK circle on the right.
    Next we call   change_color   on both Animated_Circles,
    then various color changes on both (but none via change_color).""")

    print('\nJust after calling   color_change   on both')
    print('Animated_Circles, along with various additional')
    print('color changes (but none via color_change):')

    animated_circle1.change_color(random.randrange(11))
    animated_circle2.change_color(random.randrange(11))

    animated_circle1.swell_or_shrink_repeatedly(10, 4)
    animated_circle2.swell_or_shrink_repeatedly(-10, 8)

    print(animated_circle1)
    print(animated_circle2)
    animated_circle1.draw()
    animated_circle2.draw("""
    A BROWN circle on the left and a BLUE circle on the right.
    Next, the calls to   change_to_previous_color.
    They should change the LEFT back to AQUAMARINE
    and the RIGHT back to HOT PINK.""")

    print('Just after   change_to_previous_color   on')
    print('both Animated_Circles:')

    animated_circle1.animation_factor = 1  # Slow animations for finish
    animated_circle2.animation_factor = 1

    animated_circle1.draw(1)  # To force a pause

    animated_circle1.change_to_previous_color()
    print(animated_circle1)
    animated_circle1.draw(1)

    animated_circle2.change_to_previous_color()
    print(animated_circle2)
    animated_circle2.draw("""
    The LEFT circle should now be AQUAMARINE.
    The RIGHT circle should now be HOT PINK.
    This concludes this test.""")


########################################################################
# Use this   is_prime   function when you implement   swell_to_prime.
########################################################################
def is_prime(n):
    """
    What comes in:   An integer.
    What goes out:  Returns True if the given integer is prime.
                    Returns False if the given integer is NOT prime.
    Side effects: None.
    Examples:
      This function returns True or False, depending on whether
      the given integer is prime or not.  Since the smallest prime is 2,
      this function returns False on all integers < 2.
      It returns True on 2, 3, 5, 7, and other primes.
    Note: The algorithm used here is simple and clear but slow.
    Type hints:
      :type n: int
    """
    if n < 2:
        return False

    for k in range(2, int(math.sqrt(n) + 0.1) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
