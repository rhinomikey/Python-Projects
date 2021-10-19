"""
This module is a VERY BASIC introduction to the RoseBot robot.
We'll use it to:
  -- Test whether your robot is "up and running".
  -  Help you see how to run a RoseBot.
  -- Serve as a basic example for making a RoseBot blink and move.

Authors: Dave Fisher, Leigh Mathews, David Mutchler, Sean Carter,
         Brandon Naylor, Mark Studer, Valerie Galluzzi,
         their colleagues and Josh Kuhn & Nathan Gupta.  March 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosebot as rb

# ----------------------------------------------------------------------
# DONE: 2. READ the program below WITH YOUR INSTRUCTOR
#          and RUN it (using your robot).
#
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#     CHANGE THE TODO at the beginning of this comment to DONE.
# ----------------------------------------------------------------------


def main():
    """
    Does two simple hardware tests,
    then makes the robot move in whatever way you like!
    """
    # ------------------------------------------------------------------
    # Do only ONE of the following at each run.
    # Comment out the other two for each run.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    # test_blink()
    # test_move()
    you_make_your_robot_move()
    robot.connection.shutdown()


def test_blink():
    """
    Connects to a RoseBot and does a very simple hardware test:
      -- Make an LED blink.
    """
    # ------------------------------------------------------------------
    # Construct a RoseBot, then connect to it wirelessly.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(19)  # Use the number on YOUR robot

    # ------------------------------------------------------------------
    # A RoseBot has many subcomponents, including:
    #   -- An  LED          object that can be turned on and off.
    #   -- A   Connection   object that can "sleep".
    #
    # When a Connection "sleeps", the PYTHON program pauses at that
    # point for the specified number of seconds.  The ROBOT keeps on
    # doing whatever it is doing, via the ROBOT's on-board processor.
    # ------------------------------------------------------------------
    led = robot.led
    connection = robot.connection

    print()
    print('Blinking 7 times!')
    for _ in range(7):
        led.on()
        connection.sleep(0.5)
        led.off()
        connection.sleep(0.5)

    print('Done blinking.')

    # ------------------------------------------------------------------
    # Asking the RoseBot's Connection to do a   shutdown   leaves
    # the robot in a clean state for the next run.
    # ------------------------------------------------------------------
    connection.shutdown()


def test_move():
    """
    Connects to a RoseBot and does a very simple hardware test:
      -- Make the robot move a bit.
    """
    # ------------------------------------------------------------------
    # Construct a RoseBot, then connect to it wirelessly.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(19)  # Use the number on YOUR robot

    # ------------------------------------------------------------------
    # A RoseBot also has:
    #   -- A   DifferentialDrive   object that can make the robot move.
    #
    # Today, all the  DifferentialDrive  methods are disabled EXCEPT:
    #   -- drive_pwm(left_wheel_speed, right_wheel_speed)
    #   -- stop().
    #
    #   The units for   drive_pwm   range from:
    #      -255 (full speed backward) to
    #       255 (full speed forward).
    #
    # FWIW,  pwm  is an abbreviation for "pulse width modulation".
    # ------------------------------------------------------------------
    driver = robot.differential_drive
    connection = robot.connection

    # ------------------------------------------------------------------
    # The next 3 statements (after the PRINTs)
    # make the robot move, as follows:
    #   1. Tell the robot to start moving (spinning):
    #   2. Pause ("sleep") the Python program for 3 seconds:
    #   3. Tell the robot to stop.
    # ------------------------------------------------------------------
    print()
    print('Spinning!')

    driver.drive_pwm(100, -100)
    connection.sleep(3.0)
    driver.stop()

    print('Done spinning.')

    # ------------------------------------------------------------------
    # Asking the RoseBot's Connection to do a   shutdown   leaves
    # the robot in a clean state for the next run.
    # ------------------------------------------------------------------
    connection.shutdown()


def you_make_your_robot_move():
    """
    Connects to a RoseBot and makes it move in whatever way you want!
    """
    robot = rb.RoseBot()
    robot.connect_wifly(19)

    robot.differential_drive.drive_pwm(100, 0)
    robot.connection.sleep(1)
    robot.differential_drive.drive_pwm(200, 200)
    robot.connection.sleep(2)
    robot.differential_drive.stop()
    # ------------------------------------------------------------------
    # DONE: 3. Connect to your RoseBot
    #   and make it move around in whatever ways you want!
    #   Include at least  2   DIFFERENT motions.
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
