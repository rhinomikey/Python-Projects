"""
Test 3, problem 3.

Authors: David Mutchler, Dave Fisher, their colleagues
              and Nathan Gupta.  May 2016.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()


def test_problem3():
    """ Tests the    problem3    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('--------------------------------------------------')
    # ------------------------------------------------------------------
    # Write here what tests you think appropriate
    # (but at least 2 tests).
    # ------------------------------------------------------------------
    
    seq = [(3, 1, 4),
         (2.5, 10, 1),
         [1, 2.5, 3, 4]
        ]
    print('Expected: ',10)
    print('Actual: ',problem3(seq))
    print()
    
    seq = [(2.5,9,80),
         (17,79.9,80.1),
         [90,100,10,90]
        ]
    print('Expected: ',100)
    print('Actual: ',problem3(seq))


def problem3(sequence_of_sequences):
    """
    Returns the largest number in the subsequences of the given
    sequence.  Returns None if there are no subsequences or
    all the subsequences are empty.
    #
    For example, if the argument is:
        [(3, 1, 4),
         (2.5, 10, 1),
         [1, 2.5, 3, 4]
        ]
    then this function returns:  10.
    This function returns None if the given argument is:
      []
    or
      [[], [], []]
      
    Precondition:  the given argument is a sequence of sequences,
    and each subsequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # DONE: Implement and test this function.
    #   Write tests (above) as appropriate.
    # ------------------------------------------------------------------

    seq = sequence_of_sequences
    num_seq = []
    large = 0
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            num_seq.append(seq[i][j])
    for i in range(len(num_seq)-1):
        if num_seq[i] > num_seq[i+1]:
            large = num_seq[i]
    return large


# ----------------------------------------------------------------------
# Calls main to start the ball rolling.
#   More precisely, calls main only if this module is running at the
#   top level (as opposed to being imported by another module).
#   This structure helps us automate tests of this module.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
