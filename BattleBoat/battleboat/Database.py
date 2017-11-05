

class Database(object):

    #
    def new_game(self, player_id):
        # board_id := insert into board_table () values ();
        # game_id := insert into game_table (player_one, board_one, status)
        #   values player_id, board_id, 'open';
        # return { 'game_id': game_id, 'board_id': board_id }
        pass

    #
    def join_game(self, player, game_id):
        # if not game_id: ERROR
        # game_id := select * from game_table where id = game_id;
        # if not exists game_id: ERROR
        # if not exists player_one: ERROR
        # if exists player_two: ERROR
        # board_id := insert into board_table () values ();
        # update game_table set player_two = player.id, board_two = board_id,
        #   status = 'ready'
        # return { 'game_id': game_id, 'board_id': board_id }
        pass

    # NOT IMPLEMENTED
    def create_player(self, name):
        pass

    # NOT IMPLEMENTED
    def login_player(self, name, password):
        pass

    #
    def get_game_state(self, game_id, player_id):
        # game = select * from game_table where id = game_id
        # player_board, opponent_board =
        #   if   player_id == game.player_one: game.board_one, game.board_two
        #   elif player_id == game.player_two: game.board_two, game.board_one
        #   else: ERROR
        # player_state = select * from board_table where id = player_board
        # opponent_state = select * from board_table where id = opponent_board
        # player_gb = GameBoard(player_state.size, player_state.state)
        # opponent_gb = GameBoard(opponent_state.size, opponent_state.state)
        pass
