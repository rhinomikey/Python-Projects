"""
Test 3, problem 2.

Authors: David Mutchler, Dave Fisher, their colleagues
              and Nathan Gupta.  May 2016.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_shape()


def test_shape():
    """ Tests the    shape    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   SHAPE   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1 of shape: r=7')
    shape(7)

    print()
    print('Test 2 of shape: r=4')
    shape(4)

    print()
    print('Test 3 of shape: r=2')
    shape(2)


def shape(r):
    """
    Prints a Z shape with r rows that looks like this example where r=7:
    1234567
         6
        5
       4
      3
     2
    1234567

    Another example, where r=4:
    1234
      3
     2
    1234

    One more example, where r=2:
    12
    12

    Preconditions:  r is an integer that is at least 2.
    For purposes of "lining up", assume r is a single digit.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   You may NOT use string multiplication in this problem.
    #
    # HINT:
    #   If you're having trouble with the spacing, print Xs for
    #    the spaces until you figure out where the problem is
    #    (and then change the Xs back to spaces).
    # ------------------------------------------------------------------
    numlist1 = ''
    for i in range(r-1):
        for k in range(r):
            numlist1 = numlist1 + str(k+1)
        print(numlist1)
        print(' '*(r-2-i),(r-1-i))
            


# ----------------------------------------------------------------------
# Calls main to start the ball rolling.
#   More precisely, calls main only if this module is running at the
#   top level (as opposed to being imported by another module).
#   This structure helps us automate tests of this module.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
