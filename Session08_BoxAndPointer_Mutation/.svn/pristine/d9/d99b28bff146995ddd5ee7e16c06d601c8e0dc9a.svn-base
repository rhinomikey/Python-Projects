"""
This module demonstrates   MUTATION   of an OBJECT in two ways:
  -- From an assignment in main.
  -- From within a function call.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         and their colleagues.  December 2015.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program in the debugger to watch
#           assignment and mutation in action.  This is a contrived
#           example that we are using only to show the elements
#           of mutation with simple code.
# ----------------------------------------------------------------------

import rosegraphics as rg


def main():
    # ------------------------------------------------------------------
    # 1. Constructs a zg.Point, assigning its instance variables values.
    #    Then assigns an instance variable in the object a new value,
    #      thus MUTATING the OBJECT, because
    #      one of its INSTANCE VARIABLES was ASSIGNED a new value.
    # ------------------------------------------------------------------
    print('Showing mutation via assignment:')
    point = rg.Point(45, 100)
    point.y = 33
    print(point)  # To see that the INSIDES of   point   has changed

    # ------------------------------------------------------------------
    # 2. Mutates the object again, this time from within a function call
    # ------------------------------------------------------------------
    print()
    print('Showing mutation via a function call')
    print('(which does assignment):')

    mutate_point(point)
    print(point)  # To see that the INSIDES of   point   has changed

    # ------------------------------------------------------------------
    # 3. Assigns another variable to refer to the same zg.Point
    #       to which the    point   variable refers.
    #    That creates two NAMES (variables)
    #       that refer to the same OBJECT.
    #    When one mutates, so does the other.
    # ------------------------------------------------------------------
    print()
    print('Showing two NAMES that refer to the same OBJECT:')
    point2 = point
    print(point, point2)

    point2.x = 100
    print(point, point2)  # Note that  point.x  ALSO changed

    # ------------------------------------------------------------------
    # 4. Re-assigns the   point   variable to refer to another zg.Point.
    #      This is ASSIGNMENT and NOT mutation.
    # ------------------------------------------------------------------
    print()
    print('RE-ASSIGNING an object is  NOT  MUTATING the OBJECT:')
    point = rg.Point(10, 6)

    print(point, point2)  # Prints the two DIFFERENT zg.Points

    # ------------------------------------------------------------------
    # 5. Shows the difference betwee the   is   operator
    #      (two things refer to the same place in memory)
    #    and the   ==   operator (two things contain the same data).
    # ------------------------------------------------------------------
    print()
    print('Shows the difference between two operators')
    print('  -- a IS b  (do a and b refer to the same place in memory?')
    print('  -- a == b  (do a and b have the same data?)')
    print('Predict what will get printed by the following, if you can.')
    print('First, two Points are constructed.  See IS vs == in action:')
    point3 = rg.Point(100, 20)
    point4 = rg.Point(100, 20)

    print(point3 is point4)
    print(point3 == point4)

    point3.fill_color = 'blue'
    print(point3 is point4)
    print(point3 == point4)
    print(point3.fill_color, point4.fill_color)

    print()
    print('Second, another Point is assigned to one of the existing ones.')
    print('  Here is the IS operator:')
    point5 = point3

    print(point3 is point5)
    print(point3 is point4)
    print(point4 is point5)

    print('  Now the == operator:')
    print(point3 == point5)
    print(point3 == point4)
    print(point4 == point5)
    print(point3.fill_color, point4.fill_color, point5.fill_color)

    print()
    print('Finally, a tricky one that your instruction will explain:')
    x = 'hello'
    y = 'hello'
    print(x is y)
    print(x == y)

    x = 1 * x
    y = 1 * y
    print(x is y)
    print(x == y)

    x = 2 * x
    y = 2 * y
    print(x is y)
    print(x == y)


def mutate_point(point):
    """ Silly example, just to show mutation at work. """
    point.y = 77

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
