from django.http import HttpResponse
from django.template import loader
from GameBoard import GameBoard
from Database import Database


#
def index(request, game_id=None, player_id=None):
    message = "You're at the game index"

    template = loader.get_template('index.html')
    context = {
        'message': message,
        'game_id': game_id,
        'player_id': player_id,
    }

    return HttpResponse(template.render(context, request))

#
def get_game_state(request, game_id, player_id):
    db = Database()
    game_id = db.get_player_game_id(player_id)
    response = db.get_game_state(game_id, player_id)
    return HttpResponse(response)

#
def attack_location(request, game_id, player_id):
    x = 0
    y = 0

#
def alter_board(request, game_id, player_id):
    x = 0
    y = 0
    val = 'U0'




# NOT IMPLEMENTED
def new_game(player_id):
    db = Database()
    response = db.new_game(player_id)
    return HttpResponse(response)

# NOT IMPLEMENTED
def join_game(game_id, player_id):
    db = Database()
    response = db.join_game(player_id, game_id)
    return HttpResponse(response)






