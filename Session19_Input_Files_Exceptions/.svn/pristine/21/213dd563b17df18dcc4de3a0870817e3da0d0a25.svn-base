"""
This module demonstrates how to INPUT from the CONSOLE:
  -- ints (integers)
  -- floats (floating point numbers)
  -- strings.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Nathan Gupta.  January 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# DONE: 2.  Read and run this program.  Then do the following problems,
#   putting your answers RIGHT HERE IN THIS DOCUMENT.
#
#   Write a line of code that would input an INTEGER from the console,
#   storing the integer in a variable called 'x'.
#    Write your line here: x = int(input('Please input an integer(whole number): ' ))
#
#   Write a line of code that would input an FLOAT from the console,
#   storing the float in a variable called 'x'.
#    Write your line here: x = float(input('Please input a decimal number: '))
#
#   Write a line of code that would input an STRING from the console,
#   storing the string in a variable called 'x'.
#    Write your line here: x = input('Please type any word you choose: ')
#
#   What happens if you (the user) enter something OTHER than an integer
#   (e.g., you enter   4 3   or   five   or   4.5   -- try them!)
#   when running the   input_until_a_SENTINEL_value   example?
#    Put your answer here: There is an error that is raised.
#
#   After you have PUT YOUR ANSWERS IN THIS FILE as described above,
#   change the above TODO to DONE.
########################################################################


def main():
    """ Calls the other functions in this module to demo CONSOLE IO. """
    input_a_string()
    input_an_integer()
    input_a_float()
    input_until_a_SENTINEL_value()


########################################################################
# Example: how to INPUT a STRING from the Console.
########################################################################
def input_a_string():
    print()
    print('--------------------------------------------------')
    print('Demonstrating  CONSOLE INPUT   of a STRING:')
    print('--------------------------------------------------')

    name = input('Enter your name: ')

    print('Hi, ' + name + '!  ', name, '!.  ', name)
    print('  Sorry, I have the hiccups...')


########################################################################
# Example: how to INPUT an INTEGER from the Console.
########################################################################
def input_an_integer():
    print()
    print('--------------------------------------------------')
    print('Demonstrating  CONSOLE INPUT   of an INTEGER:')
    print('--------------------------------------------------')

    age = int(input('How old are you? '))

    print('That is ' + str(age * 12) + ' months!')
    if age >= 18:
        print('You are old enough to vote, nice!')
    else:
        print('You will be able to vote in ' + str(18 - age) + ' years.')


########################################################################
# Example: how to INPUT a FLOAT (floating point number) from the Console
########################################################################
def input_a_float():
    print()
    print('--------------------------------------------------')
    print('Demonstrating  CONSOLE INPUT   of a FLOATING POINT number:')
    print('--------------------------------------------------')

    money = float(input('How much money do you have? '))

    potatoes_today = round((money / 6.46) * 10)
    potatoes_1900 = round((money / 0.140) * 10)

    print('According to Infoplease')
    print('at http://www.infoplease.com/ipa/A0873707.html')
    f_string1 = '  -- That will buy you {} pounds of potatoes today.'
    f_string2 = '  -- That would buy you {} pounds of potatoes in 1900!'
    print(f_string1.format(potatoes_today))
    print(f_string2.format(potatoes_1900))


########################################################################
# Example: how to INPUT repeatedly until a SENTINEL value is entered.
########################################################################
def input_until_a_SENTINEL_value():
    print()
    print('--------------------------------------------------')
    print('Demonstrating  CONSOLE INPUT   of integers')
    print('  that STOPS when -1 is entered as a SENTINEL value.')
    print('--------------------------------------------------')

    print('I will COUNT how many PRIME numbers you give me.')
    count = 0
    while True:
        n = int(input('Enter a positive integer (-1 to stop): '))
        if n == -1:
            break
        if is_prime(n):
            count = count + 1

    print('You entered ' + str(count) + ' prime numbers.')


def is_prime(n):
    """ Returns True if n is prime, else returns False. """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
