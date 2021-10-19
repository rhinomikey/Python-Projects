"""
This module lets you make some functions for the RoseBot robot.
They will make the robot move in interesting ways,
using the "time" approach:
  1. Start the robot moving.
  2. "Sleep" for T seconds, where T is the time necessary
       to go the distance that you want to go.
  3. Stop the robot.

We will later see better approaches that use sensors for feedback.

Authors: Dave Fisher, Leigh Mathews, David Mutchler, Sean Carter,
         Brandon Naylor, Mark Studer, Valerie Galluzzi,
         their colleagues and Josh Kuhn Nathan Gupta.  March 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosebot as rb


def main():
    """ Calls the   TEST   functions in this module. """
    # ------------------------------------------------------------------
    # Do only ONE of the following tests at each run.
    # Comment out the other two tests for each run.
    # ------------------------------------------------------------------
#     test_go_straight()
    test_spin()
#     test_trace_a_square()


def test_go_straight():
    """ Tests the   go_straight   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_straight   function:')
    print('  See the robot.')
    print('--------------------------------------------------')
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the   go_straight   function defined below.
    #   Include at least 2 reasonable tests, with a "sleep" in between
    #   the tests so that you can see what happened on each test.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(19)  # Use the number on YOUR robot
    connection = robot.connection

    go_straight(robot, 12, 200)

    connection.sleep(.5)

    go_straight(robot, 20, -200)

    connection.shutdown()


def go_straight(robot, distance_in_inches, pwm):
    """
    What comes in:  3 arguments:
      -- A RoseBot
      -- A number that is how far the robot should travel, in inches.
      -- A number  pwm  that is the power-level
           (-255 to 255, but never 0).
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. The robot starts moving straight ahead at the requested pwm
           (but straight BACKWARDS if  pwm  is negative).
      2. The Python program pauses ("sleeps") for T seconds,
           where T is the number of seconds required for the robot
           to go forward the given   distance_in_inches.
      3. The robot stops moving.

    Note: You will need to experiment to find a reasonable value
          for the constant involved in the formula for T.

        *** Do NOT try to get it exactly "right" ***
        since it depends on factors that include the battery level
        and it is NOT linear with speed (but treat it as if it were).

    Type hints:
      :type robot:               rb.RoseBot
      :type distance_in_inches:  float
      :type pwm:                 int
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #
    ####################################################################
    # HINT: To figure out the formula for T,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------


    robot.differential_drive.drive_pwm(pwm, pwm + 20)
    robot.connection.sleep(abs((distance_in_inches / pwm) * 15))
    robot.differential_drive.stop()


def test_spin():
    """ Tests the   spin   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   spin   function:')
    print('  See the robot.')
    print('--------------------------------------------------')
    # ------------------------------------------------------------------
    # TODO: 4. Implement this TEST function.
    #   It TESTS the   spin   function defined below.
    #   Include at least 2 reasonable tests, with a "sleep" in between
    #   the tests so that you can see what happened on each test.
    # ------------------------------------------------------------------

    robot = rb.RoseBot()
    robot.connect_wifly(19)  # Use the number on YOUR robot
    connection = robot.connection
    spin(robot, 90, 150)
    connection.sleep(.5)

    connection.shutdown()


def spin(robot, distance_in_degrees, pwm):
    """
    What comes in:  3 arguments:
      -- A RoseBot
      -- A number that is how far the robot should spin, in degrees.
      -- A number  pwm  that is the power-level
           (-255 to 255, but never 0).
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. The robot starts spinning (in place) clockwise at the
           requested pwm (but counter-clockwise if  pwm  is negative).
      2. The Python program pauses ("sleeps") for T seconds,
           where T is the number of seconds required for the robot
           to spin the given   distance_in_degrees.
      3. The robot stops moving.

    Note: You will need to experiment to find a reasonable value
          for the constant involved in the formula for T.

        *** Do NOT try to get it exactly "right" ***
        since it depends on factors that include the battery level
        and it is NOT linear with speed (but treat it as if it were).

    Type hints:
      :type robot:                rb.RoseBot
      :type distance_in_degrees:  float
      :type pwm:                  int

    """

    robot.differential_drive.drive_pwm(-pwm, pwm)
    robot.connection.sleep((distance_in_degrees / pwm) * 15)

    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    #
    ####################################################################
    # HINT: To figure out the formula for T,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------


def test_trace_a_square():
    """ Tests the   trace_a_square   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   trace_a_square   function:')
    print('  See the robot.')
    print('--------------------------------------------------')
    # ------------------------------------------------------------------
    # TODO: 6. Implement this TEST function.
    #   It TESTS the   trace_a_square   function defined below.
    #   A SINGLE test is ample.
    # ------------------------------------------------------------------


def trace_a_square(robot):
    """
    What comes in:  A RoseBot.
    What goes out:  Nothing (i.e., None).
    Side effects:  The robot follows a path that is a square.
    Notes:
      -- Your square can be whatever size you want.
      -- You can use whatever speeds you want.
      -- It is NOT important that the square be at all exact!
    Type hints:
      :type robot: rb.RoseBot
    """
    # ------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #
    ####################################################################
    # IMPORTANT: To receive full credit, you MUST:
    #   -- Appropriately CALL the functions that you implemented above.
    #   -- Use a LOOP appropriately.
    ####################################################################
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
