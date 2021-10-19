"""
PRACTICE Test 3.

This problem provides practice at:
  ***  MUTATING  and  RETURNING-NEW  LISTS.  ***

These problems have DIFFICULTY and TIME ratings:
  DIFFICULTY rating:  1 to 10, where:
     1 is very easy
     4 is an "easy" Test 3 question.
     6 is a "typical" Test 3 question.
    10 is an EXTREMELY hard problem (too hard for a Test 3 question)

  TIME ratings: A ROUGH estimate of the number of minutes that we
     would expect a well-prepared student to take on the problem.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  February 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_doubler()


def test_doubler():
    """ Tests the    doubler    function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  doubler  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    #
    #   Try to choose tests that might expose errors in your code!
    #
    #   As usual, include both EXPECTED and ACTUAL results in your tests
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # ------------------------------------------------------------------

    print()
    print('--------------------------------------------------')
    print('Testing the   doubler   function:')
    print('--------------------------------------------------')

    # Test 1:
    arg1 = [10, -3, 20, 4]
    arg2 = [5, 0, 8]
    correct_arg1_after = [20, -6, 40, 8]
    correct_arg2_after = [10, 0, 16]

    print()
    print('BEFORE the function call:')
    print('  Argument 1 is:', arg1)
    print('  Argument 2 is:', arg2)

    answer = doubler(arg1, arg2)

    print('AFTER the function call:')
    print('  Argument 1 is:       ', arg1)
    print('  Argument 1 should be:', correct_arg1_after)
    print('  Argument 2 is:       ', arg2)
    print('  Argument 2 should be:', correct_arg2_after)
    print()

    # ------------------------------------------------------------------
    # DONE 2 (continued): Add your ADDITIONAL test(s) here:
    # ------------------------------------------------------------------
    
    list1 = [1,4,2,5,3,6]
    list2 = [2,4,3,6,4,8]
    correct_list1 = [2,8,4,10,6,12]
    correct_list2 = [4,8,6,12,8,16]
    answer = doubler(list1,list2)
    print('  Argument 1 is:       ', list1)
    print('  Argument 1 should be:', correct_list1)
    print('  Argument 2 is:       ', list2)
    print('  Argument 2 should be:', correct_list2)


def doubler(list1, list2):
    """
    Both arguments are lists of integers.  This function:
      -- MUTATEs the first list by doubling each number in the list
    and
      -- RETURNs a new list that is the same as list2 but with each
           number in the list doubled.

    For example, if the two arguments are:
       [10, -3, 20, 4]  and  [5, 0, 8]
    then this method MUTATEs the first argument to [20, -6, 40, 8]
    and RETURNs the list [10, 0, 16]

    Preconditions:
        :type list1: list   of integers
        :type list2: list   of integers
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      4
    #    TIME ESTIMATE:   5 minutes.
    # ------------------------------------------------------------------
    list_list = []
    for i in range(len(list1)):
        if i == len(list1):
            break
        list1[i] = list1[i]*2

    for i in range(len(list2)):
        if i == len(list2):
            break
        list2[i] = list2[i]*2
    return list1,list2

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
