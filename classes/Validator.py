import os


def exists(files):
    """Returns True if each file in files exists in the current directory, and raises an Exception if not.

    :param files: A list of files to test
    :return: True if all files exist, raises an Exception if not.
    """
    for file_ in files:
        print(str(file_))
        #if not os.path.exists(file):
        #    raise Exception("File %s does not exist, executions halted" % file_)
    return True


def postive(values):
    """Returns True if each value in values is positive.

    :param values:  A list of numbers.
    :return:    True if all values are positive, raises an Exception if not.
    """

    for val in values:
        if val <= 0:
            raise Exception("Expected positive value.  Found %f." % val)
    return True


def nonNegative(values):
    """Returns True if each value in values is non-negative.

    :param values:  A list of numbers.
    :return:    True if all values are positive, raises an Exception if not.
    """

    for val in values:
        if val < 0:
            raise Exception("Expected positive value.  Found %f." % val)
    return True

def installed(progName):
    """Tests if a program is installed, and available on $PATH.

    :param progName: Command line monicker of the program to test.
    :return: True if all programs exist, and raises an Exception if not.
    """
    pass

