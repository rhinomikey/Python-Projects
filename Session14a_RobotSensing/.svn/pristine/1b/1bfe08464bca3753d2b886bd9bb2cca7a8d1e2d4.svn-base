"""
This module is a VERY BASIC introduction to the RoseBot robot.
We'll use it to:
  -- Test whether your robot is "up and running".
  -  Help you see how to run a RoseBot.
  -- Serve as a basic example for making a RoseBot:
       -- blink
       -- move
       -- sense its environment

Authors: Dave Fisher, Leigh Mathews, David Mutchler, Sean Carter,
         Brandon Naylor, Mark Studer, Valerie Galluzzi,
         their colleagues and Nathan Gupta.  April 2016.
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
    Does three simple hardware tests that illustrate
    how to make a robot blink, move and sense its environment.
    """
    # ------------------------------------------------------------------
    # Do only ONE of the following at each run.
    # Comment out the other two for each run.
    # ------------------------------------------------------------------
#     test_blink()
    test_move()
#     test_sensors()

def test_blink():
    """
    Connects to a RoseBot and does a very simple hardware test:
      -- Make an LED blink.
    """
    # ------------------------------------------------------------------
    # Construct a RoseBot, then connect to it wirelessly.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(31)  # Use the number on YOUR robot

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
    robot.connect_wifly(26)  # Use the number on YOUR robot

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
    
    while True:
        print(robot.right_encoder.read())
        robot.connection.sleep(.05)

    # ------------------------------------------------------------------
    # The next 3 statements (after the PRINTs)
    # make the robot move, as follows:
    #   1. Tell the robot to start moving (spinning):
    #   2. Pause ("sleep") the Python program for 3 seconds.
    #         But the robot keeps doing whatever it was doing,
    #         so here it keeps moving during the 3 seconds.
    #   3. Tell the robot to stop.
    # ------------------------------------------------------------------
#     print()
#     print('Spinning!')
# 
#     driver.drive_pwm(100, -100)
#     connection.sleep(3.0)
#     driver.stop()
# 
#     print('Done spinning.')

    # ------------------------------------------------------------------
    # Asking the RoseBot's Connection to do a   shutdown   leaves
    # the robot in a clean state for the next run.
    # ------------------------------------------------------------------
    connection.shutdown()


def test_sensors():
    """
    Connects to a RoseBot and does a very simple hardware test:
    Repeatedly:
      -- Prints sensor readings.
    until the left proximity sensor gives a high value
    (as when you put your hand an inch from it).
    """
    # ------------------------------------------------------------------
    # Construct a RoseBot, then connect to it wirelessly.
    # ------------------------------------------------------------------
    robot = rb.RoseBot()
    robot.connect_wifly(31)  # Use the number on YOUR robot

    # ------------------------------------------------------------------
    # A RoseBot also has the following Sensor objects:
    #   -- left_proximity_sensor
    #   -- front_proximity_sensor
    #   -- right_proximity_sensor
    #
    #   -- left_reflectance_sensor
    #   -- middle_reflectance_sensor
    #   -- right_reflectance_sensor
    #
    #   -- left_bump_sensor
    #   -- right_bump_sensor
    #
    #   -- left_encoder
    #   -- right_encoder
    #
    # Your instructor will show you where each sensor is on the robot.
    #
    # Each of these sensors has a  read()  method that returns
    # the value that the sensor is currently sensing.
    #
    # Proximity sensors return values between:
    #     0 (far) and 4095 (close).
    #     [In practice in our classroom, perhaps from 0 to about 1000.]
    #
    # Reflectance sensors return values between:
    #     0 (lots of light reflected) and 4095 (little light reflected)
    #     [In practice in our classroom, perhaps from 0 to about 1000.]
    #
    # Bump sensors return 1 (bumped, that is, pressed) or 0.
    #     [Note: bump sensors are currently unreliable.]
    #
    # A wheel "encoder" indicates how many "ticks" the wheel has turned
    # since you last reset it.
    #
    # Your instructor will tell you more about sensors.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Repeatedly get and print sensor readings.
    # Stop when the left proximity sensor value is reasonably large
    # (for example, when you put your hand about an inch from it).
    # ------------------------------------------------------------------
    print()
    print('TO STOP THIS PROGRAM:')
    print('  Put your hand about 1 inch from the left')
    print('  proximity sensor (on the side of the robot).')
    print()
    print('   Reflectance         Proximity        Encoders      Bump   ')
    print('Left Middle Right   Left Front Right   Left Right  Left Right')
    print('---- ------ -----   ---- ----- -----   ---- -----  ---- -----')

    while True:
        # --------------------------------------------------------------
        # It is critical that there be a small "sleep" between
        # sensor readings.  You should usually sleep for 0.05 seconds.
        # We use a very large sleep here so that the data does not
        # appear more quickly than our eyes can absorb it.
        # --------------------------------------------------------------
        robot.connection.sleep(1)  # Usually 0.05
        print_sensors(robot)  # See below for   print_sensors  function

        # --------------------------------------------------------------
        # You may need to adjust the following number to get
        # a good value for your robot (with its left proximity sensor)
        # in your lighting (with its shadows).
        # --------------------------------------------------------------
        close_proximity = 500
        value = robot.left_proximity_sensor.read()
        if value > close_proximity:
            print('Left proximity sensor:', value)
            break

    print('---- ------ -----   ---- ----- -----   ---- -----  ---- -----')
    print('Left Middle Right   Left Front Right   Left Right  Left Right')
    print('   Reflectance         Proximity        Encoders      Bump   ')

    # ------------------------------------------------------------------
    # Asking the RoseBot's Connection to do a   shutdown   leaves
    # the robot in a clean state for the next run.
    # ------------------------------------------------------------------
    robot.connection.shutdown()


def print_sensors(robot):
    """
    Prints the current sensor readings for the reflectance,
    proximity and bump sensors, all on a single line,
    spaced to be in fixed-size columns.
    """
    format_string = '{:4}  {:4}  {:4}    {:4} {:4}  {:4}   {:4} {:4}  {:4} {:4}'
    print(format_string.format(robot.left_reflectance_sensor.read(),
                               robot.middle_reflectance_sensor.read(),
                               robot.right_reflectance_sensor.read(),
                               robot.left_proximity_sensor.read(),
                               robot.front_proximity_sensor.read(),
                               robot.right_proximity_sensor.read(),
                               robot.left_encoder.read(),
                               robot.right_encoder.read(),
                               robot.left_bump_sensor.read(),
                               robot.right_bump_sensor.read()))

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
