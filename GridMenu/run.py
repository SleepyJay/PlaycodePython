# Run Solvers

import sys
import string

from GridMenu import GridMenu

alphabet = list(string.ascii_lowercase)

grid = GridMenu(6,alphabet)

grid.clear()
grid.move('D')
print(grid.getPosition())


# print grid.moveMany(['E']) ; grid.clear()
# print grid.moveMany(['D', 'E']) ; grid.clear()
# print grid.moveMany(['U', 'E']) ; grid.clear()
# print grid.moveMany(['R', 'E']) ; grid.clear()
# print grid.moveMany(['L', 'E']) ; grid.clear()



# a b c d e f
# g h i j k l
# m n o p q r
# s t u v w x
# y z 




	
