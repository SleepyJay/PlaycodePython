
"""Some easy number functions"""


#
def has_sign(val):
    if val < 0:
        return '-'
    elif val > 0:
        return '+'
    else:
        return 0


# While it may be Pythonic to check for an int by using Exception, it's a bit...unweildly. So, compromise?
def is_int(val):
    try:
        int(val)
    except TypeError:
        return False
    else:
        return True
