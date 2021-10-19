"""
This module lets you make some functions for the RoseBot robot.
They will make the robot move in interesting ways,
using SENSORS (including the wheel encoders) to stop the movement.

Each uses the  WAIT-UNTIL-EVENT  pattern.

Authors: Dave Fisher, Leigh Mathews, David Mutchler, Sean Carter,
         Brandon Naylor, Mark Studer, Valerie Galluzzi,
         their colleagues and Nathan Gupta.  April 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosebot as rb


def main():
    """ Calls the   TEST   functions in this module. """
    # ------------------------------------------------------------------
    # Do only ONE of the following tests at each run.
    # Comment out the other two tests for each run.
    # ------------------------------------------------------------------
#     test_go_until_reflectance_exceeds()
#     test_go_distance()
    test_go_many_distances()


def test_go_until_reflectance_exceeds():
    """ Tests the   go_until_reflectance_exceeds   function. """
    print()
    print('------------------------------------------------------')
    print('Testing the   go_until_reflectance_exceeds   function:')
    print('  See the robot.')
    print('------------------------------------------------------')
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the   go_until_reflectance_exceeds   function
    #   defined below.
    #   Include at least 2 reasonable tests, with a "sleep" in between
    #   the tests so that you can see what happened on each test.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(31)  # Use the number on YOUR robot
    connection = robot.connection

    go_until_reflectance_exceeds(robot, 700, 200)

    connection.sleep(3.0)

    go_until_reflectance_exceeds(robot, 200, -100)

    connection.shutdown()


def go_until_reflectance_exceeds(robot, threshold, pwm):
    """
    What comes in:  3 arguments:
      -- A RoseBot
      -- A number that is the "threshold" for when the robot should stop
      -- A number  pwm  that is the power-level
           (-255 to 255, but never 0).
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. The robot starts moving straight ahead at the requested pwm
           (but straight BACKWARDS if  pwm  is negative).

      2. The Python program repeatedly checks one of its reflectance
           sensors (use whichever one you want).

         The robot stops (and the function ends) when the reflectance
         sensor returns a value greater than the given threshold.

    Type hints:
      :type robot:      rb.RoseBot
      :type threshold:  int
      :type pwm:        int
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    ####################################################################
    #   HINT: Use the  WAIT-UNTIL-EVENT  pattern.
    ####################################################################
    # ------------------------------------------------------------------

    while True:
        if robot.middle_reflectance_sensor.read() < threshold:
            robot.differential_drive.drive_pwm(pwm, pwm)
            robot.connection.sleep(.5)
        else:
            break

    print(robot.left_reflectance_sensor.read(),
                           robot.middle_reflectance_sensor.read(),
                           robot.right_reflectance_sensor.read())

def test_go_distance():
    """ Tests the   go_distance   function. """
    print()
    print('------------------------------------------------------')
    print('Testing the   go_distance   function:')
    print('  See the robot.')
    print('------------------------------------------------------')
    # ------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the   go_distance   function defined below.
    #   Include at least 2 reasonable tests, with a "sleep" in between
    #   the tests so that you can see what happened on each test.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(16)  # Use the number on YOUR robot
    connection = robot.connection

    # Put your FIRST test here:
    go_distance(robot, 1000, 150)

    connection.sleep(.5)

    # Put a SECOND test here:
    go_distance(robot, 1000, 200)

    connection.shutdown()


def go_distance(robot, distance_in_ticks, pwm):
    """
    What comes in:  3 arguments:
      -- A RoseBot
      -- A number that is how far the robot should travel, in "ticks".
      -- A number  pwm  that is the power-level (1 to 255).
    What goes out:  Nothing (i.e., None).
    Side effects:
      1. The robot starts moving straight ahead at the requested pwm.

      2. The Python program repeatedly checks one of its wheel encoders
           (use whichever one you want).

         The robot stops (and the function ends) when the wheel encoder
         indicates that the robot has gone the given number of "ticks".

    Type hints:
      :type robot:             rb.RoseBot
      :type distance_in_ticks: int
      :type pwm:               int
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    ####################################################################
    #   HINT: Use the  WAIT-UNTIL-EVENT  pattern.
    ####################################################################
    # ------------------------------------------------------------------

    robot.right_encoder.reset()
    robot.left_encoder.reset()
    while True:
        robot.connection.sleep(1)
        print(robot.right_encoder.read(), robot.left_encoder.read())
        if robot.right_encoder.read() < distance_in_ticks and robot.left_encoder.read() < distance_in_ticks:
            robot.differential_drive.drive_pwm(pwm, pwm)
            robot.connection.sleep(.5)
        else:
            break


def test_go_many_distances():
    """ Tests the   go_many_distances   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   go_many_distances   function:')
    print('  See the robot.')
    print('--------------------------------------------------')
    # ------------------------------------------------------------------
    # DONE: 6. Implement this TEST function.
    #   It TESTS the   go_many_distances   function defined below.
    #   Include at least 2 reasonable tests, with a "sleep" in between
    #   the tests so that you can see what happened on each test.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(16)  # Use the number on YOUR robot
    connection = robot.connection

    # Put your FIRST test here:
    go_many_distances(robot, [500, 1000, 700, 300])

    connection.sleep(1)

    # Put a SECOND test here:
    go_many_distances(robot, [300, 400, 500, 600])

    connection.shutdown()


def go_many_distances(robot, distances):
    """
    What comes in:  2 arguments:
      -- A RoseBot
      -- A SEQUENCE of distances (in "ticks") that the robot should go
    What goes out:  Nothing (i.e., None).
    Side effects:
      For each distance in the given sequence of distances, the robot:
        1. Goes the given distance (at whatever speed you want).
        2. Pauses there for 1 second.
        3. Spins for 1 second (at whatever speed you want).
        4. Pauses there for 1 second.
    Feel free to change the pauses to be shorter or longer
    (or even of RANDOM length!), whatever you wish.

    Type hints:
      :type robot:      rb.RoseBot
      :type distances:  [int]
    """
    # ------------------------------------------------------------------
    # DONE: 7. Implement and test this function.
    ####################################################################
    # IMPORTANT: Do NOT rewrite code you have already done!
    #            Instead, CALL the relevant function!
    ####################################################################
    # ------------------------------------------------------------------

    for i in range(len(distances)):
        while True:
            if robot.left_encoder.read() < distances[i] and robot.left_encoder.read() < distances[i]:
                robot.differential_drive.drive_pwm(100, 100)
                robot.connection.sleep(.05)
            else:
                robot.differential_drive.stop()
                robot.right_encoder.reset()
                robot.left_encoder.reset()
                robot.connection.sleep(2)
                break


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
