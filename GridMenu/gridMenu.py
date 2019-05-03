
from collections import namedtuple
import string

NamedMoves = namedtuple('NamedMoves', ['enter', 'backsp', 'space', 'down', 'up', 'left', 'right'])

ENTER   = 'E'
BACKSP	= 'B'
SPACE	= 'S'
DOWN 	= 'D'
UP		= 'U'
LEFT	= 'L'
RIGHT	= 'R'

ALPHABET = list(string.ascii_uppercase)


class GridMenu(object):

    def __init__(self, cols=6, alphabet=None):
        self.cols = cols
        self.alphabet = alphabet or ALPHABET
        self.last = len(self.alphabet)-1
        self.debug = 0

        rows = int(self.last / self.cols)
        if self.last % self.cols:
            rows += 1

        self.full = self.cols * rows

        self.string = ''
        self.position = 0

    def move_many(self, moves):
        for move in moves:
            self.move(move)

        return self.string

    def move(self, move):
        if move == ENTER:
            self.grab_letter()

        elif move == BACKSP:
            self.string = self.string[:-1]

        elif move == SPACE:
            self.string += ' '

        elif move == DOWN:
            if self.at_bottom_edge():
                self.position = self.position + self.cols - self.full
                self.log_debug("DOWN + AtBottomEdge: " + self.get_letter())
            else:
                self.position += self.cols
                self.log_debug("DOWN + Else: " + self.get_letter())

            if self.in_empty_pos():
                self.move(DOWN)
                self.log_debug("DOWN + InEmpty: " + self.get_letter())

        elif move == UP:
            if self.at_top_edge():
                self.position = self.position - self.cols + self.full
                self.log_debug("UP + AtTopEdge: " + self.get_letter())
            else:
                self.position -= self.cols
                self.log_debug("UP + Else: " + self.get_letter())

            if self.in_empty_pos():
                self.move(UP)
                self.log_debug("UP + InEmpty: " + self.get_letter())

        elif move == RIGHT:
            if self.at_right_edge():
                self.position = self.position - self.cols + 1
                self.log_debug("RIGHT + AtRightEdge: " + self.get_letter())
            else:
                self.position += 1
                self.log_debug("RIGHT + Else: " + self.get_letter())

            if self.in_empty_pos():
                self.move(RIGHT)
                self.log_debug("RIGHT + InEmpty: " + self.get_letter())

        elif move == LEFT:
            if self.at_left_edge():
                self.position = self.position + self.cols - 1
                self.log_debug("LEFT + AtLeftEdge: " + self.get_letter())
            else:
                self.position -= 1
                self.log_debug("LEFT + Else: " + self.get_letter())

            if self.in_empty_pos():
                self.move(LEFT)
                self.log_debug("LEFT + InEmpty: " + self.get_letter())

    def clear(self):
        self.string = ''
        self.position = 0

    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = int(pos)

    def get_string(self):
        return self.string

    def get_letter(self):
        rtn = ''
        if self.position <= self.last:
            rtn = self.alphabet[self.position]

        return rtn

    def grab_letter(self):
        self.string += self.get_letter()

    def at_left_edge(self):
        return self.position % self.cols == 0

    def at_right_edge(self):
        return (self.position % self.cols) + 1 == self.cols

    def at_top_edge(self):
        return self.position < self.cols

    def at_bottom_edge(self):
        return self.position >= (self.full - self.cols)

    def in_empty_pos(self):
        return self.position > self.last

    def log_debug(self, message):
        if self.debug:
            print(message)
