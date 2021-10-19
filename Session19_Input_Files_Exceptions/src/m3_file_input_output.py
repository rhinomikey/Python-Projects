"""
This module demonstrates simple ways to:
  -- READ FROM and
  -- WRITE to
TEXT files.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# DONE: 2.
#   3. READ the   example3_reading_in_one_chunk   function below,
#      then run it. [Change  main  to do so.]
#
#      Then answer these questions (RIGHT HERE IN THIS DOCUMENT):
#
#      a. If you were to change that example so that the filename is
#         NOT the name of an existing file [e.g. 'blah.txt' - try it!],
#         what happens when that example runs?

#         Write your answer here: The program breaks because it can't find the file.
#
#      b. Now suppose that the filename is the name of a file
#         that DOES exist (so reading the file works fine).
#         For the   example3_reading_in_one_chunk   function below,
#         what does its   print(s)   statement print?
#         That is, what is the value of s?
#
#         Write your answer here: It prints the file contents.
#
#   4. READ the   example4_reading_line_by_line   function below,
#      then run it. [Change  main  to do so.]
#
#      Then answer this question:
#
#      Why does the   print(line)   statement in that function
#      print a BLANK LINE after printing each line of the file?
#
#      Write your answer here: The line variable is right now a space but if you change it, it would print something in between.
#
# ***
# *** Do a COMMIT at this point and after EACH question below. ***
# ***
#
#   5. READ the   example5_writing   function below,
#      then run it. [Change  main  to do so.]
#
#      Then answer this question:
#
#      Open the   f_my_first_new_file.txt   that the   example5_writing
#      function creates/writes.  You will see that it contains:
#             This is
#             how youwrite to a file.
#      Why is the   'you'   right up against the   'write'   ?
#
#      Write your answer here: In the write statements there isn't a space at the end of the one of the lines.
#
#   6. READ the   example6_relative_filenames   function below,
#      then run it. [Change  main  to do so.]
#
#      Then answer this question:
#
#      What would the following snippet of code print?
#
#          filename = '../src/m3_file_input_output.py'
#          with open(filename, 'r') as f:  # BE CAREFUL! Use 'r'!
#              print(f.read())
#
#      Write your answer here: It would print the contents of the m3 module.
#
#   7. READ the   example7_absolute_filenames   function below,
#      then run it. [Change  main  to do so.]
#
#    *** CRITAL WARNING: The following question asks a WHAT-IF question.
#    *** Do NOT try out the code to find the answer!!!!!!
#
#      Look at the last part of the  example7_absolute_filenames
#      function.  Consider the lines:
#
#          with open(full_pathname, 'r') as f:
#              print(f.read())
#
#      What would happen if you were to change the 'r' to 'w'?
#
#   *** CRITAL WARNING: The above question asks a WHAT-IF question.
#   *** Do NOT try out the code to find the answer!!!!!!
#
#      Write your answer here: It would designate the file to written to not read.
#
#   After you have PUT YOUR ANSWERS IN THIS FILE as described above,
#   change the above TODO to DONE.
########################################################################

import os


def main():
    """ Calls the other functions in this module to demo FILE I/O. """
#     example3_reading_in_one_chunk()
#     example4_reading_line_by_line()
    example5_writing()
#     example6_relative_filenames()
#     example7_absolute_filenames()


########################################################################
# OPENs and READs the contents of the ENTIRE FILE into a string.
#
#   This is the same as the previous examples, but
#      ** DONE IN THE PROPER WAY. **
#   The  WITH  expression takes care of closing the file object f,
#   even if the  read  fails.
########################################################################
def example3_reading_in_one_chunk():
    with open('f_short_file.txt', 'r') as f:
        s = f.read()

    print(s)


########################################################################
# OPENs and READs the contents of the file LINE BY LINE.
#   Useful if the file is too big to be processed in a single string.
########################################################################
def example4_reading_line_by_line():
    with open('f_short_file.txt', 'r') as f:
        for line in f:
            # Do whatever you want with the STRING called  line, e.g.:
            print(line)


########################################################################
# Similar to the previous examples, but WRITES to the file.
########################################################################
def example5_writing():
    #   *** BE CAREFUL: *** Opening a file for writing OVERWRITES
    #                       any existing file with that name!!!
    with open('f_my_first_new_file.txt', 'w') as f:
        f.write('This is\n')
        f.write('how you')
        f.write('write to a file.\n')

    # This is one way to avoid overwriting an existing file:
    if os.path.isfile('f_my_second_new_file.txt'):
        print('File already exists. I will NOT overwrite it.')
    else:
        with open('f_my_second_new_file.txt', 'w') as f:
            f.write('This will NOT\n')
            f.write(' ** overwrite **\n')
            f.write('an existing file.\n')


########################################################################
# Shows how to read or write to files in OTHER FOLDERS.
########################################################################
def example6_relative_filenames():
    # ------------------------------------------------------------------
    # Examples:  using a pathname RELATIVE to the current folder.
    #    The notation:
    #        ..   (two dots)
    #    means to go UP one folder from the current folder.
    # ------------------------------------------------------------------
    with open('f_current_folder_file.txt', 'w') as f:
        f.write('This file is in the CURRENT folder.')

    with open('../f_parent_folder_file.txt', 'w') as f:
        f.write('This file is in the PARENT of the current folder.')

    with open('../foo/file_in_foo_folder.txt', 'r') as f:
        s = f.read()
        print(s)


def example7_absolute_filenames():
    # ------------------------------------------------------------------
    # Examples:  using an ABSOLUTE pathname.
    #
    # Note: This example will fail if your project
    #       is not in the standard place.
    # -----------------------------------------------------------------
    prefix = 'C:/EclipseWorkspaces/csse120/'
    folder = 'Session19_Input_Files_Exceptions/src/'
    filename = 'f_absolute_filename.txt'

    full_pathname = prefix + folder + filename

    with open(full_pathname, 'w') as f:
        f.write('This file is in your:\n   ')
        f.write('   ' + full_pathname + '\n')
        f.write('folder.\n')
        f.write('Do you see it now?\n')

    this_file = 'm3_file_input_output.py'
    full_pathname = prefix + folder + this_file
    # CAREFUL!  Be sure it is 'r' and not 'w' in the next line!
    with open(full_pathname, 'r') as f:
        print(f.read())

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
