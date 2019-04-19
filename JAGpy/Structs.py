
"""This is a bunch of sugar around Python collections."""


#
def lookup(collection, key, if_none=None):
    """Lookup key in collection; if not found return if_none (or None)"""
    if key in collection:
        return collection[key]
    else:
        return if_none


#
def lookup_any(collection, keys, if_none=None):
    for key in keys:
        val = lookup(collection, key)

        if val:
            return val

    return if_none


#
def lookup_all(collection, keys, if_none=None):
    values = []
    for key in keys:
        val = lookup(collection, key)

        if not val:
            return if_none

        values.append(val)

    return values

