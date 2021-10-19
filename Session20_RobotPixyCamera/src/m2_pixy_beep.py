"""
This module lets you experience the RoseBot Pixy camera
by making the robot BEEP when it sees an object similar
to that one which it was trained.

Authors: Dave Fisher, Leigh Mathews, David Mutchler, Sean Carter,
         Brandon Naylor, Mark Studer, Valerie Galluzzi,
         their colleagues and PUT_YOUR_NAME_HERE.  April 2016.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosebot as rb


def main():
    """
    Calls the   CAMERA_BEEP  function in this module to demo/test it.
    """
    camera_beep()


def camera_beep():
    """
    What comes in: Nothing.
    What goes out:  Nothing (i.e., None).
    Side effects:
    1. Constructs and connects to a RoseBot.
    2. Repeatedly, stopping when the user puts a hand
         (or other object) close to the left proximity sensor:
         -- Sleep briefly (0.5 second).
         -- Get the largest camera block.
         -- If the block is not None,
              a. If its x-coordinate < 120,
                   make the Buzzer play tone 440 for 0.25 seconds.
              b. If its x-coordinate > 200,
                   make the Buzzer play tone 220 for 0.25 seconds.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    # ------------------------------------------------------------------
    
    robot = rb.RoseBot()
    robot.connect_wifly(26)
    while True:
        robot.connection.sleep(.5)
        block = robot.camera.get_block()
        if robot.left_proximity_sensor.read() > 500:
            robot.connection.shutdown()
            break
        if block != None:
            print(block.x)
            if block.x < 120:
                robot.buzzer.play_tone(440)
                robot.connection.sleep(.25)
                robot.buzzer.stop()
            elif block.x > 200:
                robot.buzzer.play_tone(220)
                robot.connection.sleep(.25)
                robot.buzzer.stop()
            
#             robot.buzzer.play_sound_file('Super Mario Bros. -Full.mp3')

main()
