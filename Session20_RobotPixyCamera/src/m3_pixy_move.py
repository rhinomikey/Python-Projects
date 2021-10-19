"""
This module lets you experience the RoseBot Pixy camera
by making the robot MOVE when it sees an object similar
to that one which it was trained.

Authors: Dave Fisher, Leigh Mathews, David Mutchler, Sean Carter,
         Brandon Naylor, Mark Studer, Valerie Galluzzi,
         their colleagues and PUT_YOUR_NAME_HERE.  April 2016.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosebot as rb


def main():
    """
    Calls the   CAMERA_MOVE function in this module to demo/test it.
    """
    camera_move()


def camera_move():
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
                   make the robot spin clockwise AND
                        the Buzzer play tone 220
                   for 0.25 seconds (both at the same time).
                   
              b. If its x-coordinate > 200,
                   Same as Case a, but spin COUNTER-clockwise
                   and play tone 440 (instead of 220)
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    # ------------------------------------------------------------------


main()
