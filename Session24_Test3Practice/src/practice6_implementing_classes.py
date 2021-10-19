"""
PRACTICE Test 3.

This problem provides practice at:
  ***  IMPLEMENTING CLASSES.  ***

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
    test_init()
    test_double()
    test_shrink()
    test_double_then_shrink()
    test_reset()
    test_steal()
    test_history()

# ----------------------------------------------------------------------
# STUDENTS:  The TEST functions appear next.
#   ** Find the  ** BOX ** class   *** AFTER ***   the TEST functions.
# ----------------------------------------------------------------------


def test_init():
    """ Tests the   __init__   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Box class.')
    print('-----------------------------------------------------------')

    expected_contents = 'Good morning'
    expected_volume = 20
    box = Box(expected_contents, expected_volume)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    expected_contents = 'Good morning'
    expected_volume = 12
    box = Box(expected_contents, expected_volume)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    # Test case volume < contents
    expected_contents = 'Good morning'
    expected_volume = 8
    box = Box(expected_contents, 8)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


def test_double():
    """ Tests the   double   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   double   method of the Box class.')
    print('-----------------------------------------------------------')

    initial_contents = 'Good morning'
    expected_contents = initial_contents + initial_contents
    expected_volume = 24
    box = Box(initial_contents, expected_volume)
    box.double()
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    initial_contents = 'Good morning'
    expected_contents = initial_contents + initial_contents
    expected_volume = 30
    box = Box(initial_contents, expected_volume)
    box.double()
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    initial_contents = 'Good morning'
    expected_contents = initial_contents
    expected_volume = 23
    box = Box(initial_contents, expected_volume)
    box.double()
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    initial_contents = 'Good morning'
    expected_contents = initial_contents * 4
    expected_volume = 100
    box = Box(initial_contents, expected_volume)
    box.double()
    box.double()
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


def test_shrink():
    """ Tests the   shrink   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   shrink   method of the Box class.')
    print('-----------------------------------------------------------')

    initial_contents = 'Good morning'
    initial_volume = 12
    expected_contents = 'Good'
    expected_volume = 4
    box = Box(initial_contents, initial_volume)
    box.shrink(expected_volume)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    initial_contents = 'Good morning'
    initial_volume = 30
    expected_contents = initial_contents
    expected_volume = 15
    box = Box(initial_contents, initial_volume)
    box.shrink(expected_volume)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


def test_double_then_shrink():
    """ Tests the   double_then_shrink   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   double_then_shrink   method of the Box class.')
    print('-----------------------------------------------------------')
    initial_contents = 'Good morning'
    initial_volume = 24
    expected_contents = initial_contents + 'Goo'
    expected_volume = 15
    box = Box(initial_contents, initial_volume)
    box.double_then_shrink(expected_volume)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    initial_contents = 'Good morning'
    initial_volume = 15
    expected_contents = initial_contents
    expected_volume = 14
    box = Box(initial_contents, initial_volume)
    box.double_then_shrink(expected_volume)
    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


def test_reset():
    """ Tests the   reset   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   reset   method of the Box class.')
    print('-----------------------------------------------------------')

    initial_contents = 'Good morning'
    initial_volume = 100

    expected_contents = initial_contents
    expected_volume = initial_volume

    box = Box(initial_contents, initial_volume)
    box.double()
    box.double_then_shrink(2)
    box.reset()

    print("Expected:", expected_contents, expected_volume)
    print("Actual:  ", box.contents, box.volume)
    if (expected_contents == box.contents) and (expected_volume == box.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


def test_steal():
    """ Tests the   steal   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   steal   method of the Box class.')
    print('-----------------------------------------------------------')

    initial_contents_1 = 'Good morning'
    initial_volume_1 = 100
    initial_contents_2 = 'Hello'
    initial_volume_2 = 10

    expected_contents_1 = initial_contents_1 + initial_contents_2
    expected_volume_1 = initial_volume_1

    expected_contents_2 = ''
    expected_volume_2 = initial_volume_2

    box1 = Box(initial_contents_1, initial_volume_1)
    box2 = Box(initial_contents_2, initial_volume_2)
    box1.steal(box2)

    print("Expected 1:", expected_contents_1, expected_volume_1)
    print("Actual   1:", box1.contents, box1.volume)

    print("\nExpected 2:", expected_contents_2, expected_volume_2)
    print("Actual   2:", box2.contents, box2.volume)
    if (expected_contents_1 == box1.contents) and \
            (expected_volume_1 == box1.volume) \
            and (expected_contents_2 == box2.contents) \
            and (expected_volume_2 == box2.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()

    initial_contents_1 = 'Good morning'
    initial_volume_1 = 12
    initial_contents_2 = 'Hello'
    initial_volume_2 = 10

    expected_contents_1 = initial_contents_1 + initial_contents_2
    expected_volume_1 = initial_volume_1 + len(initial_contents_2)

    expected_contents_2 = ''
    expected_volume_2 = initial_volume_2

    box1 = Box(initial_contents_1, initial_volume_1)
    box2 = Box(initial_contents_2, initial_volume_2)
    box1.steal(box2)

    print("Expected 1:", expected_contents_1, expected_volume_1)
    print("Actual   1:", box1.contents, box1.volume)

    print("\nExpected 2:", expected_contents_2, expected_volume_2)
    print("Actual   2:", box2.contents, box2.volume)
    if (expected_contents_1 == box1.contents) \
            and (expected_volume_1 == box1.volume) \
            and (expected_contents_2 == box2.contents) \
            and (expected_volume_2 == box2.volume):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


def test_history():
    """ Tests the   history   method of the Box class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   history   method of the Box class.')
    print('-----------------------------------------------------------')
    expected_results = ['Good']
    b = Box('Good', 20)

    hist = b.history()
    print("Expected:", expected_results)
    print("Actual:  ", hist)
    if (expected_results == hist):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print("\n")

    expected_results = ['Good', 'GoodGood', 'GoodGo',
                        'GoodGo', 'Good', 'Go']
    b = Box('Good', 20)
    b.double()
    b.shrink(6)

    b.double()
    b.reset()
    b.shrink(2)
    hist = b.history()
    print("Expected:", expected_results)
    print("Actual:  ", hist)
    if (expected_results == hist):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")
    print()


class Box(object):
    """
    A Box has:
        -- CONTENTS, which is a string, and
        -- VOLUME, which is a non-negative integer.
    The length of the Box's CONTENTS
    can never exceed the Box's VOLUME.
    """

    def __init__(self, contents, volume):
        """
        Stores the Box's contents and volume in the instance variables
          self.contents
          self.volume

        EXCEPT: if the given volume is less than the length of the
        given contents, then self.volume is set to the length of the
        given contents.  For example, if contents is 'Good morning'
        but volume is 7, then self.volume is set to 12 (which is
        the length of 'Good morning'), not 7.

        Initializes other instance variables as needed by other methods.
          :type contents: str
          :type volume: int
        """
        # --------------------------------------------------------------
        # DONE: 2. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      4
        #    TIME ESTIMATE:   5 minutes.
        # --------------------------------------------------------------
        
        self.contents = contents
        self.volume = volume
        self.container_vol = volume
        self.container_con = contents
        self.his_con_double = contents
        self.his_con_shrink = contents
        self.his_con_double_shrink = contents
        self.his_con_reset = contents
        self.his_con_steal = contents

    def double(self):
        """
        If this Box's volume is greater than or equal to TWICE the
        length of this Box's contents, this method changes this Box's
        contents to what it was PLUS what it was.  Otherwise,
        this method leaves the Box's contents unchanged.

        For example, if this Box currently has contents 'OK Bob':
          -- if this Box's volume is 30, then this method changes
               this Box's contents to 'OK BobOK Bob'.
          -- if this Box's volume is 11 (or any smaller number),
               then this method leaves this Box's contents unchanged.
        """
        # --------------------------------------------------------------
        # DONE: 3. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      6
        #    TIME ESTIMATE:   5 minutes.
        # --------------------------------------------------------------
        
        if self.volume >= 2*len(self.contents):
            self.contents = self.contents + self.contents
            self.his_con_double = self.contents

    def shrink(self, new_volume):
        """
        1. Sets this Box's volume to the given new_volume.

        2. If the new volume is less than the length of this Box's
             contents, sets this Box's contents to what it was
             but "clipped" to fit in this Box.

        For example, if this Box currently has contents 'Good morning'
        and volume 30, and if new_volume is 7, then this method
        changes this Box's volume to 7 and changes this Box's contents
        to 'Good mo' (since the first-7-characters substring
        of 'Good morning' is the string 'Good mo').

        Another example: if this Box currently has contents 'Good morning'
        and volume 30, and if new_volume is 35, then this method
        changes this Box's volume to 35 and leaves its contents unchanged.

          :type new_volume: int  that is nonnegative
        """
        # --------------------------------------------------------------
        # DONE: 4. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      7
        #    TIME ESTIMATE:   5 minutes.
        # --------------------------------------------------------------
        
        self.volume = new_volume
        if len(self.contents) > new_volume:
            self.contents = self.contents[0:new_volume]
            self.his_con_shrink = self.contents
        return self.contents

    def double_then_shrink(self, newer_volume):
        """
        Calls this Box's double method,
        then calls this Box's shrink method with the given newer_volume.
        """
        # --------------------------------------------------------------
        # DONE: 5. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      4
        #    TIME ESTIMATE:   3 minutes.
        # --------------------------------------------------------------
        
        self.double()
        self.shrink(newer_volume)
        self.his_con_double_shrink = self.contents

    def reset(self):
        """
        Changes this Box's contents and volume to whatever they were
        when this Box was constructed.
        """
        # --------------------------------------------------------------
        # DONE: 6. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      7
        #    TIME ESTIMATE:   5 minutes.
        # --------------------------------------------------------------
        
        self.contents = self.container_con
        self.volume = self.container_vol
        self.his_con_reset = self.container_con

    def steal(self, other_box):
        """
        1. Sets this Box's contents to what is was, but with the
             other Box's contents appended to this Box's contents.
        2. If this Box's volume is less than the length of
             this Box's NEW contents, then this method sets
             this Box's volume to the length of this Box's NEW contents.
        3. Sets the other Box's contents to the empty string.

        See the TEST cases for examples.

          :type other_box: Box
        """
        # --------------------------------------------------------------
        # DONE: 7. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      7
        #    TIME ESTIMATE:   5 minutes.
        # --------------------------------------------------------------
        
        self.contents = self.contents + other_box.contents
        if self.volume < len(self.contents):
            self.volume = len(self.contents)
        other_box.contents = ''
        
        self.his_con_steal = self.contents

    def history(self):
        """
        Returns a list that contains the contents of this Box
          -- when it was constructed
          -- when it had any of the above methods applied to it
          -- when it had any of the above methods applied to it
          -- when it had any of the above methods applied to it
          --   ...
        to this point.

        For example, the following code:
          b = Box('Good', 20)   # [b's contents is now 'Good', and its
                                #      volume is now 20]
          b.double()            # [b's contents is now 'GoodGood']
          b.shrink(6)           # [b's contents is now 'GoodGo', and its
                                #      volume is now 6]
          b.double()            # [b's contents remains 'GoodGo']
          b.reset()             # [b's contents returns to 'Good', and its
                                #      volume returns to 20]
          b.shrink(2)           # [b's contents is now 'Go']
          h = b.history()
          print(h)

        would print:
          ['Good', 'GoodGood', 'GoodGo', 'GoodGo', 'Good', 'Go']
        """
        # --------------------------------------------------------------
        # TODO: 8. Implement and test this function.
        #     The testing code is already written for you (above).
        # --------------------------------------------------------------
        # --------------------------------------------------------------
        # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
        #    DIFFICULTY:      8
        #    TIME ESTIMATE:   5 minutes.
        # --------------------------------------------------------------
        
        return [self.container_con,self.his_con_double,self.his_con_shrink,self.his_con_double_shrink,self.his_con_reset,self.his_con_steal]

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
