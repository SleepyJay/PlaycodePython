from django.db import models

class Game(models.Model):
    player_one_id = models.ForeignKey(Player)
    player_two_id = models.ForeignKey(Player)
    board_one_state = models.CharField(max_length=300)
    board_two_state = models.CharField(max_length=300)


