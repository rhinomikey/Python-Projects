"""
This module lets you practice two forms of the ACCUMULATOR pattern:
  -- SUMMING
  -- COUNTING
where the accumulation is done via ITERATING (i.e., looping)
through a SEQUENCE.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import random
import builtins  # Never necessary, but here to make a point about SUM
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_sequence()
    test_count_items_bigger_than()
    test_count_positive_sines()
    test_sum_first_n()


def test_sum_sequence():
    """ Tests the   sum_sequence   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_sequence   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # Here (below) are examples of using an ORACLE for testing,
    # that is, using a separate way of gaining the correct tests as if
    # by "magic". The oracle here is the built-in    sum    function.
    # We provided two test that use that oracle.
    #
    # BTW, google for  "Oracle of Delphi" if you are curious about
    # why we call such tests "oracles".
    # ------------------------------------------------------------------

    # Test 1:
    sequence1 = [48, -10, 100, 9939309808, 433443080, -45634930]

    oracle_answer = builtins.sum(sequence1)
    actual_answer = sum_sequence(sequence1)

    print()
    print('Testing:  sum_sequence  with argument:')
    print('   ', sequence1)
    print('  Expected (oracle) result: ', oracle_answer)
    print('  Actual result:            ', actual_answer)

    # Test 2:
    sequence2 = [48, 180, -475, 205, 88]

    oracle_answer = builtins.sum(sequence2)
    actual_answer = sum_sequence(sequence2)

    print()
    print('Testing:  sum_sequence  with argument:')
    print('   ', sequence2)
    print('  Expected (oracle) result: ', oracle_answer)
    print('  Actual result:            ', actual_answer)

    # Test 3:  This test uses a RANDOMLY generated sequence.
    sequence3 = []
    for _ in range(10000):
        sequence3.append(random.randrange(-10, 11))

    oracle_answer = builtins.sum(sequence3)
    actual_answer = sum_sequence(sequence3)

    print()
    print('Testing:  sum_sequence  with argument:')
    print('   ', sequence3)
    print('  Expected (oracle) result: ', oracle_answer)
    print('  Actual result:            ', actual_answer)

    # ------------------------------------------------------------------
    # These examples use a KNOWN answer
    # (here, ones easily computed by hand).
    # ------------------------------------------------------------------
    # Test 4:
    sequence4 = [48, -10]

    known_answer = 38
    actual_answer = sum_sequence(sequence4)

    print()
    print('Testing:  sum_sequence  with argument:')
    print('   ', sequence4)
    print('  Expected (known) result: ', known_answer)
    print('  Actual result:           ', actual_answer)

    # Test 5:
    sequence5 = []

    known_answer = 0
    actual_answer = sum_sequence(sequence5)

    print()
    print('Testing:  sum_sequence  with argument:')
    print('   ', sequence5)
    print('  Expected (known) result: ', known_answer)
    print('  Actual result:           ', actual_answer)


def sum_sequence(sequence):
    """
    What comes in:  An sequence of integers.
    What goes out: Returns the sum of the numbers in the given sequence.
    Side effects: None.
    Examples:
      sum_sequence([8, 13, 7, -5])  returns  23
      sum_sequence([48, -10])       returns  38
      sum_sequence([])              returns  0
    Type hints:
      :type sequence: [int]
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # RESTRICTION:
    #    You may NOT use the built-in  sum   function
    #    in IMPLEMENTING this function.
    #      -- The TESTING code above does use   built_ins.sum
    #         as an ORACLE in TESTING this function, however.
    # ------------------------------------------------------------------
    
    tot = 0
    for i in range(len(sequence)):
        tot = tot + sequence[i]
    return tot


def test_count_items_bigger_than():
    """ Tests the   count_items_bigger_than   function. """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this TEST function.
    #   It TESTS the  count_items_bigger_than  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond what we supplied.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_items_bigger_than   function:')
    print('--------------------------------------------------')

    # Test 1:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = 45
    expected = 2
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = 0
    expected = 5
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 3:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = -10
    expected = 5
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 4:
    sequence = [45, 84, 32, 70, -10, 40]
    threshold = -10.000000001
    expected = 6
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 5:
    sequence = []
    threshold = -99999999999999999999999999999
    expected = 0
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 6:  This test uses a RANDOMLY generated sequence
    #          but a KNOWN answer (none in the sequence are > threshold)
    sequence = []
    for _ in range(100000):
        sequence.append(random.randrange(-100, 100))
    threshold = 99.000000001
    expected = 0
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 7:  This test uses a RANDOMLY generated sequence
    #          but a KNOWN answer (all in the sequence are > threshold).
    sequence = []
    for _ in range(100000):
        sequence.append(random.randrange(-100, 100))
    threshold = -100.00000001
    expected = 100000
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 8:  This test uses a RANDOMLY generated sequence
    #          and an APPROXIMATE answer that is PROBABLY about right,
    #          based on the Law of Large Numbers.
    sequence = []
    n = 100000
    for _ in range(n):
        sequence.append(random.randrange(-100, 100))
    threshold = 98
    expected = n / 200
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected, 'APPROXIMATELY')
    print('Actual:  ', actual)
    standard_deviation = math.sqrt((n / 200) * (199 / 200))
    message = 'The actual should be within {:.0f} of the expected'
    print(message.format(1.96 * standard_deviation))
    print('about 95 percent of the time.')

    # Add your ADDITIONAL test(s) here:
    
    sequence = [10, 90, 100, 70, -40, 60]
    threshold = 90
    expected = 1
    actual = count_items_bigger_than(sequence, threshold)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)


def count_items_bigger_than(numbers, threshold):
    """
    What comes in:
      -- An sequence of numbers.
      -- A number that is a 'threshold'.
    What goes out:
      Returns the number of items in the given sequence of numbers
      that are strictly bigger than the given 'threshold' number.
    Side effects: None.
    Examples:
      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is 45,
      then this function returns 2 (since 84 and 70 are bigger than 45).

      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is 0,
      then this function returns 5
      (since all of the 6 numbers except -10 are bigger than 0).

      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is -10,
      then this function still returns 5
      (since all of the 6 numbers except -10 are bigger than -10;
      note that -10 is NOT bigger than itself).

      If  numbers   is  [45, 84, 32, 70, -10, 40]
      and threshold is -10.00000001,
      then this function returns 6.

    Type hints:
      :type numbers:   [float]
      :type threshold: float
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > threshold:
            count += 1
    return count

def test_count_positive_sines():
    """ Tests the   count_positive_sines   function. """
    # ------------------------------------------------------------------
    # DONE: 5. Implement this TEST function.
    #   It TESTS the  count_positive_sines  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond what we supplied.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    #
    # NOTE: Some numbers that you might expect to be zero,
    #   for example math.sin(math.pi), are in fact slightly positive.
    #   That is because   math.pi   is not exact (nor is math.sin).
    #   Simply stay away from such test cases in this problem.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_positive_sines   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 4
    actual = count_positive_sines([3, 4, 5, 6, 7, 8, 9])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2:
    expected = 2
    actual = count_positive_sines([3, 6, 8])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 3:
    expected = 3
    actual = count_positive_sines([7, 7, 7])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 4:
    expected = 0
    actual = count_positive_sines([6, 6, 6, 6, 6, 6, 6, 6, 6])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 5:
    expected = 1
    actual = count_positive_sines([3])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 6:
    expected = 0
    actual = count_positive_sines([6])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 7:
    expected = 0
    actual = count_positive_sines([5, 4, 6])
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 8:
    sequence = []
    for k in range(1064):
        sequence.append(k)
    expected = 532  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 9:
    sequence.append(1064)
    expected = 533  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 10:
    sequence.append(1065)
    expected = 533  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Add your ADDITIONAL test(s) here:
    
    sequence.append(1070)
    expected = 534  # Trust me!
    actual = count_positive_sines(sequence)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)


def count_positive_sines(numbers):
    """
    What comes in:  An sequence of numbers.
    What goes out: Returns the number of items in the given sequence
      whose sine is positive.
    Side effects: None.

    Examples:  Since:
       sine(3) is about 0.14
       sine(4) is about -0.76
       sine(5) is about -0.96
       sine(6) is about -0.28
       sine(7) is about 0.66
       sine(8) is about 0.99
       sine(9) is about 0.41

      -- count_positive_sines([3, 4, 5, 6, 7, 8, 9])  returns 4
      -- count_positive_sines([3, 6, 8])              returns 2
      -- count_positive_sines([7, 7, 7])              returns 3

    Type hints:
      :type sequence: [float]
    """
    # ------------------------------------------------------------------
    # DONE: 6. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    
    count = 0
    for i in range(len(numbers)):
        num = math.sin(numbers[i])
        if num > 0:
            count += 1
    return count


def test_sum_first_n():
    """ Tests the   sum_first_n   function. """
    # ------------------------------------------------------------------
    # DONE: 7. Implement this TEST function.
    #   It TESTS the  sum_first_n  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    #
    #   As usual, include both EXPECTED and ACTUAL results in your test
    #   and compute the latter BY HAND (not by running your program).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_first_n   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 0
    actual = sum_first_n([48, -10, 50, 5], 0)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 2:
    expected = 48
    actual = sum_first_n([48, -10, 50, 5], 1)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 3:
    expected = 38
    actual = sum_first_n([48, -10, 50, 5], 2)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 4:
    expected = 88
    actual = sum_first_n([48, -10, 50, 5], 3)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 5:
    expected = 93
    actual = sum_first_n([48, -10, 50, 5], 4)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 6:  This test uses a RANDOMLY generated sequence
    #          and an ORACLE to determine the expected (correct) result.
    sequence = []
    for _ in range(10000):
        sequence.append(random.randrange(-100, 100))
    expected = builtins.sum(sequence[:-1])
    actual = sum_first_n(sequence, 9999)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Test 7:  This test uses a RANDOMLY generated sequence
    #          and an ORACLE to determine the expected (correct) result.
    sequence = []
    for _ in range(10000):
        sequence.append(random.randrange(-100, 100))
    expected = builtins.sum(sequence[:-4000])
    actual = sum_first_n(sequence, 6000)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)

    # Add your ADDITIONAL test(s) here:
    
    expected = 108
    actual = sum_first_n([30,90,70,18,-70,-30,65], 6)
    print()
    print('Expected:', expected)
    print('Actual:  ', actual)


def sum_first_n(numbers, n):
    """
    What comes in:
      -- An sequence of numbers.
      -- A nonnegative integer   n   that is less than or equal to
           the length of the given sequence.
    What goes out:
      Returns the sum of the first   n   numbers in the given sequence,
      where   n   is the second argument.
    Side effects: None.
    Examples:
      If numbers is   [48, -10, 50, 5], then:
      - sum_first_n(numbers, 0) returns 0
      - sum_first_n(numbers, 1) returns 48
      - sum_first_n(numbers, 2) returns 38
      - sum_first_n(numbers, 3) returns 88
      - sum_first_n(numbers, 4) returns 93
    Type hints:
      :type numbers:   [float]
      :type n: int
    """
    # ------------------------------------------------------------------
    # DONE: 8. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # RESTRICTION:
    #    You may NOT use the built-in  sum   function
    #    in IMPLEMENTING this function.
    #      -- The TESTING code above does use   built_ins.sum
    #         as an ORACLE in TESTING this function, however.
    # ------------------------------------------------------------------
    
    tot = 0
    for i in range(n):
        tot = tot + numbers[i]
    return tot

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
