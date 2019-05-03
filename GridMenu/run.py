
from GridMenu.GridMenu import GridMenu

print()

for i in [3,4,5,6,7,8,9]:
    grid = GridMenu(i)

    grid.clear()
    grid.move_many(['D', 'R', 'E'])
    grid.move_many(['U', 'R', 'R', 'R', 'E'])
    grid.move_many(['D', 'R', 'E'])
    grid.move('E')
    grid.move_many(['D', 'L', 'L', 'L', 'E'])
    grid.move('S')
    grid.move_many(['D', 'R', 'R', 'E'])
    grid.move_many(['U', 'L', 'L', 'E'])
    grid.move_many(['L', 'L', 'L', 'E'])
    grid.move_many(['U', 'E'])
    grid.move_many(['U', 'L', 'L', 'E'])

    print(grid.get_string())


# a b c d e f
# g h i j k l
# m n o p q r
# s t u v w x
# y z 

