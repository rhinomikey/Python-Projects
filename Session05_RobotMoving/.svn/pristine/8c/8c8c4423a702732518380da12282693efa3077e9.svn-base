"""
This module contains the top-level code for the RoseBot robot library.

CSSE 120 students should use this module, NOT the rosebot_low_level
module that contains lower-level implementations.
"""

########################################################################
#
# This is a purposely "stripped-down" version of the Rosebot library.
# It limits what students can do (in this first exercise) to:
#   -- Turning the LED on and off
#   -- Moving by using the   drive_pwm   method.
#
########################################################################

import rosebot_low_level as rbll
import collections

PIN = collections.namedtuple('PIN', ['pin_type', 'pin_number'])
LED_PIN = PIN(rbll.RoseBotDigitalOutput, 13)
HIGH = 1
LOW = 0


class RoseBot(object):

    def __init__(self):
        """
        Initializes a RoseBot that has:
          -- self.connection:          for Python-to-robot communication
          -- self.differential_drive:  for making the robot move
          -- self.sensors:    for getting information about its world
          -- self.camera:     for doing things with the Pixy camera
          -- self.buzzer:     for making noises
          -- self.led:        for turning the LED on and off
        """
        self.connection = None  # Established via  connect_wifly
        self.differential_drive = DifferentialDrive()
        self.sensors = Sensors()
        self.camera = Camera()
        self.buzzer = Buzzer()
        self.led = LED()

    def connect_wifly(self, robot_number):
        """
        What comes in: An integer that is the number written on the
          WiFly on the phyical RoseBot.
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Establishes a Connection that is used "under the hood" to:
               -- Send commands from the Python program to the robot.
               -- Receive information from the robot.
          -- Sets this RoseBot's  connection  instance variable
               to that Connection.
        Raises a  ConnectionFailed  exception if the connection
        cannot be establish (e.g. if the robot is not turned on).

        Example:
          robot = rb.RoseBot()
          robot.connect_wifly(23)

        Note: This method accepts its argument in any of several
        equivalent forms, per these examples:
          robot.connect_wifly(23)
          robot.connect_wifly('23')
          robot.connect_wifly('r23')
          robot.connect_wifly('r23.wlan.rose-hulman.edu')
        """
        self.connection = Connection(robot_number)
        print('Connected!  Robot is ready to run!')

        self._establish_connections_for_subcomponents()

    def connect_wired(self, com_port=None):
        """
        Similar to connect_wifly, except a wired connection.
        """
        self.connection = Connection(None, com_port)
        print('Connected!  Robot is ready to run!')

        self._establish_connections_for_subcomponents()

    def _establish_connections_for_subcomponents(self):
        """
        Private method for establishing connections to the lower-level
        objects that do the heavy lifting.
        """
        board = self.connection._low_level_connection
        lower_level_led = LED_PIN.pin_type(board, LED_PIN.pin_number)
        self.led._connect_to_board(lower_level_led)


class Connection(object):
    """
    Handles communication between the Python program
    and the robot with which it is communicating.
    """

    def __init__(self, robot_number=None, com_port=None,
                 use_log_file=False):
        """
        Establishes the PyMata3 object that is used "under the hood" to:
          -- Send commands from the Python program to the robot.
          -- Receive information from the robot.
        Raises a  ConnectionFailed  exception if the connection
        cannot be establish (e.g. if the robot is not turned on).
        """
        if robot_number is not None:
            ip_address = str(robot_number)
            if len(ip_address) == 1:
                ip_address = '0' + ip_address
            if not ip_address.startswith('r'):
                ip_address = 'r' + ip_address
            if not ip_address.endswith('.wlan.rose-hulman.edu'):
                ip_address = ip_address + '.wlan.rose-hulman.edu'
        elif com_port is not None:
            ip_address = None
            com_port = str(com_port)
            if not com_port.startswith('COM'):
                com_port = 'COM' + com_port
        else:
            ip_address = None

        connection = rbll.Connection(ip_address, com_port,
                                     use_log_file=use_log_file)
        self._low_level_connection = connection.board

    def sleep(self, seconds):
        """
        What comes in: A positive number.
        What goes out: Nothing (i.e., None).
        Side effects:
          Pauses the program for the given number of seconds.
        Example (assuming   connection   is a Connection for a RoseBot):
           connection.sleep(2.5)   [pauses the program for 2.5 seconds]

        Note that:
          1. The ROBOT continues doing whatever it was doing
               (e.g. moving).
          2. A Connection maintains a "heartbeat" to the robot.
             In part because of that, you must use the robot's
             connection.sleep   method and NOT the   time.sleep
             method to make the program pause.
        """
        self._low_level_connection.sleep(seconds)

    def shutdown(self):
        """
        Stops the program, leaving the robot in a "clean" state.
        """
        self._low_level_connection.shutdown()


class DifferentialDrive(object):
    """ A  DifferentialDrive  controls all robot movement. """

    def __init__(self):
        """
        Establishes a connection to the low-level object
        that does the heavy lifting.
        """
        self._lower_level_differential_drive = rbll.DifferentialDrive()

    def drive_pwm(self, left_wheel_power, right_wheel_power):
        """
        What comes in: Two integers, each between -255 and 255.
        What goes out: Nothing (i.e., None).
        Side effects:
          Makes the robot move at the given power levels, where
            -255 is full-speed backward and
             255 is full-speed forward.
        Examples (where   drive   is a DifferentialDrive object
        for a RoseBot that has established a Connection):
           drive.drive_pwm(255, 255)   [full speed forward]
           drive.drive_pwm(100, -100)  [spin clockwise in place]
           drive.drive_pwm(-50, -50)   [backwards very slowly]
           drive.drive_pwm(50, 200)    [forwards, veering to the left]
        Type hints:
          :type left_wheel_power:  int
          :type right_wheel_power: int
        """
        self._lower_level_differential_drive.drive_pwm(left_wheel_power,
                                                       right_wheel_power)

    def stop(self):
        """
        What comes in: Nothing (i.e., no arguments).
        What goes out: Nothing (i.e., None).
        Side effects:  Makes the robot stop.
        Example (where   drive   is a DifferentialDrive object
        for a RoseBot that has established a Connection):
           robot.stop()
        """
        self.drive_pwm(0, 0)


class LED(object):

    def on(self):
        """ Turns the LED fully ON. """
        self._lower_level_led.digital_write(HIGH)

    def off(self):
        """ Turns the LED fully OFF. """
        self._lower_level_led.digital_write(LOW)

    def _connect_to_board(self, lower_level_led):
        """
        Private method that establishes a connection to the low-level
        object that does the heavy lifting.
        """
        self._lower_level_led = lower_level_led


class Sensors(object):
    """ Not implemented (for today's exercise). """


class Camera(object):
    """ Not implemented (for today's exercise). """


class Buzzer(object):
    """ Not implemented (for today's exercise). """
