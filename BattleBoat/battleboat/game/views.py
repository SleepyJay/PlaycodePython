from django.http import HttpResponse
from GameBoard import GameBoard
from DataLayer import Database

#
#
def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


#
def create_board(size=10):
    gb = GameBoard(size)

    if not str_board:
        str_board =

#
def get_player(name):
    pass

#
def board_test(request):
    gb = GameBoard()

    gb.place_cell(1, 1, "M0")
    gb.place_cell(2, 2, "U1")
    gb.place_cell(3, 3, "M0")
    gb.place_cell(4, 4, "H1")
    gb.place_cell(5, 5, "H2")
    gb.place_cell(5, 6, "U2")

    gb.place_ship(3, 10, 1, 3, 0)
    gb.place_ship(4, 4, 7, 3, 1)
    gb.place_ship(5, 10, 9, 3, 0)

    gb.attack_cell(5, 6)
    print(gb.get_cell(5, 6))

    gb.attack_cell(10, 1)
    gb.attack_cell(9, 1)
    gb.attack_cell(10, 2)
    gb.attack_cell(10, 3)
    gb.attack_cell(4, 8)
    gb.attack_cell(5, 7)

    player_board = gb.to_player_repr(True)
    opponet_board = gb.to_opponent_repr(True)


    return HttpResponse("{}\n\n{}".format(player_board, opponet_board))