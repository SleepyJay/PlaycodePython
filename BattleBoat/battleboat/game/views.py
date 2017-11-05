from django.http import HttpResponse
from GameBoard import GameBoard
#from DataLayer import Database

#
#
def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

#
def get_player(name):
    pass

#
def board_test(request):
    gb = GameBoard()

    player_board = gb.to_player_repr()
    opponet_board = gb.to_opponent_repr()

    return HttpResponse("{}\n\n{}".format(player_board, opponet_board))