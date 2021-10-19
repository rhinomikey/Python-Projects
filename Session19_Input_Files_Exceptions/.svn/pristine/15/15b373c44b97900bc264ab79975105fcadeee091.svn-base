"""
This project demonstrates EXCEPTIONS
and TRY/EXCEPT for catching and handling them.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.  January 2016.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions in this module to demo EXCEPTIONS. """
    cause_a_bunch_of_exceptions_to_happen()


def cause_a_bunch_of_exceptions_to_happen():
    ####################################################################
    # Here (below) are many of the most common Exception types.
    #   *** See  https://docs.python.org/3/library/exceptions.html  ***
    # for explanations of each.
    ####################################################################
    common_exception_types = (
        ZeroDivisionError,
        AttributeError,
        FileNotFoundError,
        IndexError,
        NameError,
        TypeError,
        ValueError,
    )

    other_exception_types = (
        AssertionError,
        ImportError,
        KeyboardInterrupt,
        OSError,
        RuntimeError,
        SyntaxError,
        UnboundLocalError,
    )

    # Loop through the common_exception_types.
    # The STUDENT'S code (below) should make each occur.
    for k in range(len(common_exception_types)):
        catch_exception(common_exception_types[k])

    # OPTIONAL: Try to generate exceptions for these Exception types
    #  by augmenting your   make_the_exception_happen  function below
    #  (see TODO 2).  WARNING: For some of them, I do not know
    #  any sensible way to generate them.
    for k in range(len(other_exception_types)):
        catch_exception(other_exception_types[k])


def catch_exception(exception_type):
    try:
        make_the_exception_happen(exception_type)
    except AssertionError:
        print('AssertionError:')
        print('  Oops! Your assertion was false!')
        print()
    except AttributeError:
        print('AttributeError:')
        print('  Hmmm ... You just don\'t have the right attribute!')
        print()
    except FileNotFoundError:
        print('FileNotFoundError:')
        print('  Oops! That file does not exist! Do you?')
        print()
    except ImportError:
        print('ImportError:')
        print('  Yikes! I cannot import that module! Is it from Venus?')
        print()
    except IndexError:
        print('IndexError:')
        print('  Well! This time you have gone TOO FAR!')
        print()
    except KeyboardInterrupt:
        print('KeyboardInterrupt:')
        print('  Whew! For a while there I thought that')
        print('  we were in an infinite loop!')
        print()
    except NameError:
        print('NameError:')
        print('  Some names exist, some don\'t. Existential, yes?')
        print()
    except OSError:
        print('OSError:')
        print('  Wow, that OS is BAD -- must be Windows! :-)')
        print()
    except RuntimeError:
        print('RuntimeError:')
        print('  Oh no, Billy Bob! What ELSE could go wrong?!')
        print()
    except SyntaxError:
        print('SyntaxError:')
        print('  BAD syntax! Bad, bad, bad!')
        print()
    except TypeError:
        print('TypeError:')
        print('  Sorry, you are not my type...')
        print()
    except UnboundLocalError:
        print('UnboundLocalError:')
        print('  Hmmm... Are you unbound? Pull yourelf together!')
        print()
    except ValueError:
        print('ValueError:')
        print('  My word! Your values are not so good, try meditation!')
        print()
    except ZeroDivisionError:
        print('ZeroDivisionError:')
        print('  No, no, no! Divions by zero! Go back to 5th grade!')
        print()


def make_the_exception_happen(exception_type):
    # ------------------------------------------------------------------
    # TODO: 2. Replace each   pass   in the following
    #   with a short snippet of code that causes the exception
    #   that is just above the   pass   to happen.
    #
    #   Here is how you can TEST whether or not
    #   you have a successful solution:
    #     For each exception that you generate,
    #     the CALLING code catches the exception
    #     and prints a short message, as in this example:
    #
    #          ZeroDivisionError:
    #            No, no, no! Divions by zero! Go back to 5th grade!
    #
    #     For each Exception type,
    #     if the name of that Exception type is NOT printed
    #     (along with a short message) by the CALLING code,
    #     then you have NOT successfully generated the Exception.
    # ------------------------------------------------------------------
    ####################################################################
    # IMPORTANT: You may NOT use a  raise  expression in this problem,
    # since that would defeat the purpose of this problem.
    ####################################################################
    if exception_type is ZeroDivisionError:
        pass
    elif exception_type is AttributeError:
        pass
    elif exception_type is FileNotFoundError:
        pass
    elif exception_type is IndexError:
        pass
    elif exception_type is NameError:
        pass
    elif exception_type is TypeError:
        pass
    elif exception_type is ValueError:
        pass


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
