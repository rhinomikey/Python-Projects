"""
PRACTICE Test 2, practice_problem 3.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Gupta.  April 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import simple_testing as st
import math
import rosegraphics as rg
import builtins

########################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     4 is an "easy" Test 2 question.
#     6 is a "typical" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
########################################################################


def main():
    """ Calls the   TEST   functions in this module. """
#     test_practice_problem3a()
#     test_practice_problem3b()
#     test_practice_problem3c()
#     test_practice_problem3d()
#     test_practice_problem3e()
    test_practice_problem3f()


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
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
#           See details in the  test  code below.
# ----------------------------------------------------------------------


def test_practice_problem3a():
    """ Tests the    practice_problem3a    function. """
    # ------------------------------------------------------------------
    # 6 tests.
    # They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3a((rg.Circle(rg.Point(5, 10), 20),
    #                       rg.Circle(rg.Point(2, 20), 20),
    #                       rg.Circle(rg.Point(7, 30), 10),
    #                       rg.Circle(rg.Point(10, 40), 20),
    #                       rg.Circle(rg.Point(2, 50), 10)))
    # and compare the returned value against 1400 (the correct answer).
    # ------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3a,
                               [(rg.Circle(rg.Point(5, 10), 20),
                                 rg.Circle(rg.Point(2, 20), 20),
                                 rg.Circle(rg.Point(7, 30), 10),
                                 rg.Circle(rg.Point(10, 40), 20),
                                 rg.Circle(rg.Point(2, 50), 10))],
                               5 * 2 * 7 * 10 * 2),
             st.SimpleTestCase(practice_problem3a,
                               [(rg.Circle(rg.Point(58, 10), 20),)],
                               58),
             st.SimpleTestCase(practice_problem3a,
                               [(rg.Circle(rg.Point(84, 100), 200),
                                 rg.Circle(rg.Point(28, 200), 200),
                                 rg.Circle(rg.Point(10005, 300), 100))],
                               84 * 28 * 10005),
             st.SimpleTestCase(practice_problem3a,
                               [()],
                               1),
             st.SimpleTestCase(practice_problem3a,
                               [(rg.Circle(rg.Point(5, 10), 20),
                                 rg.Circle(rg.Point(0, 20), 20),
                                 rg.Circle(rg.Point(7, 30), 10),
                                 rg.Circle(rg.Point(10, 40), 20),
                                 rg.Circle(rg.Point(2, 50), 10))],
                               5 * 0 * 7 * 10 * 2),
             ]

    circles = []
    for k in range(1, 101):
        circles.append(rg.Circle(rg.Point(k, k + 20), 5 * k))
    answer = math.factorial(100)
    tests.append(st.SimpleTestCase(practice_problem3a,
                                   [circles],
                                   answer))

    # ------------------------------------------------------------------
    # Run the 6 tests in the   tests   list constructed above.
    # ------------------------------------------------------------------
    st.SimpleTestCase.run_tests('practice_problem3a', tests)


def practice_problem3a(circles):
    """
    What comes in:  A sequence of rg.Circles.
    What goes out:  Returns the product of the x-coordinates
      of the centers of the rg.Circles.
      Returns 1 if the given sequence is empty.
    Side effects: None.
    Examples:
      If the sequence is a list containing these 5 rg.Circles:
        rg.Circle(rg.Point(5, 10), 20)
        rg.Circle(rg.Point(2, 20), 20)
        rg.Circle(rg.Point(7, 30), 10)
        rg.Circle(rg.Point(10, 40), 20)
        rg.Circle(rg.Point(2, 50), 10)
      then this function returns:
        5 x 2 x 7 x 10 x 2, which is 1400.
    Type hints:
      :type sequence: [rg.Circle]
    """
    ####################################################################
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    ####################################################################
    
    tot = 1
    
    for i in range(len(circles)):
        tot = tot * circles[i].center.x
    return tot


def test_practice_problem3b():
    """ Tests the    practice_problem3b    function. """
    # ------------------------------------------------------------------
    # 13 tests.  They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3b([12, 33, 18, 'hello', 9, 13, 3, 9])
    # and compare the returned value against True (the correct answer).
    # ------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3b,
                               [[12, 33, 18, 'hello', 9, 13, 3, 9]],
                               True),
             st.SimpleTestCase(practice_problem3b,
                               [[12, 12, 33, 'hello', 5, 33, 5, 9]],
                               False),
             st.SimpleTestCase(practice_problem3b,
                               [(77, 112, 33, 'hello', 0, 43, 5, 77)],
                               True),
             st.SimpleTestCase(practice_problem3b,
                               [[1, 1, 1, 1, 1, 1, 2]],
                               False),
             st.SimpleTestCase(practice_problem3b,
                               [['aa', 'a']],
                               False),
             st.SimpleTestCase(practice_problem3b,
                               ['aaa'],
                               True),
             st.SimpleTestCase(practice_problem3b,
                               [['aa', 'a', 'b', 'a', 'b', 'a']],
                               True),
             st.SimpleTestCase(practice_problem3b,
                               [[9]],
                               False),
             st.SimpleTestCase(practice_problem3b,
                               [(12, 33, 8, 'hello', 99, 'hello')],
                               True),
             st.SimpleTestCase(practice_problem3b,
                               [['hello there', 'he', 'lo', 'hello']],
                               False),
             st.SimpleTestCase(practice_problem3b,
                               [((8,), '8', (4 + 4, 4 + 4), [8, 8], 7, 8)],
                               False),
             st.SimpleTestCase(practice_problem3b,
                               [[(8,), '8', [4 + 4, 4 + 4],
                                 (8, 8), 7, [8, 8]]],
                               True),
             st.SimpleTestCase(practice_problem3b,
                               [[(8,), '8', [4 + 4, 4 + 4],
                                 [8, 8], 7, (8, 8)]],
                               False),
             ]

    # Run the 13 tests in the   tests   list constructed above.
    st.SimpleTestCase.run_tests('practice_problem3b', tests)


def practice_problem3b(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns True if the last item of the sequence
      appears again somewhere else in the sequence.  Returns False
      if the last item of the sequence does NOT appear somewhere
      else in the sequence.
    Side effects: None.
    Examples:
      If the sequence is [12, 33, 18, 'hello', 9, 13, 3, 9],
      this function returns True because the last item (9)
      DOES appear elsewhere in the sequence (namely, at index 4).

      If the sequence is [12, 12, 33, 'hello', 5, 33, 5, 9],
      this function returns False because the last item (9)
      does NOT appear elsewhere in the sequence

      If the sequence is (77, 112, 33, 'hello', 0, 43, 5, 77),
      this function returns True.

      If the sequence is [9], this function returns False.

      If the sequence is [12, 33, 8, 'hello', 99, 'hello'],
      this function returns True since the last item ('hello')
      DOES appear elsewhere in the sequence (namely, at index 3).

      If the sequence is ['hello there', 'he', 'lo', 'hello'],
      this function returns False.

      If the sequence is 'hello there',
      this function returns True since the last item ('e') DOES
      appear elsewhere in the sequence (namely, at indices 1 and 8).

    Type hints:
      :type: sequence: list    or tuple or string
    """
    ####################################################################
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    #
    # IMPLEMENTATION REQUIREMENT:  You are NOT allowed to use the
    #    'count' or 'index' methods for sequences in this problem
    #    (because here we want you to demonstrate your ability
    #    to use explicit looping here).
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      6
    #    TIME ESTIMATE:   10 minutes.
    ####################################################################
    
    last_value=sequence[len(sequence)-1]
    for i in range(len(sequence)-1):
        if last_value==sequence[i]:
            return True
    return False


def test_practice_problem3c():
    """ Tests the    practice_problem3c    function. """
    # ------------------------------------------------------------------
    # 4 tests.  They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3v((9, 33, 8, 8, 0, 4, 4, 8))
    # and compare the returned value against [2, 5] (the correct answer).
    # ------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3c,
                               [(9, 33, 8, 8, 0, 4, 4, 8)],
                               [2, 5]),
             st.SimpleTestCase(practice_problem3c,
                               [(9, 9, 9, 9, 0, 9, 9, 9)],
                               [0, 1, 2, 5, 6]),
             st.SimpleTestCase(practice_problem3c,
                               [(4, 5, 4, 5, 4, 5, 4)],
                               []),
             st.SimpleTestCase(practice_problem3c,
                               ['abbabbb'],
                               [1, 4, 5]),
             ]

    # Run the 4 tests in the   tests   list constructed above.
    st.SimpleTestCase.run_tests('practice_problem3c', tests)


def practice_problem3c(sequence):
    """
    What comes in: A non-empty sequence.
    What goes out: Returns a list of integers,
      where the integers are the places (indices)
      where an item in the given sequence appears twice in a row.
    Side effects: None.
    Examples:
      Given sequence (9, 33, 8, 8, 0, 4, 4, 8)
         -- this function returns [2, 5]
              since 8 appears twice in a row starting at index 2
              and 4 appears twice in a row starting at index 5

      Given sequence (9, 9, 9, 9, 0, 9, 9, 9)
         -- this function returns [0, 1, 2, 5, 6]

      Given sequence (4, 5, 4, 5, 4, 5, 4)
         -- this function returns []

      Given sequence 'abbabbb'
         -- this function returns [1, 4, 5]

    Type hints:
      :type: sequence: list    or tuple or string
    """
    ####################################################################
    # DONE: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      8
    #    TIME ESTIMATE:   15 minutes.
    ####################################################################
    seq=[]
    length = len(sequence)
    for i in range(length):
        if i == length -1:
            break
        elif sequence[i]==sequence[i+1]:
            seq.append(i)
    return seq

def test_practice_problem3d():
    """ Tests the    practice_problem3d    function. """
    # ------------------------------------------------------------------
    # 5 tests.  They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3d((12, 33, 18, 9, 13, 3, 9, 20, 19, 20))
    # and compare the returned value against 22 (the correct answer).
    # ------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3d,
                               [(12, 33, 18, 9, 13, 3, 9, 20, 19, 20)],
                               19),
             st.SimpleTestCase(practice_problem3d,
                               [(3, 12, 10, 8, 8, 9, 8, 11)],
                               10),
             st.SimpleTestCase(practice_problem3d,
                               [(-9999999999, 8888888888)],
                               - 9999999999 + 8888888888),
             st.SimpleTestCase(practice_problem3d,
                               [(8888888888, -9999999999)],
                               8888888888),
             st.SimpleTestCase(practice_problem3d,
                               [(-77, 20000, -33, 40000, -55,
                                 60000, -11)],
                               - 11),
             ]

    # ------------------------------------------------------------------
    # Run the 5 tests in the   tests   list constructed above.
    # ------------------------------------------------------------------
    st.SimpleTestCase.run_tests('practice_problem3d', tests)


def practice_problem3d(sequence):
    """
    What comes in:
      A sequence of numbers, where the length of the sequence >= 2.
    What goes out:
      Returns the largest of the numbers at EVEN INDICES of the sequence.
    Side effects: None.
    Examples:
      If the sequence is:
          (12, 33, 18, 9, 13, 3, 99, 20, 19, 20)
      then the largest of the numbers at EVEN indices is the largest of
           12      18     13     99      19        which is 99.
      So the function returns 99 in this example.

    Type hints:
      :type sequence: list(float)    or tuple(float)
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      7
    #    TIME ESTIMATE:   10 minutes.
    ####################################################################
    
    seq = []
    num = 0
    for i in range(len(sequence)):
        if i % 2 == 0:
            seq.append(sequence[i])
    return max(seq)

def test_practice_problem3e():
    """ Tests the    practice_problem3e    function. """
    # ------------------------------------------------------------------
    # 3 tests.  They use the imported   simple_testing (st)   module.
    # ------------------------------------------------------------------
    argument1 = (rg.Point(5, 12),
                 rg.Point(20, 20),
                 rg.Point(1, 13),
                 rg.Point(10, 40),
                 rg.Point(13, 5),
                 rg.Point(10, 3),
                 rg.Point(3, 7),
                 rg.Point(2, 2))
    answer1 = rg.Point(5, 13)

    argument2 = (rg.Point(5, 12),
                 rg.Point(20, 20),
                 rg.Point(27, 13),
                 rg.Point(10, 40),
                 rg.Point(13, 4),
                 rg.Point(1, 1),
                 rg.Point(3, 7))
    answer2 = rg.Point(7, 3)

    argument3 = (rg.Point(5, 2),
                 rg.Point(20, 20),
                 rg.Point(27, 13),
                 rg.Point(10, 40),
                 rg.Point(13, 4),
                 rg.Point(1, 1),
                 rg.Point(3, 7))
    answer3 = rg.Point(2, 5)

    argument4 = (rg.Point(5, 12),
                 rg.Point(20, 20),
                 rg.Point(27, 13))
    answer4 = 'Not found'

    tests = [st.SimpleTestCase(practice_problem3e, [argument1], answer1),
             st.SimpleTestCase(practice_problem3e, [argument2], answer2),
             st.SimpleTestCase(practice_problem3e, [argument3], answer3),
             st.SimpleTestCase(practice_problem3e, [argument4], answer4),
             ]
    # ------------------------------------------------------------------
    # Run the 3 tests in the   tests   list constructed above.
    # ------------------------------------------------------------------
    st.SimpleTestCase.run_tests('practice_problem3e', tests)

    if argument1[4] != answer1:
        print()
        print('*** WARNING, WARNING, WARNING ***')
        print('If your code DID pass the above tests')
        print('but you get this message,')
        print('then you have missed an important concept about mutation.')
        print('  *** SEE YOUR INSTRUCTOR for an important explanation!')
        print()


def practice_problem3e(points):
    """
    What comes in:  A tuple of rg.Points, each of whose coordinates
      is an integer.
    What goes out:
      AFTER doing the side effect below, this function
      returns the rg.Point to which it did the side effect.
      If there is no point to which to do the side effect,
      returns 'Not found'.
    Side effects:
      Swaps the x and y coordinates of the first (leftmost) rg.Point
      in the given list whose x and y coordinates are both primes.
      Has no side effect if there are no such rg.Points
      in the given list. For purposes of this problem, any integer
      less than 2 is NOT a prime.
    Examples:
      If the given tuple is: (rg.Point(5, 12),
                              rg.Point(20, 20),
                              rg.Point(1, 13),
                              rg.Point(10, 40),
                              rg.Point(13, 5),
                              rg.Point(10, 3),
                              rg.Point(3, 7),
                              rg.Point(2, 2))
      then after this function the rg.Point in the given tuple
      whose x and y were (13, 5) will have x and y (5, 13)
      and the function returns that rg.Point.
    Type hints:
      :type sequence: [rg.Point]
    """
    ####################################################################
    # DONE: 6. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      10
    #    TIME ESTIMATE:   10 minutes.
    ####################################################################
    
    for i in range(len(points)):
        if is_prime(points[i].x) and is_prime(points[i].y) == True:
            x = points[i].x
            points[i].x = points[i].y
            points[i].y = x
            return points[i]
    return 'Not found'


def test_practice_problem3f():
    """ Tests the    practice_problem3f    function. """
    # ------------------------------------------------------------------
    # 5 tests.  They use the imported   simple_testing (st)   module.
    # Each test is a SimpleTestCase with 3 arguments:
    #   -- the function to test,
    #   -- a list containing the argument(s) to send to the function,
    #   -- the correct returned value.
    # For example, the first test below will call
    #   practice_problem3f((6, 80, 17, 13, 40, 3, 3, 7, 13, 7, 12, 5))
    # and compare the returned value against 40 (the correct answer).
    # ------------------------------------------------------------------
    tests = [st.SimpleTestCase(practice_problem3f,
                               [(6, 80, 17, 13, 40, 3, 3, 7, 13, 7, 12, 5)],
                               17 + 3 + 7 + 13),
             st.SimpleTestCase(practice_problem3f,
                               [(7, 7, 7, 7, 7, 4, 4, 8, 5, 5, 6)],
                               0),
             st.SimpleTestCase(practice_problem3f,
                               [(2, 3, 5, 7, 5, 3, 2)],
                               2 + 3 + 5 + 7 + 5 + 3),
             st.SimpleTestCase(practice_problem3f,
                               [(11, 3, 17, 13, 40, 3, 3, 7, 13, 7, 12, 5)],
                               11 + 3 + 17 + 3 + 7 + 13),
             st.SimpleTestCase(practice_problem3f,
                               [(6, 80, 17, 13, 40, 3, 3, 7, 13, 7, 11, 5)],
                               17 + 3 + 7 + 13 + 7 + 11),
             ]

    # Run the 5 tests in the   tests   list constructed above.
    st.SimpleTestCase.run_tests('practice_problem3f', tests)


def practice_problem3f(sequence):
    """
    What comes in: A non-empty sequence of integers.
    What goes out: An integer that is the sum of all the items
      in the given sequence such that:
        -- the item is a prime number, AND
        -- the immediate successor of the item
             is a DIFFERENT prime number.
    Side effects: None.
    Examples:
      Given sequence (6, 80, 17, 13, 40, 3, 3, 7, 13, 7, 12, 5)
         -- this function returns  17 + 3 + 7 + 13,  which is 40,
            because:
            6 (at index 0) is NOT prime - do NOT include 6 in the sum
            80 (at index 1) is NOT prime - do NOT include 80 in the sum

            17 (at index 2) IS prime AND the next item (13, at index 3)
              is a DIFFERENT prime - ** DO ** include 17 in the sum

            13 (at index 3) IS prime but the next item (40, at index 4)
              is NOT prime - do NOT include 13 in the sum
            40 (at index 4) is NOT prime - do NOT include 40 in the sum
            3 (at index 5) IS prime AND the next item (3, at index 6)
              IS prime but is NOT a DIFFERENT prime -
              do NOT include 3 in the sum

            3 (at index 6) IS prime AND the next item (7, at index 7)
              is a DIFFERENT prime - ** DO ** include 3 in the sum
            7 (at index 7) IS prime AND the next item (13, at index 8)
              is a DIFFERENT prime - ** DO ** include 7 in the sum
            13 (at index 8) IS prime AND the next item (7, at index 9)
              is a DIFFERENT prime - ** DO ** include 13 in the sum

            7 (at index 9) IS prime but the next item (12, at index 10)
              is NOT prime - do NOT include 7 in the sum
            12 (at index 10) is NOT prime - do NOT include 12 in the sum
            5 (at index 11) IS prime but there is NO item after it
               - do NOT include 5 in the sum

      Given sequence (7, 7, 7, 7, 7, 4, 4, 8, 5, 5, 6)
         -- this function returns 0

      Given sequence (2, 3, 5, 7, 5, 3, 2)
         -- this function returns 2 + 3 + 5 + 7 + 5 + 3, which is 25

    Type hints:
      :type: sequence: list(int)     or tuple(int)
    """
    ####################################################################
    # DONE: 7. Implement and test this function.
    #     The testing code is already written for you (above).
    ####################################################################
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      8
    #    TIME ESTIMATE:   15 minutes.
    ####################################################################
    
    tot = 0
    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i+1]:
            if is_prime(sequence[i]) == True and is_prime(sequence[i+1]) == True:
                tot = tot + sequence[i]
    return tot

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
