"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  September 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_powers()
    test_sum_powers_in_range()


def test_sum_powers():
    """ Tests the   sum_powers   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_powers  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers   function:')
    print('--------------------------------------------------')

    expected = 22.46827
    answer = sum_powers(10, .5)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 6.003412
    answer = sum_powers(9, -.3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 12.12853
    answer = sum_powers(8, .3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 313.3774
    answer = sum_powers(1000, -.2)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)


def sum_powers(n, p):
    """
    What comes in:  A non-negative integer n
                    and a number p.
    What goes out:  The sum   1**p + 2**p + 3**p + ... + n**p
       for the given numbers n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:   None.
    Examples:
      -- sum_powers(5, -0.3) returns about 3.80826
      -- sum_powers(100, 0.1) returns about 144.45655
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** p
    return sum


def test_sum_powers_in_range():
    """ Tests the   sum_powers_in_range   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_powers_in_range  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_powers_in_range   function:')
    print('--------------------------------------------------')

    expected = 120.5579
    answer = sum_powers_in_range(5, 50, .3)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 2914.628
    answer = sum_powers_in_range(9, 900, .2)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 5185.949
    answer = sum_powers_in_range(65, 225, .7)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 264261.1
    answer = sum_powers_in_range(95, 9500, .4)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)


def sum_powers_in_range(m, n, p):
    """
    What comes in:  Non-negative integers m and n, with n >= m,
                    and a number p.
    What goes out:  the sum
           m**p + (m+1)**p + (m+2)**p + ... + n**p
       for the given numbers m, n and p.  The latter may be any number
       (possibly a floating point number, and possibly negative).
    Side effects:  None.
    Example:
      -- sum_powers_in_range(3, 100, 0.1) returns about 142.384776
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    #   No fair running the code of  sum_powers_in_range  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    #
    # COMMENT: Do you see how you could use   sum_powers_in_range
    #    to test  sum_powers   and (to a lesser extent) vice-versa?
    # ------------------------------------------------------------------

    sum = 0
    for i in range(m, n + 1):
        sum = sum + i ** p
    return sum


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
