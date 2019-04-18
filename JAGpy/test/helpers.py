

# only does size 3 (for reference)
def loop_to_3(stop=2):
    boring = []
    for x in range(0, stop):
        for y in range(0, stop):
            for z in range(0, stop):
                boring.append([x, y, z])

    return boring


