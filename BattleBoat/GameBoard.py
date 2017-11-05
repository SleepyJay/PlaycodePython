
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
from collections import namedtuple

class GameBoard(object):
    #
    def __init__(self, size=10, grid_string=None):
        self.size = size
        self.grid = []
        self.re_cell = re.compile('(\w)(\w+)')
        self.re_board = re.compile('([A-Z][\d_]+)')
#re.split('([A-Z][\d_]+)', stuff)[1::2]
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
        positions = re.split(self.re_board, grid_serial_string)[1::2]
        print(positions)
        pass

    #
    def place_ship(self, id, x, y, size, horizontal=True):
        if horizontal:
            if x + size > self.size:
                # TODO: Exception?
                print("OOPS! Won't fit!")
                return
            for n in range(0, size):
                self.place_cell(x + n, y, 'U' + str(id))

        else:
            if y + size > self.size:
                # TODO: Exception?
                print("OOPS! Won't fit!")
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
    def orig_to_player_repr(self, pretty=False):
        board_str = ''
        ending = ''
        joiner = ''
        i = 0
        if pretty:
            ending = "\n"
            joiner = ' '
            board_str += self.get_pretty_header()

        for row in self.grid:
            i += 1
            if pretty:
                board_str += self.get_pretty_prefix(i)

            board_str += joiner.join(row) + ending

        return board_str

    #
    def orig_to_opponent_repr(self, pretty=False):
        board_str = ''
        ending = ''
        joiner = ''
        i = 0
        if pretty:
            ending = "\n"
            joiner = ' '
            board_str += self.get_pretty_header()

        for row in self.grid:
            i += 1
            if pretty:
                board_str += self.get_pretty_prefix(i)


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


            board_str += joiner.join(vals) + ending

        return board_str

    #
    def to_player_repr(self, pretty=False):
        return self.to_board_repr(self._func_player_repr, pretty)

    #
    def to_opponent_repr(self, pretty=False):
        return self.to_board_repr(self._func_opponent_repr, pretty)
        pass

    #
    def _func_opponent_repr(self, row):
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

        return vals

    # This doesn't really do much, does it, now?
    def _func_player_repr(self, row, pretty=False):
        return row

    #
    def to_board_repr(self, repr_func, pretty=False):
        board_str = ''
        ending = ''
        joiner = ''
        i = 0
        if pretty:
            ending = "\n"
            joiner = ' '
            board_str += self.get_pretty_header()

        for row in self.grid:
            i += 1
            if pretty:
                board_str += self.get_pretty_prefix(i)

            vals = repr_func(row)

            board_str += joiner.join(vals) + ending
        return board_str

    #
    def get_pretty_header(self):
        return "\t|" + " |".join([str(x) for x in list(range(1, self.size + 1))]) + "\n"

    #
    def get_pretty_prefix(self, i):
        return str(i) + "\t|"