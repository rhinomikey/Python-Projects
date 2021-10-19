"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  October 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. Make a window that shows up.
    # ------------------------------------------------------------------
    
    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE: 3. Put a Frame on the window.
    # ------------------------------------------------------------------
    
    frame = ttk.Frame(root, padding=(30, 10), relief='raised')
    frame.grid()

    # ------------------------------------------------------------------
    # DONE: 4. Put a Button on the frame.
    # ------------------------------------------------------------------
    
    hello_button = ttk.Button(frame, text = 'Click Here!!!')
    hello_button.grid()
    
    hello_button['command'] = (lambda: hello())
    
    rand_button = ttk.Button(frame, text = 'No Click Here!!')
    rand_button.grid()
    
    rand_button['command'] = (lambda: rand(type_box))
    
    type_box = ttk.Entry(frame,text='Enter some text: ')
    type_box.grid()
    
    message = 'Enter Some Text in the Box\n'
    command_label = ttk.Label(frame, text=message)
    command_label.grid()
    
    number_box = ttk.Entry(frame,text='Enter some number: ')
    number_box.grid()
    
    number_button = ttk.Button(frame, text = 'Now Click Here!!')
    number_button.grid()
    
    number_button['command'] = (lambda: n_strings(type_box,number_box))
    
    message1 = 'Enter Some Number in the Box\n'
    command_label1 = ttk.Label(frame, text=message1)
    command_label1.grid()

    # ------------------------------------------------------------------
    # DONE: 5. Make your Button respond to a button-press
    #   by printing   "Hello"  on the Console.
    # ------------------------------------------------------------------
    root.mainloop()
    
def hello():
    print('Hello!!')
    
def rand(type_box):
    string = type_box.get()
    print(string)
    
def n_strings(string,number_box):
    number = int(number_box.get())
    string = string.get()
    for _ in range(number):
        print(string)

    # ------------------------------------------------------------------
    # DONE: 6. Put a second Button on the frame.
    #          Put an Entry on the frame.
    #          Make your second Button respond to a button-press
    #          by printing whatever is in the Entry on the Console.
    # ------------------------------------------------------------------
    

    # ------------------------------------------------------------------
    # DONE: 7. Put a third Button on the frame.
    #          Put a second Entry on the frame.
    #          Make your third Button respond to a button-press
    #          as follows:
    #
    #    Let N be the integer that the user had entered into the
    #    second Entry box.  (If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.)
    #
    #    Then pressing the third Button causes the string
    #    in the first Entry to be printed onto the Console, N times.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    
    
    

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
