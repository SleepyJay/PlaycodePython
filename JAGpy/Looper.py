
"""Generic looping"""


#
def combos(start, stop, size):
    full = map(lambda x: [x], range(start, stop))

    for i in range(0, size - 1):
        full = combo_step(start, stop, full)

    return full


#
def combo_step(start, stop, items):
    my_step = []

    # [ [1,1], [0,1], ...]
    for item in items:
        # [1,1]
        for z in range(start, stop):
            cur = []
            # make copy of existing
            for x in item:
                cur.append(x)
            # add from the range
            cur.append(z)

            my_step.append(cur)

    return my_step


# Turn a number in to a list of "bits" of a given base.
def value_to_list(base, value, size=None):
    my_list = []
    high = base - 1

    it = value
    while it > high:
        res = divmod(it, base)
        it = res[0]
        my_list.append(res[1])

    my_list.append(it)

    if size:
        while len(my_list) < size:
            my_list.append(0)

    my_list.reverse()

    return my_list


#
def list_to_value(base, my_list):
    my_list.reverse()

    val = 0
    mul = 1

    for x in my_list:
        val += (x * mul)
        mul *= base

    return val
