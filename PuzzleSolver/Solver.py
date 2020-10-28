# Puzzler Solver Base

import random


class Solver(object):

    def __init__(self, starting_point = None, goal = None):
        self.MAX_ITERS = 1000
        self.MAX_SOLVE_ATTEMPTS = 50

        self.starting_point = self.to_int_list(starting_point)
        self.goal = self.to_int_list(goal)

        self.solutions = []
        self.prev_states = {}
        self.current_state = []
        self.iterations = []
        self.solve_attempts = 0

        self.board = None

        self.create_board()
        self.reset()

    def create_board(self):
        self.board = []

    def reset(self, to_str=None):
        to_str = to_str or self.starting_point
        vals = list(to_str)
        for i in range(self.get_range()):
            self.set_int(i, int(vals[i]))

    def get_board_state(self):
        if not self.current_state:
            self.current_state = self.calc_board_state()
        return self.current_state

    def calc_board_state(self):
        board = []
        for position in self.board:
            board.append(position['value'])
        return board

    def clear_board_state(self):
        self.current_state = []

    def to_int_list(self, str_):
        return [int(x) for x in list(str_)]

    def get_range(self):
        return len(self.starting_point)

    def get(self, index):
        return self.board[index]

    def get_int(self, index):
        pos = self.get(index)
        return pos['value']

    def set_int(self, index, int_):
        self.clear_board_state()
        pos = self.get(index)
        pos['value'] = int_

    def flip(self, index):
        position = self.get(index)
        position['value'] = (0 if position['value'] else 1)

    # move is an int
    def move(self, move):
        self.clear_board_state()
        position = self.get(move)
        for aff in position['affects']:
            self.flip(aff)

    # moves is list of ints
    def move_many(self, moves):
        for mv in moves:
            self.move(int(mv))

    def unmove(self, move):
        self.move(move)

    def get_random_move(self):
        range_ = self.get_range()
        rand_ = random.randrange(0,range_,1)
        return rand_

    def solve(self):
        self.reset()
        moves = []
        for g in range(self.MAX_ITERS):
            mv = self.get_random_move()
            self.move(mv)
            moves.append(mv)

            if self.get_board_state() == self.goal:
                moves = self.prune(moves)
                self.solutions.append(moves)
                self.iterations.append(g)
                return moves

        self.iterations.append(self.MAX_ITERS-1)
        return None

    def solve_many(self, n):
        s = 0
        for i in range(self.MAX_SOLVE_ATTEMPTS):
            while(s < n):
                solution = self.solve()
                if solution:
                    s += 1

    def solve_shortest(self, n):
        self.solve_many(n)
        best = ()
        min_ = 0
        for s in self.solutions:
            if not min or min_ > len(s):
                min_ = len(s)
                best = s

        self.solve_attempts += 1
        return best

    def confirm_solution(self, solution):
        self.reset()
        self.move_many(list(solution))
        curr = self.get_board_state()
        return curr == self.goal

    def clear_solutions(self):
        self.solutions = []

    def prune(self, solution):
        move_counts = {}
        for b in solution:
            if b in move_counts:
                move_counts[b] += 1
            else:
                move_counts[b] = 1

        pruned = []
        # moving the same position an odd number of times means you changed the value
        for (k, v) in move_counts.items():
            if v % 2:
                pruned.append(k)

        return pruned
