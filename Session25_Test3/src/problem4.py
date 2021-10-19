"""
Test 3, problem 3.

Authors: David Mutchler, Dave Fisher, their colleagues
              and Nathan Gupta.  May 2016.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
#     test_let_air_out()
#     test_puncture()
#     test_blow_once()
#     test_blow_many_times()
#     test_change_owner()
#     test_get_owners()
    test_return_new_Balloon()
    test_puncture_bigger_balloon()

# ----------------------------------------------------------------------
# STUDENTS:  The TEST functions appear next.
#   ** Find the  ** BALLOON ** class  *** AFTER ***  the TEST functions.
# ----------------------------------------------------------------------


def test_let_air_out():
    person1 = Person('bob',61,150)
    person2 = Person('sue',11,85)
    
    b1 = Balloon(3.5,person1)
    b2 = Balloon(4.0,person2)
    
    print('Expected: ',3.5,3.5)
    print('Actual: ',b1.current_volume,b1.capacity)
    print()
    
    b1.let_air_out(2.5)
    print('Expected: ',1.5,3.5)
    print('Actual: ',b1.current_volume,b1.capacity)
    print()
    
    print('Expected: ',4.0,4.0)
    print('Actual: ',b2.current_volume,b2.capacity)
    print()
    
    b2.let_air_out(10)
    print('Expected: ',0,4.0)
    print('Actual: ',b2.current_volume,b2.capacity)
    print()

def test_puncture():
    person1 = Person('bob',61,150)
    person2 = Person('sue',11,85)
    
    b1 = Balloon(3.5,person1)
    b2 = Balloon(4.0,person2)
    
    b1.puncture()
    print('Expected: ',0,False)
    print('Actual: ',b1.current_volume,person1.is_happy)
    print()


def test_blow_once():
    person1 = Person('bob',61,150)
    person2 = Person('sue',11,85)
    
    b1 = Balloon(3.4,person1)
    b2 = Balloon(4.0,person2)
    
    b1.let_air_out(2.5)
    b1.blow_once()
    print('Expected: ',1.9,True)
    print('Actual: ',b1.current_volume,person1.is_happy)
    print()
    
    b2.let_air_out(0)
    b2.blow_once()
    print('Expected: ',0,False)
    print('Actual: ',b2.current_volume,person2.is_happy)
    print()


def test_blow_many_times():
    person1 = Person('bob',61,150)
    person2 = Person('sue',11,85)
    
    b1 = Balloon(3.4,person1)
    b2 = Balloon(4.0,person2)
    
    b1.let_air_out(2.5)
    b1.blow_many_times(3)
    print('Expected: ',2.9,True)
    print('Actual: ',b1.current_volume,person1.is_happy)
    print()
    
    b2.let_air_out(0)
    b2.blow_many_times(8)
    print('Expected: ',0,False)
    print('Actual: ',b2.current_volume,person2.is_happy)
    print()


def test_change_owner():
    person1 = Person('bob',61,150)
    person2 = Person('sue',11,85)
    
    b1 = Balloon(3.4,person1)
    b2 = Balloon(4.0,person2)
    
    print('Expected: ',person2)
    print('Actual: ',b1.change_owner(person2))
    
    print('Expected: ',person1)
    print('Actual: ',b2.change_owner(person1))


def test_get_first_owner():
    pass


def test_get_owners():
    person1 = Person('bob',61,150)
    person2 = Person('sue',11,85)
    
    b1 = Balloon(3.4,person1)
    b2 = Balloon(4.0,person2)
    
    b1.change_owner(person2)
    print('Expected: ',person1,person2)
    print('Actual: ',b1.get_owners())
    print()
    
    b2.change_owner(person1)
    print('Expected: ',person2,person1)
    print('Actual: ',b2.get_owners())


def test_return_new_Balloon():
    person1 = Person('bob',61,150)
    
    b1 = Balloon(3.4,person1)
    
    b1.return_new_Balloon(person1)
    print('Expected: ',b1.return_new_Balloon(person1))
    print('Actual: ')
    print()


def test_puncture_bigger_balloon():
    pass


# ---------------------------------------------------------------------
# DONE: Implement the   Balloon   class below.
#       Test your methods by using the  problem2_test_Balloon  module.
#
# IMPORTANT:
#  1. Read the specification of the ENTIRE   Balloon   class BEFORE
#       writing any code.
#  2. Test each method AS YOU DEFINE IT (one by one).
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# USE this Person class in implementing the Balloon class below.
# ----------------------------------------------------------------------
class Person(object):
    """
    Simulates a person with an age (in years) and weight (in pounds).
    """

    def __init__(self, name, age, weight, is_happy=True):
        """
        Stores the Person's name, age and weight.
        The Person starts out happy by default.
        """
        self.name = name
        self.age = age
        self.weight = weight
        self.is_happy = is_happy

    def __repr__(self):
        """ Returns a string representation of this Person. """
        return 'Person({}, {}, {})'.format(self.age,
                                           self.weight,
                                           self.is_happy)


class Balloon(object):
    """
    A Balloon:
      -- CAPACITY - how much air can be blown into it before it pops
      -- CURRENT_VOLUME - how much air is currently in the balloon
      -- OWNER - the owner of the Balloon (a Person)
    and any other instance variables you find the need for.
    """

    def __init__(self, original_capacity, original_owner):
        """
        Stores the Balloon's capacity and owner in the instance variables
          self.capacity
          self.owner
        and sets the initial volume of the Balloon to its capacity
        (that is, the Balloon starts out already inflated to its capacity).
        
        The capacity and current_volume are in cubic feet.
        The owner is a Person object.
        
          :type original_capacity: float
          :type owner: Person
        """
        ################################################################
        # DONE:
        #   READ the green doc-string (specification) above.  If you
        #   do not understand it, ASK YOUR INSTRUCTOR to explain it.
        #
        #   READ the code that we supplied below.  Make sure that
        #   you understand it before you continue.
        #     Note:  the   self.person   instance variable is
        #     a Person, as defined in the Person class above.
        #
        #   Do NOT change this method at this time!  You will need
        #   to AUGMENT this method later for some of the other methods.
        #
        #   Mark this TODO as DONE when you feel like you understand
        #   this method.
        ################################################################
        self.capacity = original_capacity
        self.owner = original_owner
        self.current_volume = self.capacity
        self.check_puncture = False
        self.ori_owner = original_owner

      
    def let_air_out(self, seconds):
        """
        What comes in:
          -- self
          -- A positive floating point number that gives
               the number of seconds that the person blows air
               into this Balloon.
        What goes out: Nothing (i.e., None).
        
        Side effects:
          The Balloon's current volume is reduced according
          to the following formula:
            Every second removes 0.8 cubic feet from the Balloon
            (but the Balloon never has negative volume)
        Type hints:
          :type seconds: int
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        self.current_volume = self.current_volume - (seconds*.8)
        if self.current_volume < 0:
            self.current_volume = 0
        
    def puncture(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        
        Side effects:
        Punctures the balloon (putting a hole into it).
        Thus this method reduces the Balloon's current volume to 0.
        
        Additionally, the Balloon's owner becomes sad when her
        Balloon is punctured, that is, this method changes
        the   is_happy   instance variable of this Balloon's owner
        to False.
        
        Additionally, a Balloon that has been punctured
        can NOT be re-inflated -- so blowing air into a punctured
        Balloon (see the blow_once and blow_many methods below)
        has no effect.
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        self.current_volume = 0
        self.owner.is_happy = False
        self.check_puncture = True

    def blow_once(self):
        """
        What comes in:
          -- self
        What goes out: Nothing (i.e., None).
        
        Side effects:
          The Balloon's current volume is increased according
          to the following formula:
          
            If the age of this Balloon's owner is less than 12,
            add 0.03 cubic feet to this balloon's current volume;
            otherwise, add 0.5 cubic feet to this balloon's current volume.

          Additionally, if this balloon's current volume exceeds
          its capacity, the balloon bursts (so its current_volume is set
          to 0) and its owner becomes sad (that is, the owner's  is_happy
          instance variable becomes False).

          If a person blows air into a punctured or burst balloon,
          nothing happens -- the current volume stays at 0.
          
          Note that a Balloon that has current volume might have
          burst, or might have been punctured, or might have had
          all its air let out.  In the first two cases, attempting
          to blow into the Balloon has no effect.  But in the third
          case, the Balloon can have more air blown into it.
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        #Because the current volume is = to the capacity no matter what the volume
        #will be over the capacity.
        
        if self.check_puncture == True:
            self.current_volume = 0
        if self.owner.age < 12:
            self.current_volume = self.current_volume + .03
        if self.owner.age > 12:
            self.current_volume = self.current_volume + .5
        if self.current_volume >= self.capacity:
            self.current_volume = 0
            self.owner.is_happy = False
            

    def blow_many_times(self, number_of_breaths):
        """
        A person blows into this balloon the given number of times.
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        if self.check_puncture == True:
            self.current_volume = 0
        if self.owner.age < 12:
            self.current_volume = self.current_volume + (number_of_breaths*.03)
        if self.owner.age > 12:
            self.current_volume = self.current_volume + (number_of_breaths*.5)
        if self.current_volume >= self.capacity:
            self.current_volume = 0
            self.owner.is_happy = False

    def change_owner(self, new_owner):
        """
        Changes this Balloon's owner to the given Person.
        
        :type new_owner: Person
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        self.owner = new_owner
        return self.owner

    def get_owners(self):
        """
        RETURNS a list of all the owner's of this Balloon,
        in the order in which they took ownership.
        
        So if the original owner of this Balloon was person1,
        and then the  change_owner   method was called to
        change the owner to person2, and later the  change_owner
        method was called again to change the owner to person3,
        then this method would return [person1, person2, person3].
                
          :type new_owner: Person
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        return [self.ori_owner,self.owner]

    def return_new_Balloon(self, owner):
        """
        RETURNS a NEW Balloon whose capacity is the same as the capacity
        of this Balloon but whose owner is the given Person.
          :type owner: Person
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------
        
        #Not sure how to test this function but am fairly confident that it should work.
        
        new_balloon = Balloon(self.capacity,owner)
        return new_balloon
        
    def puncture_bigger_balloon(self, other_balloon):
        """
        Punctures either this Balloon or the given other_balloon,
        whichever has larger current volume.
        Break ties however you want.
        """
        # --------------------------------------------------------------
        # DONE:  Implement and test this function.
        #  Write tests (in the TEST function above) as appropriate.
        # --------------------------------------------------------------

        if other_balloon.current_volume > self.current_volume:
            other_balloon.puncture()
        else:
            self.current_volume = 0
            self.owner.is_happy = False
            

# ----------------------------------------------------------------------
# Calls main to start the ball rolling.
#   More precisely, calls main only if this module is running at the
#   top level (as opposed to being imported by another module).
#   This structure helps us automate tests of this module.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()