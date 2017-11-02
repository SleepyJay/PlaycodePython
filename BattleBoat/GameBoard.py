
# Codes -- ThisPlayer:
#   U0 => unrevealed: nothing
#   U1 => unrevealed: ship_type_1
#   M0 => revealed (miss)
#   H1 => hit ship_type_1

# Codes -- OtherPlayer:
#   UX => unrevealed: unknown
#   HX => hit (unknown)

# Conv:
#   U* => UX
#   H1 => H0 only if not destroyed

import re

class GameBoard(object):
    #
    def __init__(self, size=10, grid_string=None):
        self.size = size
        self.grid = []
        self.re_cell = re.compile('(\w)(\w+)')

        if grid_string:
            self.load_board(size, grid_string)
        else:
            for y in range(0,size):
                row = []
                for x in range(0, size):
                    row.append('U0')
                self.grid.append(row)

    #
    def load_board(self, size, grid_serial_string):
        # TODO: load from given string
        positions = grid_serial_string.split(" ")
        print(positions)
        pass

    #
    def place_ship(self, id, x, y, size, horizontal=True):
        if horizontal:
            if x + size > self.size:
                # TODO: Exception?
                print("OOPS! Won't fix!")
                return
            for n in range(0, size):
                self.place_cell(x + n, y, 'U' + str(id))

        else:
            if y + size > self.size:
                # TODO: Exception?
                print("OOPS! Won't fix!")
                return
            for n in range(0, size):
                self.place_cell(x, y + n , 'U' + str(id))

    #
    def place_cell(self, x, y, code='U0'):
        self.grid[y-1][x-1] = code

    #
    def get_cell(self, x, y):
        return self.grid[y - 1][x - 1]

    #
    def attack_cell(self, x, y):
        cell = self.get_cell(x,y)
        if cell.startswith('M') or cell.startswith('H'):
            return
        elif(cell.startswith('U')):
            code, id = self.split_cell(cell)
            if id == 0:
                self.place_cell(x,y,'M0')
            else:
                self.place_cell(x,y,'H'+id)

    #
    def split_cell(self, cell_str):
        m = self.re_cell.match(cell_str)
        return m.group(1,2)

    #
    def register_hit(self, x,y,id):
        # TODO: how do I collect hits?
        pass

    #
    def is_ship_destroyed(self, id):
        # TODO: ship destroyed logic
        return 0

    #
    def to_player_repr(self, pretty=False):
        board_str = ''
        ending = ' '
        if pretty:
            ending = "\n"
        for row in self.grid:
            board_str += ' '.join(row) + ending

        return board_str

    #
    def to_opponent_repr(self, pretty=False):
        board_str = ''
        ending = ' '
        if pretty:
            ending = "\n"
        r = 1
        if pretty:
            board_str += " |".join(range(0,self.size))
        for row in self.grid:
            vals = []
            for val in row:
                if val.startswith('U'):
                    vals.append('U_')
                elif val.startswith('H'):
                    code, id = self.split_cell(val)
                    if self.is_ship_destroyed(id):
                        vals.append(val)
                    else:
                        vals.append('H0')
                else:
                    vals.append(val)
            if pretty:
                board_str += str(r) + " |"
            board_str += ' '.join(vals) + ending

        return board_str

