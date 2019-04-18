
"""This is a bunch of sugar around Python collections."""


#
def has_sign(val):
    if val < 0:
        return '-'
    elif val > 0:
        return '+'
    else:
        return 0

def is_int(val):
    try:
        int(val)
    except:
        return False
    else:
        return True
