"""
This module demonstrates the WAIT-FOR-EVENT pattern implemented
by using a WHILE loop using the ITCH pattern:

   Initialize as needed so that the CONDITION can be TESTED.
   while <some CONDITION>: # Test the CONDITION, continue WHILE it is true.
       ...
       ...
       CHange something that (eventually) affects the CONDITION.
         (else otherwise you will be in an infinite loop)

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_wait_for_prime()
    test_wait_for_sum_of_cubes()


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:  True if the given integer is prime, else False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
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


def test_wait_for_prime():
    """ Tests the   wait_for_prime    function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  wait_for_prime  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond what we supplied.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_prime   function:')
    print('--------------------------------------------------')

    # Test 1:
    print('TEST STARTED!  Has it ended?')
    expected = 7
    actual = wait_for_prime(7)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 2:
    print('TEST STARTED!  Has it ended?')
    expected = 11
    actual = wait_for_prime(8)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 3:
    print('TEST STARTED!  Has it ended?')
    expected = 83
    actual = wait_for_prime(80)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 4:
    print('TEST STARTED!  Has it ended?')
    expected = 155921 + 86
    actual = wait_for_prime(155922)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 5:
    print('TEST STARTED!  Has it ended?')
    expected = 2
    actual = wait_for_prime(2)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 6:  PUT YOUR TEST(S) ** IN BETWEEN ** THESE LINES:
    print('TEST STARTED!  Has it ended?')
    expected = 23
    actual = wait_for_prime(20)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')


def wait_for_prime(m):
    """
    What comes in:  An integer   m   that is at least 2.
    What goes out:  The first integer >= m that is prime.
    Side effects:   None.
    Examples:
      -- wait_for_prime(7)  returns  7
      -- wait_for_prime(8)  returns  11
      -- wait_for_prime(80)  returns  83
      -- wait_for_prime(155921)  returns  156007  [trust me!]
    Type hints:
      :type m: int
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #    -- Use (call) the   is_prime   function above appropriately.
    # ------------------------------------------------------------------
    
    for i in range(m,200000):
        if is_prime(i) == True:
            return i
            

def test_wait_for_sum_of_cubes():
    """ Tests the   wait_for_sum_of_cubes    function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  wait_for_sum_of_cubes  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond what we supplied.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_sum_of_cubes   function:')
    print('--------------------------------------------------')

    # Test 1:
    print('TEST STARTED!  Has it ended?')
    expected = 2
    actual = wait_for_sum_of_cubes(4.3)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 2:
    print('TEST STARTED!  Has it ended?')
    expected = 4
    actual = wait_for_sum_of_cubes(58)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 3:
    print('TEST STARTED!  Has it ended?')
    expected = 8
    actual = wait_for_sum_of_cubes(1000)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 4:
    print('TEST STARTED!  Has it ended?')
    expected = 8
    actual = wait_for_sum_of_cubes(1296)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 5:
    print('TEST STARTED!  Has it ended?')
    expected = 9
    actual = wait_for_sum_of_cubes(1296.000001)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 6:
    print('TEST STARTED!  Has it ended?')
    expected = 1
    actual = wait_for_sum_of_cubes(-5.2)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')

    # Test 6:  PUT YOUR TEST(S) ** IN BETWEEN ** THESE LINES:
    #          Use   wait_for_sum_of_cubes(30.33)   as one of your tests
    print('TEST STARTED!  Has it ended?')
    expected = 6
    actual = wait_for_sum_of_cubes(345)
    print('Expected:', expected)
    print('Actual:  ', actual)
    print('TEST ENDED!')


def wait_for_sum_of_cubes(x):
    """
    What comes in:  A number x.
    What goes out:  Returns the smallest positive integer n
      such that the sum
           1 cubed  +  2 cubed  +  3 cubed  +  ...  + n cubed
      is greater than or equal to x.
    Side effects:   None.
    Examples:
      -- If x is 4.3, this function returns   2   because:
            1 cubed = 1 which is less than 4.3
         but
            1 cubed + 2 cubed = 9 which is greater than or equal to 4.3
      -- For similar reasons, if x is any number in the range (1, 9]
         (that is, numbers greater than 1 but less than or equal to 9),
         this function returns 2.
      -- If x is 58, this function returns   4   because:
            1 cubed + 2 cubed + 3 cubed = 36   which is less than 58
         but
            1 cubed + 2 cubed + 3 cubed + 4 cubed = 100
              which is greater than or equal to 58
      -- For similar reasons, if x is any number in the range (36, 100],
         this function returns 4.
      -- If x is 1000, this function returns 8 because:
              1 + 8 + 27 + 64 + ... + (7**3) = 784
            but
              1 + 8 + 27 + 64 + ... + (8**3) = 1296
      -- For similar reasons, f x is 1296, this function returns 8.
      -- if x is -5.2 (or any number less than or equal to 1),
           this function returns 1.
    Type hints:
      :type x: float  [or an int]
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPLEMENTATION REQUIREMENT:
    #   -- Solve this using the   wait-until-event   pattern.
    #
    # Note for the mathematically inclined:  One could figure out
    # (or look up) a formula that would allow a faster computation.
    # But no fair using that in this function.
    # ------------------------------------------------------------------
    num = 0
    if x < 1:
        return 1
    for i in range(2000):
        num = num + i**3
        if num + (i+1)**3 >= x and num <= x:
            return i+1


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
