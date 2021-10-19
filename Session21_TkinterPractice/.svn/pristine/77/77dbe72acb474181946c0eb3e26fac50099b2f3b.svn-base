"""
Example showing for tkinter and ttk:
  -- ttk.Entry
  -- Using its GET and SET methods to get/set an Entry's information
     (as opposed to using a CONTROL VARIABLE as in a subsequent module)

     This is the SIMPLER way to use an Entry box.
     See a subsequent module for a more complicated alternative that is
     sometimes more convenient than this way.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology. January 2012.
"""

import tkinter
from tkinter import ttk


def main():
    # Root window and Frame on it.
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    # The Entry box.
    # The user can type a temperature (number) in it.
    temperature_entry = ttk.Entry(frame)
    temperature_entry.grid()

    # A Label, with an initial text on it.
    # Two Button's (below) will change the text to display the Entry's
    # temperature (number) in Fahrenheit or Celsius, respectively.
    message = 'Enter a temperature in the box\n'
    temperature_label = ttk.Label(frame, text=message)
    temperature_label.grid()

    # Buttons with "command" keys that specify what function
    # to call when the Button is pressed.  See the functions below.
    # Note that the functions defined by the LAMBDA expression
    # need the ENTRY and LABEL.
    f_button = ttk.Button(frame, text='Compute Fahrenheit from Celsius')
    f_button.grid()
    f_button['command'] = (lambda:
                           fahrenheit_from_celsius(temperature_entry,
                                                   temperature_label))

    c_button = ttk.Button(frame, text='Compute Celsius from Fahrenheit')
    c_button.grid()
    c_button['command'] = (lambda:
                           celsius_from_fahrenheit(temperature_entry,
                                                   temperature_label))

    root.mainloop()


def celsius_from_fahrenheit(temperature_entry, temperature_label):
    """ Displays temperature in Celsius.
      :type temperature_entry: ttk.Entry
      :type temperature_label: ttk.Label
    """
    # Get the contents (as a STRING) from the given Entry box.
    contents_of_entry_box = temperature_entry.get()

    # Convert that STRING to a floating point NUMBER.
    # Use the number to compute the corresponding Celsius temperature.
    fahrenheit = float(contents_of_entry_box)
    celsius = (5 / 9) * (fahrenheit - 32)

    # Display the computed Celsius temperature in the given Label.
    format_string = '{:0.2f} Fahrenheit is {:0.2f} Celsius\n'
    answer = format_string.format(fahrenheit, celsius)
    temperature_label['text'] = answer


def fahrenheit_from_celsius(temperature_entry, temperature_label):
    """ Displays temperature in Fahrenheit.
      :type temperature_entry: ttk.Entry
      :type temperature_label: ttk.Label
    """
    contents_of_entry_box = temperature_entry.get()

    celsius = float(contents_of_entry_box)
    fahrenheit = (celsius * (9 / 5)) + 32

    format_string = '{:0.2f} Celsius is {:0.2f} Fahrenheit\n'
    answer = format_string.format(celsius, fahrenheit)
    temperature_label['text'] = answer

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
